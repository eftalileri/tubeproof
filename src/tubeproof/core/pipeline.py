"""Streaming pipeline for one run: nothing waits for a whole stage to finish.

    harvest (plan) ──► bundle has transcript ──────────────────────────► map pool (LLM ×M)
                   └─► no transcript ─► audio downloads (×N, media CDN) ─► Whisper (×1) ─┘
    then: reduce → verify → synthesize (once, over everything)

Audio downloads run in parallel because the media CDN is not caption-rate-limited; Whisper
runs one at a time because a second model on the same GPU only slows both; analysis of a
video starts as soon as its transcript exists.
"""

from __future__ import annotations

import json
import queue
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from tubeproof.config import settings
from tubeproof.i18n import lang_of
from tubeproof.core.harvest import harvest
from tubeproof.core.map_stage import map_video
from tubeproof.core.reduce_stage import run_reduce
from tubeproof.core.synth_stage import write_reports
from tubeproof.core.verify_stage import run_verify
from tubeproof.llm.base import LLM
from tubeproof.models import VideoBundle
from tubeproof.sources.youtube.transcript import (captions_blocked, download_audio, fetch_transcript,
                                                transcribe_audio)
from tubeproof.store.db import Store


MIN_COVERAGE = 0.8


def coverage(tr, duration_s: int | None) -> float:
    """Share of the video the transcript reaches (1.0 when the duration is unknown)."""
    if not duration_s or not tr.segments:
        return 1.0 if not duration_s else 0.0
    last = tr.segments[-1]
    return min(1.0, (last.start + last.duration) / duration_s)


def process(run_id: str, llm: LLM, cfg: dict, *, downloads: int = 6, map_workers: int = 4,
            log=print) -> Path:
    run_dir = settings.run_dir(run_id)
    manifest = json.loads((run_dir / "manifest.json").read_text())
    topic = manifest["topic"]
    report_lang = lang_of(cfg)
    audio_dir = settings.data_dir / "audio" / run_id
    ext_dir = run_dir / "extractions"
    ext_dir.mkdir(exist_ok=True)
    store = Store()
    t0 = time.time()
    stats = {"audio": 0, "whisper": 0, "whisper_failed": 0, "mapped": 0, "map_failed": 0}
    lock = threading.Lock()
    dl_pool = ThreadPoolExecutor(downloads, thread_name_prefix="audio")
    map_pool = ThreadPoolExecutor(map_workers, thread_name_prefix="map")
    dl_futs, map_futs = [], []
    whisper_q: queue.Queue = queue.Queue()

    def elapsed() -> str:
        return f"{(time.time() - t0) / 60:4.1f} min"

    def bundle_path(vid: str) -> Path:
        return run_dir / "videos" / f"{vid}.json"

    def map_one(vid: str) -> None:
        b = VideoBundle.model_validate_json(bundle_path(vid).read_text())
        try:
            res = map_video(llm, topic, b, report_lang)
        except Exception as e:
            with lock:
                stats["map_failed"] += 1
            log(f"   ✗ analysis {vid}: {str(e)[:140]}")
            return
        (ext_dir / f"{vid}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
        with lock:
            stats["mapped"] += 1
        log(f"   ✓ analysis {vid} · claims={len(res['video']['claims'])} · ${llm.meter.usd:.2f} · {elapsed()}")

    def submit_map(vid: str) -> None:
        if (ext_dir / f"{vid}.json").exists():
            return
        with lock:
            map_futs.append(map_pool.submit(map_one, vid))

    def download(vid: str, lang: str | None) -> None:
        try:
            path = download_audio(vid, audio_dir)
        except Exception as e:
            with lock:
                stats["whisper_failed"] += 1
            log(f"   ✗ audio {vid}: {str(e)[:140]}")
            return
        with lock:
            stats["audio"] += 1
        whisper_q.put((vid, lang, path))

    def whisper_worker() -> None:
        while (item := whisper_q.get()) is not None:
            vid, lang, path = item
            t = time.time()
            try:
                tr = None
                if not captions_blocked():  # block may have lifted: captions are instant
                    try:
                        tr = fetch_transcript(vid, lang, allow_whisper=False)
                    except Exception:
                        tr = None
                tr = tr or transcribe_audio(vid, path, lang)
                dur = VideoBundle.model_validate_json(bundle_path(vid).read_text()).meta.duration_s
                if tr.source == "whisper" and coverage(tr, dur) < MIN_COVERAGE:
                    # A cut-off audio file once gave 48 s of text for a 60 min talk (2026-10-27):
                    # fetch the audio again and transcribe once more before accepting it.
                    log(f"   ⚠ coverage {vid}: {coverage(tr, dur) * 100:.0f}% → re-downloading audio")
                    path.unlink(missing_ok=True)
                    path = download_audio(vid, audio_dir)
                    tr = transcribe_audio(vid, path, lang)
                    if coverage(tr, dur) < MIN_COVERAGE:
                        log(f"   ⚠ coverage {vid}: still {coverage(tr, dur) * 100:.0f}%")
            except Exception as e:
                with lock:
                    stats["whisper_failed"] += 1
                log(f"   ✗ whisper {vid}: {str(e)[:140]}")
                continue
            b = VideoBundle.model_validate_json(bundle_path(vid).read_text())
            b.transcript, b.transcript_error = tr, None
            bundle_path(vid).write_text(b.model_dump_json(indent=1))
            store.put("transcript", vid, tr.model_dump(mode="json"))
            path.unlink(missing_ok=True)
            with lock:
                stats["whisper" if tr.source == "whisper" else "captions_late"] = \
                    stats.get("whisper" if tr.source == "whisper" else "captions_late", 0) + 1
            warn = ""
            if lang and tr.language and tr.language.split("-")[0] != lang.split("-")[0]:
                warn = f" · ⚠ language {tr.language} ≠ video {lang} (dub?)"
            log(f"   ✓ whisper {vid} · {tr.source} · {tr.language} · {time.time() - t:.0f}s · "
                f"queue {whisper_q.qsize()} · {elapsed()}{warn}")
            submit_map(vid)

    def on_bundle(b: VideoBundle) -> None:
        if b.transcript:
            submit_map(b.meta.id)
        else:
            dl_futs.append(dl_pool.submit(download, b.meta.id, b.meta.language))

    worker = threading.Thread(target=whisper_worker, name="whisper", daemon=True)
    worker.start()
    for f in sorted((run_dir / "videos").glob("*.json")):
        on_bundle(VideoBundle.model_validate_json(f.read_text()))
    if manifest.get("planned"):
        harvest(topic, [], run_id=run_id, allow_whisper=False, on_bundle=on_bundle, log=log)
    for fut in dl_futs:
        fut.result()
    whisper_q.put(None)
    worker.join()
    while True:  # map futures can still be added by the last Whisper results
        with lock:
            pending = [f for f in map_futs if not f.done()]
        if not pending:
            break
        for f in pending:
            f.result()
    dl_pool.shutdown()
    map_pool.shutdown()
    log(f"[flow] audio {stats['audio']} · whisper {stats['whisper']} (failed {stats['whisper_failed']}) · "
        f"analysis {stats['mapped']} (failed {stats['map_failed']}) · {elapsed()} · ${llm.meter.usd:.2f}")

    clusters = run_dir / "clusters.json"
    newest = max((f.stat().st_mtime for f in ext_dir.glob("*.json")), default=0)
    if clusters.exists() and clusters.stat().st_mtime > newest:
        log("[reduce] clusters up to date, skipped")  # resume must not re-roll the LLM grouping
    else:
        run_reduce(run_dir, llm, map_workers, log=log)
    run_verify(llm, run_dir, topic, cfg, workers=map_workers, log=log)
    outs = write_reports(llm, run_id, cfg, log=log)
    log(f"[flow] done · {elapsed()} · total ${llm.meter.usd:.2f} · {llm.meter.by_tier}")
    return outs[0]
