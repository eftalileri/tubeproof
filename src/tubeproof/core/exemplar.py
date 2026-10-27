"""Exemplar measurements: what a video *does*, measured by code from its picture and transcript.

Advice mode collects what creators say works; exemplar mode looks at how a channel's own videos
are built. Numbers a model would guess badly are computed here (cuts, speech rate, frames); the
map stage's exemplar prompt only labels what it sees and hears, grounded by timestamps.

Output per video: `<run>/exemplar/<id>.json` plus `<id>/` with the thumbnail and frames.
"""

from __future__ import annotations

import json
import re
import statistics
import subprocess
from pathlib import Path

from tubeproof import http
from tubeproof.config import layout
from tubeproof.models import Transcript

# A shot change = ffmpeg scene score above this. 0.3 is ffmpeg's documented starting point; on a
# 43 min MrBeast video it gave 25 cuts/min, matching a hand count of the first minute (2026-10-27).
SCENE_THRESHOLD = 0.3
# A visual change = scene score above this: a new element, a wall drawn, a code block collapsing.
# Animated and slide-style videos change the picture without cutting; on a Code Aesthetic video with
# 0 cuts, 0.02 caught each checked change by eye (2026-10-27). Changes closer than CHANGE_MERGE_S are
# one change (continuous motion such as typing or scrolling fires on every frame).
CHANGE_THRESHOLD = 0.02
CHANGE_MERGE_S = 1.0
# Frames the model sees: the first seconds densely (the hook), the rest of the first 30 s, then the
# body at these fractions of the duration (teaching visuals live there).
FRAME_TIMES = (0, 1, 2, 3, 5, 8, 12, 20, 30)
BODY_FRACTIONS = (0.2, 0.4, 0.6, 0.8)
# Picture metrics shown to the synth model and in the report table, in this order.
PICTURE_METRICS = ("duration_s", "cuts_per_min", "cuts_first_3s", "cuts_first_10s", "cuts_first_30s",
                   "cuts_first_60s", "shot_s_median", "changes_per_min", "changes_first_30s", "change_gap_s_median")
WINDOWS = (3, 10, 30, 60)  # seconds; "first N s" metrics
# Speech metrics (keys of `speech`) in the report table, in this order.
SPEECH_METRICS = ("wpm", "wpm_first_10s", "wpm_first_30s", "first_speech_s")
_SENTENCE = re.compile(r"[.!?…]+\s+")


def cuts(video: Path) -> tuple[list[float], list[float]]:
    """One ffmpeg pass → (cut times, visual-change times). Cuts are scores above SCENE_THRESHOLD;
    changes are scores above CHANGE_THRESHOLD, merged within CHANGE_MERGE_S."""
    r = subprocess.run(["ffmpeg", "-nostdin", "-i", str(video), "-vf",
                        f"select='gt(scene,{CHANGE_THRESHOLD})',metadata=print", "-f", "null", "-"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg scene detection failed: {r.stderr[-300:]}")
    scored, t = [], None
    for line in r.stderr.splitlines():
        if "pts_time:" in line:
            t = float(line.split("pts_time:")[1].split()[0])
        elif "lavfi.scene_score=" in line and t is not None:
            scored.append((t, float(line.split("lavfi.scene_score=")[1])))
    changes: list[float] = []
    for t, _ in scored:
        if not changes or t - changes[-1] >= CHANGE_MERGE_S:
            changes.append(t)
    return [t for t, s in scored if s > SCENE_THRESHOLD], changes


def frame_times(duration_s: int) -> list[int]:
    return sorted(set(FRAME_TIMES) | {int(duration_s * f) for f in BODY_FRACTIONS})


def frames(video: Path, out_dir: Path, times: list[int]) -> list[tuple[int, Path]]:
    """(time, path) of each frame actually written: ffmpeg writes nothing for a time past the end, and
    the frame list and its times must stay paired (the model is told which second each image is)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    out = []
    for t in times:
        p = out_dir / f"f{t:04d}.jpg"
        p.unlink(missing_ok=True)  # a frame from an earlier run must not pass as written now
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(video),
                        "-frames:v", "1", "-q:v", "4", str(p)], check=True)
        if p.exists():
            out.append((t, p))
    return out


def thumbnail(video_id: str, out_dir: Path) -> Path | None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with http.client() as c:
        for name in ("maxresdefault", "hqdefault"):
            resp = http.request(c, "GET", http.thumbnail_url(video_id, name))
            if resp.status_code == 200 and len(resp.content) > 2000:  # 120x90 grey placeholder is ~1 KB
                p = out_dir / "thumb.jpg"
                p.write_bytes(resp.content)
                return p
    return None


def speech(tr: Transcript) -> dict:
    """Words per minute overall and in the first windows, first-speech time, sentence length."""
    def words_until(t: float) -> int:
        return sum(len(s.text.split()) for s in tr.segments if s.start < t)

    total = sum(len(s.text.split()) for s in tr.segments)
    end = max((s.start + s.duration for s in tr.segments), default=0)
    text = " ".join(s.text for s in tr.segments)
    sentences = [x for x in _SENTENCE.split(text) if x.strip()]
    lengths = [len(x.split()) for x in sentences]
    return {
        "first_speech_s": round(tr.segments[0].start, 1) if tr.segments else None,
        "wpm": round(total / (end / 60), 1) if end else None,
        **{f"wpm_first_{w}s": round(words_until(w) / (w / 60), 1) for w in WINDOWS},
        "words_first_3s": words_until(3),
        # Whisper/caption punctuation is approximate, so this is a rough, comparable-within-corpus number.
        "sentence_words_median": statistics.median(lengths) if lengths else None,
    }


def measure(video_id: str, video: Path, duration_s: int | None, run_dir: Path) -> dict:
    """Picture metrics, frames and thumbnail. Speech metrics need the final transcript, so the map
    stage adds them (`speech`) when it analyses the video."""
    out_dir = layout.exemplar_assets(run_dir, video_id)
    if not duration_s:
        raise ValueError(f"{video_id}: no duration in metadata; cuts per minute would be invented")
    cs, ch = cuts(video)
    dur = duration_s
    shots = [b - a for a, b in zip([0.0] + cs, cs + [float(dur)]) if b > a]
    gaps = [b - a for a, b in zip([0.0] + ch, ch + [float(dur)]) if b > a]
    shot = frames(video, out_dir / "frames", frame_times(dur))
    res = {
        "video_id": video_id,
        "duration_s": dur,
        "cuts": len(cs),
        "cuts_per_min": round(len(cs) / (dur / 60), 1),
        **{f"cuts_first_{w}s": sum(1 for t in cs if t < w) for w in WINDOWS},
        "shot_s_median": round(statistics.median(shots), 2) if shots else None,
        "cut_times_first_60s": [round(t, 2) for t in cs if t < 60],
        "changes_per_min": round(len(ch) / (dur / 60), 1),
        "changes_first_30s": sum(1 for t in ch if t < 30),
        "change_gap_s_median": round(statistics.median(gaps), 2) if gaps else None,
        "frames": [str(p) for _, p in shot],
        "thumbnail": str(p) if (p := thumbnail(video_id, out_dir)) else None,
        "frame_times": [t for t, _ in shot],  # one per frame, in the same order
    }
    out = layout.exemplar_file(run_dir, video_id)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


def load(run_dir: Path, video_id: str) -> dict | None:
    p = layout.exemplar_file(run_dir, video_id)
    return json.loads(p.read_text()) if p.exists() else None


def table(run_dir: Path) -> list[dict]:
    """Per-video rows for the report: picture metrics + the speech metrics the map stage saved."""
    rows = []
    for p in layout.exemplar_files(run_dir):
        row = json.loads(p.read_text())
        ex = layout.extraction(run_dir, p.stem)
        row["speech"] = json.loads(ex.read_text()).get("speech") if ex.exists() else None
        rows.append(row)
    return rows
