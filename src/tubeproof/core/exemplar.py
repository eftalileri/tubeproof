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
from tubeproof.models import Transcript

# A shot change = ffmpeg scene score above this. 0.3 is ffmpeg's documented starting point; on a
# 43 min MrBeast video it gave 25 cuts/min, matching a hand count of the first minute (2026-10-27).
SCENE_THRESHOLD = 0.3
# Frames the model sees: the first seconds densely (the hook), then the rest of the first 30 s.
FRAME_TIMES = (0, 1, 2, 3, 5, 8, 12, 20, 30)
WINDOWS = (3, 10, 30, 60)  # seconds; "first N s" metrics
_SENTENCE = re.compile(r"[.!?…]+\s+")


def cuts(video: Path) -> list[float]:
    r = subprocess.run(["ffmpeg", "-nostdin", "-i", str(video), "-vf",
                        f"select='gt(scene,{SCENE_THRESHOLD})',showinfo", "-f", "null", "-"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"ffmpeg scene detection failed: {r.stderr[-300:]}")
    return [float(line.split("pts_time:")[1].split()[0]) for line in r.stderr.splitlines() if "pts_time:" in line]


def frames(video: Path, out_dir: Path) -> list[Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for t in FRAME_TIMES:
        p = out_dir / f"f{t:03d}.jpg"
        subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-ss", str(t), "-i", str(video),
                        "-frames:v", "1", "-q:v", "4", str(p)], check=True)
        if p.exists():
            paths.append(p)
    return paths


def thumbnail(video_id: str, out_dir: Path) -> Path | None:
    out_dir.mkdir(parents=True, exist_ok=True)
    with http.client() as c:
        for name in ("maxresdefault", "hqdefault"):
            resp = http.request(c, "GET", f"https://i.ytimg.com/vi/{video_id}/{name}.jpg")
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


def measure(video_id: str, video: Path, duration_s: int | None, out_root: Path) -> dict:
    """Picture metrics, frames and thumbnail. Speech metrics need the final transcript, so the map
    stage adds them (`speech`) when it analyses the video."""
    out_dir = out_root / video_id
    cs = cuts(video)
    dur = duration_s or (max(cs) if cs else 0)
    shots = [b - a for a, b in zip([0.0] + cs, cs + [float(dur)]) if b > a]
    res = {
        "video_id": video_id,
        "duration_s": dur,
        "cuts": len(cs),
        "cuts_per_min": round(len(cs) / (dur / 60), 1) if dur else None,
        **{f"cuts_first_{w}s": sum(1 for t in cs if t < w) for w in WINDOWS},
        "shot_s_median": round(statistics.median(shots), 2) if shots else None,
        "cut_times_first_60s": [round(t, 2) for t in cs if t < 60],
        "frames": [str(p) for p in frames(video, out_dir / "frames")],
        "thumbnail": str(p) if (p := thumbnail(video_id, out_dir)) else None,
        "frame_times": list(FRAME_TIMES),
    }
    (out_root / f"{video_id}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    return res


def load(run_dir: Path, video_id: str) -> dict | None:
    p = run_dir / "exemplar" / f"{video_id}.json"
    return json.loads(p.read_text()) if p.exists() else None


def table(run_dir: Path) -> list[dict]:
    """Per-video rows for the report: picture metrics + the speech metrics the map stage saved."""
    rows = []
    for p in sorted((run_dir / "exemplar").glob("*.json")):
        row = json.loads(p.read_text())
        ex = run_dir / "extractions" / p.name
        row["speech"] = json.loads(ex.read_text()).get("speech") if ex.exists() else None
        rows.append(row)
    return rows
