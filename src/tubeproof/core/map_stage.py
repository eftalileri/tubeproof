"""Stage 5 (map): per-video LLM extraction, then code-side grounding checks.

Output: runs/<id>/extractions/<video_id>.json = {video, comments, grounding}.
Resumable: videos with an existing extraction are skipped.
"""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from rapidfuzz import fuzz

from tubeproof.config import layout
from tubeproof.core import exemplar
from tubeproof.core.extraction import CommentExtraction, ExemplarExtraction, VideoExtraction
from tubeproof.core.segment import Window, fmt_ts, windows
from tubeproof.prompts import load as load_prompt
from tubeproof.llm.base import LLM, LLMError
from tubeproof.models import VideoBundle

PROMPT_VERSION = "map-v4"  # v4: topic-neutral basis/evidence wording (2026-10-27)
EXEMPLAR_PROMPT_VERSION = "exemplar-v2"
MAX_DESC_CHARS = 3000
MAX_COMMENTS = 140
MAX_COMMENT_CHARS = 450
QUOTE_MATCH_MIN = 80


def claim_budget(duration_s: int | None) -> int:
    """25 claims flattened long talks: a 59 min interview gave as many as an 11 min video
    (2026-10-27). Up to ~31 min stays 25; longer talks get 0.8 per minute, at most 50."""
    return max(25, min(50, round((duration_s or 0) / 60 * 0.8)))


def _video_input(b: VideoBundle, wins: list[Window]) -> str:
    m = b.meta
    links = "\n".join(
        f"- [{l.link_class}{', PAID' if l.is_paid else ''}] {l.resolved_url or l.url}" for l in b.links
    ) or "(none)"
    segs = "\n".join(f"[{w.seg_id} {fmt_ts(w.t_start)}-{fmt_ts(w.t_end)}] {w.text}" for w in wins)
    return (
        f"<untrusted_data>\nTITLE: {m.title}\nCHANNEL: {m.channel} ({m.channel_followers or '?'} subscribers)\n"
        f"PUBLISHED: {m.upload_date} · VIEWS: {m.views} · LIKES: {m.likes} · "
        f"YOUTUBE PAID-PROMOTION DISCLOSURE: {m.has_paid_promotion}\n"
        f"CHAPTERS: {', '.join(f'{fmt_ts(c.start)} {c.title}' for c in m.chapters) or '(none)'}\n\n"
        f"DESCRIPTION:\n{m.description[:MAX_DESC_CHARS]}\n\nDESCRIPTION LINKS (pre-classified):\n{links}\n\n"
        f"TRANSCRIPT SEGMENTS:\n{segs}\n</untrusted_data>"
    )


def _comment_input(b: VideoBundle, ext: VideoExtraction) -> tuple[str, int]:
    clean = [c for c in b.comments if not c.spam_reasons]
    top = sorted(clean, key=lambda c: -c.likes)[: MAX_COMMENTS * 2 // 3]
    ids = {c.id for c in top}
    rest = [c for c in clean if c.id not in ids][: MAX_COMMENTS - len(top)]
    chosen = top + rest
    claims = "\n".join(f"{c.claim_id}: {c.text_en}" for c in ext.claims)
    lines = "\n".join(
        f"[{c.id}] likes={c.likes}{' by_creator=true' if c.by_creator else ''}"
        f"{' reply' if c.is_reply else ''}: {c.text[:MAX_COMMENT_CHARS].replace(chr(10), ' ')}"
        for c in chosen
    )
    return (f"VIDEO: {b.meta.title}\n\nCLAIMS:\n{claims}\n\n<untrusted_data>\nCOMMENTS:\n{lines}\n"
            f"</untrusted_data>"), len(chosen)


def ground(ext, wins: list[Window], field: str = "claims") -> dict:
    """Drop items of `ext.<field>` (claims, exemplar beats, or taught concepts) whose verbatim quote cannot be found
    in the cited (or any) segment."""
    by_id = {w.seg_id: w.text for w in wins}
    full = " ".join(by_id.values())
    kept, dropped = [], []
    for c in getattr(ext, field):
        cited = " ".join(by_id.get(s, "") for s in c.seg_ids)
        score = max(fuzz.partial_ratio(c.quote, cited) if cited else 0, fuzz.partial_ratio(c.quote, full))
        (kept if score >= QUOTE_MATCH_MIN else dropped).append((c, score))
    setattr(ext, field, [c for c, _ in kept])
    valid_segs = set(by_id)
    for c in getattr(ext, field):
        c.seg_ids = [s for s in c.seg_ids if s in valid_segs]
    return {"kept": len(kept), "dropped": [{"id": getattr(c, "claim_id", None) or getattr(c, "t", None) or getattr(c, "name", None),
                                            "quote": c.quote, "score": s} for c, s in dropped]}


def _map_exemplar(llm: LLM, topic: str, b: VideoBundle, lang: str, wins: list[Window], run_dir: Path) -> dict:
    """How the video is built: code measurements + frames + transcript → ExemplarExtraction."""
    m = exemplar.load(run_dir, b.meta.id)
    if m is None:
        raise LLMError(f"no exemplar measurements for {b.meta.id}")
    sp = exemplar.speech(b.transcript)
    measured = {k: v for k, v in m.items() if k not in ("frames", "thumbnail", "video_id")} | {"speech": sp}
    images = ([m["thumbnail"]] if m["thumbnail"] else []) + m["frames"]
    system = load_prompt("map_exemplar.md", lang, topic=topic,
                         frame_times=", ".join(f"{t}s" for t in m["frame_times"][:len(m["frames"])]))
    user = _video_input(b, wins) + f"\n\nMEASURED BY CODE:\n{json.dumps(measured, ensure_ascii=False)}"
    ext = ExemplarExtraction.model_validate(
        llm.json("extract", system, user, ExemplarExtraction.model_json_schema(), images=images))
    grounding = ground(ext, wins, field="beats") | {"concepts": ground(ext.teaching, wins, field="concepts")}
    full = " ".join(w.text for w in wins)
    ext.language.examples = [x for x in ext.language.examples if fuzz.partial_ratio(x, full) >= QUOTE_MATCH_MIN]
    return {"prompt_version": EXEMPLAR_PROMPT_VERSION, "mode": "exemplar", "video_id": b.meta.id,
            "windows": [w.__dict__ for w in wins], "speech": sp, "video": ext.model_dump(mode="json"),
            "comments": None, "grounding": grounding}


def map_video(llm: LLM, topic: str, b: VideoBundle, lang: str, mode: str = "claims",
              run_dir: Path | None = None) -> dict:
    """`mode="claims"` extracts advice claims; `mode="exemplar"` describes how the video is built
    (needs the run's exemplar measurements, see core/exemplar.py)."""
    if not b.transcript:
        raise LLMError(f"no transcript: {b.transcript_error}")
    wins = windows(b.transcript)
    if mode == "exemplar":
        return _map_exemplar(llm, topic, b, lang, wins, run_dir)
    system = load_prompt("map_video.md", lang, topic=topic, max_claims=claim_budget(b.meta.duration_s))
    raw = llm.json("extract", system, _video_input(b, wins),
                   VideoExtraction.model_json_schema())
    ext = VideoExtraction.model_validate(raw)
    grounding = ground(ext, wins)
    comments = None
    if b.comments and ext.claims:
        user, n = _comment_input(b, ext)
        if n:
            raw_c = llm.json("extract", load_prompt("map_comments.md", lang, topic=topic), user,
                             CommentExtraction.model_json_schema())
            comments = CommentExtraction.model_validate(raw_c)
            known = {c.id for c in b.comments}
            comments.evidence = [e for e in comments.evidence if e.comment_id in known]
    return {
        "prompt_version": PROMPT_VERSION,
        "video_id": b.meta.id,
        "windows": [w.__dict__ for w in wins],
        "video": ext.model_dump(mode="json"),
        "comments": comments.model_dump(mode="json") if comments else None,
        "grounding": grounding,
    }


def summary(res: dict) -> str:
    """One log line per analysed video, for either mode."""
    v, g = res["video"], res["grounding"]
    if res.get("mode") == "exemplar":
        return f"beats={len(v['beats'])} (dropped {len(g['dropped'])})"
    ev = len(res["comments"]["evidence"]) if res["comments"] else 0
    return (f"claims={len(v['claims'])} (dropped {len(g['dropped'])}) · comment evidence={ev} · "
            f"clickbait={v['hype']['clickbait_score']:.2f}")


def is_mapped(run_dir: Path, video_id: str) -> bool:
    return layout.extraction(run_dir, video_id).exists()


def save_extraction(run_dir: Path, res: dict) -> None:
    """The one writer of `extractions/<id>.json` (batch map and the streaming pipeline)."""
    p = layout.extraction(run_dir, res["video_id"])
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(res, ensure_ascii=False, indent=1))


def run_map(llm: LLM, run_dir: Path, topic: str, lang: str, workers: int = 4, only: list[str] | None = None,
            mode: str = "claims", log=print) -> dict:
    todo = []
    for f in sorted(layout.videos(run_dir).glob("*.json")):
        if only and f.stem not in only:
            continue
        if is_mapped(run_dir, f.stem):
            continue
        todo.append(VideoBundle.model_validate_json(f.read_text()))
    log(f"[map] {len(todo)} videos to process ({workers} parallel)")
    done, failed = 0, {}
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(map_video, llm, topic, b, lang, mode, run_dir): b for b in todo}
        for fut in as_completed(futs):
            b = futs[fut]
            try:
                res = fut.result()
            except Exception as e:
                failed[b.meta.id] = f"{type(e).__name__}: {str(e)[:200]}"
                log(f"   ✗ {b.meta.id}: {failed[b.meta.id]}")
                continue
            save_extraction(run_dir, res)
            done += 1
            log(f"   ✓ {done}/{len(todo)} {b.meta.id} · {summary(res)} · ${llm.meter.usd:.3f}")
    return {"done": done, "failed": failed, "usd": llm.meter.usd}
