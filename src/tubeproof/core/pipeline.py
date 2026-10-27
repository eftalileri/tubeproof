"""Streaming pipeline for one run: nothing waits for a whole stage to finish.

    harvest (plan) ──► bundle has transcript (and exemplar measured) ──────────────────► map pool (LLM ×M)
                   └─► otherwise ─► one video download (×N, media CDN) ─► measure picture
                                                                     └─► split audio ─► Whisper (×1) ─┘
    then: reduce → verify → synthesize (once, over everything)

Each video is downloaded from YouTube once and everything else is cut from that file locally.
Downloads run in parallel because the media CDN is not caption-rate-limited; Whisper runs one
at a time because a second model on the same GPU only slows both; analysis of a video starts as
soon as its transcript exists.
"""

from __future__ import annotations

import queue
import threading
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from tubeproof.config import layout, settings
from tubeproof.core import exemplar
from tubeproof.i18n import base_lang, lang_of
from tubeproof.core.harvest import EXEMPLAR_BUNDLE, harvest, read_manifest, set_transcript
from tubeproof.core.map_stage import is_mapped, map_video, save_extraction, summary
from tubeproof.core.reduce_stage import run_reduce
from tubeproof.core.synth_stage import write_reports
from tubeproof.core.verify_stage import run_verify
from tubeproof.llm.base import LLM
from tubeproof.models import VideoBundle
from tubeproof.research import mode_of, verify_args
from tubeproof.sources.youtube.metadata import bot_checked
from tubeproof.sources.youtube.transcript import (CAPTIONS_DEFERRED, captions_blocked, download_media,
                                                fetch_transcript, split_audio, transcribe_audio)
from tubeproof.store.db import Store


MIN_COVERAGE = 0.8
# Per-video failure counters; any of them in exemplar mode stops the report (no partial sample).
FAILURES = ("media_failed", "whisper_failed", "map_failed")


def coverage(tr, duration_s: int | None) -> float | None:
    """Share of the video the transcript reaches; None when the metadata has no duration (the
    check cannot run, and the caller says so instead of passing it as full coverage)."""
    if not duration_s:
        return None
    if not tr.segments:
        return 0.0
    last = tr.segments[-1]
    return min(1.0, (last.start + last.duration) / duration_s)


def process(run_id: str, llm: LLM, cfg: dict, *, downloads: int = 6, map_workers: int = settings.llm_workers,
            log=print) -> Path:
    run_dir = settings.run_dir(run_id)
    manifest = read_manifest(run_dir)
    topic = manifest["topic"]
    report_lang = lang_of(cfg)
    mode = mode_of(cfg)
    media_dir = settings.media_dir(run_id, "video")
    audio_dir = settings.media_dir(run_id, "audio")
    layout.extractions(run_dir).mkdir(exist_ok=True)
    store = Store()
    t0 = time.time()
    stats: Counter = Counter()
    lock = threading.Lock()
    dl_pool = ThreadPoolExecutor(downloads, thread_name_prefix="media")
    map_pool = ThreadPoolExecutor(map_workers, thread_name_prefix="map")
    dl_futs, map_futs = [], []
    whisper_q: queue.Queue = queue.Queue()

    def elapsed() -> str:
        return f"{(time.time() - t0) / 60:4.1f} min"

    def map_one(vid: str) -> None:
        b = VideoBundle.model_validate_json(layout.bundle(run_dir, vid).read_text())
        try:
            res = map_video(llm, topic, b, report_lang, mode, run_dir)
        except Exception as e:
            with lock:
                stats["map_failed"] += 1
            log(f"   ✗ analysis {vid}: {str(e)[:140]}")
            return
        save_extraction(run_dir, res)
        with lock:
            stats["mapped"] += 1
        log(f"   ✓ analysis {vid} · {summary(res)} · ${llm.meter.usd:.2f} · {elapsed()}")

    def submit_map(vid: str) -> None:
        if is_mapped(run_dir, vid):
            return
        with lock:
            map_futs.append(map_pool.submit(map_one, vid))

    def whisper_worker() -> None:
        while (item := whisper_q.get()) is not None:
            vid, lang, path, dur = item
            t = time.time()
            try:
                tr = None
                b = VideoBundle.model_validate_json(layout.bundle(run_dir, vid).read_text())
                # Retry captions only where the harvest deferred them for a block that has since lifted;
                # a video that simply has none would cost one more watch-page load for nothing.
                if CAPTIONS_DEFERRED in (b.transcript_error or "") and not captions_blocked():
                    try:
                        tr = fetch_transcript(vid, lang, allow_whisper=False)
                    except Exception as e:  # Whisper below still runs; the reason is logged, not dropped
                        log(f"   · late captions {vid}: {str(e)[:140]} → Whisper")
                        tr = None
                tr = tr or transcribe_audio(vid, path, lang)
                if tr.source == "whisper" and coverage(tr, dur) is None:
                    log(f"   ⚠ coverage {vid}: unknown (no duration in metadata), not checked")
                elif tr.source == "whisper" and coverage(tr, dur) < MIN_COVERAGE:
                    # A cut-off audio file once gave 48 s of text for a 60 min talk (2026-10-27):
                    # fetch the audio again and transcribe once more before accepting it.
                    log(f"   ⚠ coverage {vid}: {coverage(tr, dur) * 100:.0f}% → re-downloading the video")
                    path.unlink(missing_ok=True)
                    path = fetch_audio(vid)
                    tr = transcribe_audio(vid, path, lang)
                    if coverage(tr, dur) < MIN_COVERAGE:
                        log(f"   ⚠ coverage {vid}: still {coverage(tr, dur) * 100:.0f}%")
            except Exception as e:
                with lock:
                    stats["whisper_failed"] += 1
                log(f"   ✗ whisper {vid}: {str(e)[:140]}")
                continue
            set_transcript(run_dir, b, tr, store)
            path.unlink(missing_ok=True)
            with lock:
                stats["whisper" if tr.source == "whisper" else "captions_late"] += 1
            warn = ""
            if lang and tr.language and base_lang(tr.language) != base_lang(lang):
                warn = f" · ⚠ language {tr.language} ≠ video {lang} (dub?)"
            log(f"   ✓ whisper {vid} · {tr.source} · {tr.language} · {time.time() - t:.0f}s · "
                f"queue {whisper_q.qsize()} · {elapsed()}{warn}")
            submit_map(vid)

    def fetch_audio(vid: str) -> Path:
        """Only on a repair (cut-off audio): the one place a video is downloaded a second time."""
        video = download_media(vid, media_dir)
        try:
            return split_audio(video, audio_dir)
        finally:
            video.unlink(missing_ok=True)

    def prepare(b: VideoBundle) -> None:
        """One download of the video; the picture is measured (exemplar mode) and the audio split for
        Whisper from that same file, which is then deleted."""
        vid = b.meta.id
        measure = mode == "exemplar" and exemplar.load(run_dir, vid) is None
        audio = None
        try:
            path = download_media(vid, media_dir)
            if measure:
                m = exemplar.measure(vid, path, b.meta.duration_s, run_dir)
            if not b.transcript:
                audio = split_audio(path, audio_dir)
            path.unlink(missing_ok=True)
        except Exception as e:
            with lock:
                stats["media_failed"] += 1
                stats["blocked"] += bot_checked(e)
            log(f"   ✗ media {vid}: {str(e)[:140]}")
            return
        if measure:
            log(f"   ✓ exemplar {vid} · {m['cuts_per_min']} cuts/min · first 10 s {m['cuts_first_10s']} cuts · "
                f"{m['changes_per_min']} changes/min · frames {len(m['frames'])} · {elapsed()}")
        if b.transcript:
            submit_map(vid)
        else:
            with lock:
                stats["media"] += 1
            whisper_q.put((vid, b.meta.language, audio, b.meta.duration_s))

    def on_bundle(b: VideoBundle) -> None:
        if b.transcript and not (mode == "exemplar" and exemplar.load(run_dir, b.meta.id) is None):
            submit_map(b.meta.id)
        else:
            dl_futs.append(dl_pool.submit(prepare, b))

    worker = threading.Thread(target=whisper_worker, name="whisper", daemon=True)
    worker.start()
    for f in layout.bundles(run_dir):
        on_bundle(VideoBundle.model_validate_json(f.read_text()))
    if manifest.get("planned"):
        harvest(topic, [], run_id=run_id, allow_whisper=False, on_bundle=on_bundle, log=log,
                **(EXEMPLAR_BUNDLE if mode == "exemplar" else {}))
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
    log(f"[flow] downloads → audio {stats['media']} (failed {stats['media_failed']}) · whisper {stats['whisper']} "
        f"(failed {stats['whisper_failed']}, late captions {stats['captions_late']}) · "
        + f"analysis {stats['mapped']} (failed {stats['map_failed']}) · {elapsed()} · ${llm.meter.usd:.2f}")

    if stats["blocked"]:
        raise RuntimeError(f"YouTube bot check on {stats['blocked']} downloads: wait for it to lift and re-run "
                           "(finished videos are kept)")
    if mode == "exemplar" and (failed := sum(stats[k] for k in FAILURES)):
        raise RuntimeError(f"{failed} videos failed: re-run to retry them "
                           "before writing a report on a partial sample")
    if mode == "exemplar":  # no claims to cluster or verify: the report tests rules against the videos
        outs = write_reports(llm, run_id, cfg, log=log)
        log(f"[flow] done · {elapsed()} · total ${llm.meter.usd:.2f} · {llm.meter.by_tier}")
        return outs[0]
    clusters = layout.clusters(run_dir)
    newest = max((f.stat().st_mtime for f in layout.extraction_files(run_dir)), default=0)
    if clusters.exists() and clusters.stat().st_mtime > newest:
        log("[reduce] clusters up to date, skipped")  # resume must not re-roll the LLM grouping
    else:
        run_reduce(run_dir, llm, map_workers, log=log)
    run_verify(llm, run_dir, topic, **verify_args(cfg), workers=map_workers, log=log)
    outs = write_reports(llm, run_id, cfg, log=log)
    log(f"[flow] done · {elapsed()} · total ${llm.meter.usd:.2f} · {llm.meter.by_tier}")
    return outs[0]
