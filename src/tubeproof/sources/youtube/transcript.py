"""Transcript fetching with a fallback chain.

1. youtube-transcript-api, original-language track (fast, works from home IPs)
2. yt-dlp `<lang>-orig` auto-subs (translated tracks get HTTP 429, so never ask for them)
3. Whisper on the audio track (optional). Audio comes from the media CDN, which the
   caption rate-limit does not touch. Engine: mlx-whisper large-v3-turbo (Apple GPU) when its
   model is already in the shared Hugging Face cache, else faster-whisper on CPU
   (TUBEPROOF_WHISPER=mlx|faster forces one).

Circuit breaker: when YouTube blocks caption requests (IpBlocked / 429) caption calls stop
for BLOCK_COOLDOWN seconds, so a soft block is not prolonged by hammering it.
"""

from __future__ import annotations

import contextlib
import fcntl
import json
import os
import subprocess
import tempfile
import threading
import time
from pathlib import Path

import yt_dlp
from youtube_transcript_api import YouTubeTranscriptApi

from tubeproof import http
from tubeproof.config import settings
from tubeproof.i18n import base_lang
from tubeproof.models import Transcript, TranscriptSegment
from tubeproof.sources.youtube.metadata import extract, ydl_opts


class TranscriptUnavailable(Exception):
    pass


BLOCK_COOLDOWN = 900
_blocked_until = 0.0
_model = None
_model_lock = threading.Lock()


def _is_block(e: Exception) -> bool:
    text = f"{type(e).__name__} {e}"
    return any(k in text for k in ("IpBlocked", "RequestBlocked", "429", "Too Many Requests"))


# Written into a bundle's transcript_error when captions were skipped for the rate-limit, so a later
# stage knows a retry may succeed (a video without captions is not retried).
CAPTIONS_DEFERRED = "captions deferred"


def captions_blocked() -> bool:
    return time.time() < _blocked_until


def _via_transcript_api(video_id: str, prefer_lang: str | None) -> Transcript:
    http.throttle(http.YOUTUBE_HOME)
    tlist = YouTubeTranscriptApi().list(video_id)
    tracks = list(tlist)
    if not tracks:
        raise TranscriptUnavailable("no tracks")
    base = base_lang(prefer_lang)

    def score(t) -> tuple:
        same_lang = bool(base) and base_lang(t.language_code) == base
        return (same_lang, not t.is_generated)

    track = max(tracks, key=score)
    fetched = track.fetch()
    segs = [TranscriptSegment(start=s.start, duration=s.duration, text=s.text) for s in fetched]
    return Transcript(video_id=video_id, language=track.language_code,
                      is_generated=track.is_generated, source="youtube_transcript_api", segments=segs)


def _via_ytdlp(video_id: str, prefer_lang: str | None) -> Transcript:
    base = base_lang(prefer_lang)
    langs = [f"{base}-orig", base] if base else []
    langs.append(".*-orig")
    with tempfile.TemporaryDirectory() as tmp:
        opts = ydl_opts(writesubtitles=True, writeautomaticsub=True, subtitleslangs=langs,
                        subtitlesformat="json3", outtmpl=str(Path(tmp) / "%(id)s.%(ext)s"))
        info = extract(video_id)
        http.throttle(http.YOUTUBE_HOME)  # the subtitle file is one more youtube.com request
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.process_ie_result(info, download=True)
        files = sorted(Path(tmp).glob(f"{video_id}.*.json3"))
        if not files:
            raise TranscriptUnavailable("yt-dlp found no original-language subtitles")
        f = files[0]
        lang = f.suffixes[0].lstrip(".") if f.suffixes else None
        data = json.loads(f.read_text())
    segs = []
    for ev in data.get("events", []):
        text = "".join(s.get("utf8", "") for s in ev.get("segs") or []).strip()
        if text:
            segs.append(TranscriptSegment(start=ev.get("tStartMs", 0) / 1000,
                                          duration=ev.get("dDurationMs", 0) / 1000, text=text))
    if not segs:
        raise TranscriptUnavailable("empty subtitle file")
    return Transcript(video_id=video_id, language=lang, is_generated=None, source="yt_dlp", segments=segs)


# kind -> yt-dlp format. video: 360p picture (enough to see a frame and detect cuts; a 43 min video
# is 118 MB, cut detection 38 s; 2026-10-27) merged with the original audio track, so exemplar mode
# fetches each video once and `split_audio` hands Whisper its track (two fetches per video tripped
# YouTube's bot check after ~45 videos; 2026-10-27).
_AUDIO = "ba[format_note*=original][ext=m4a]/ba[format_note*=original]/ba"
MEDIA_FORMATS = {
    "audio": _AUDIO,
    "video": "+".join(("bv*[height<=360][ext=mp4]", _AUDIO.split("/")[0])) + "/bv*[height<=360]+ba/b[height<=360]",
}


def download_media(video_id: str, dest_dir: str | Path, kind: str = "audio") -> Path:
    """Smallest original-language audio track (`kind="audio"`) or a 360p picture with the original
    audio (`kind="video"`). The media CDN is not covered by the caption rate-limit, so this is safe to
    run in parallel. Keep the two kinds in separate folders: an existing file is reused."""

    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    for old in dest.glob(f"{video_id}.*"):
        if old.suffix not in (".part", ".ytdl"):
            return old
    # Original track only: many videos carry 20+ AI-dubbed audio tracks, and "smallest audio"
    # picked an Arabic dub of an English video (2026-10-27). lang sort prefers the original,
    # +abr then takes its smallest bitrate (speech needs little).
    # Whole file through yt-dlp's native chunked downloader, never download_ranges: a range hands
    # the stream to ffmpeg, which YouTube throttles to near playback speed (13 MB: 6 s native vs
    # 12+ min ranged, and one stall forever; 2026-10-27).
    opts = ydl_opts(skip_download=False, noprogress=True,
                    format=MEDIA_FORMATS[kind],
                    format_sort=["lang", "+abr"] if kind == "audio" else ["lang", "res:360", "+size", "+abr"],
                    merge_output_format="mp4", outtmpl=str(dest / f"{video_id}.%(ext)s"),
                    socket_timeout=30, http_chunk_size=10 * 1024 * 1024)
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.process_ie_result(extract(video_id), download=True)
    return next(p for p in dest.glob(f"{video_id}.*") if p.suffix not in (".part", ".ytdl"))


def split_audio(video: Path, dest_dir: str | Path) -> Path:
    """The audio track of a `kind="video"` download as its own file (stream copy, no re-encode)."""
    dest = Path(dest_dir)
    dest.mkdir(parents=True, exist_ok=True)
    out = dest / f"{video.stem}.m4a"
    r = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(video), "-vn", "-c:a", "copy",
                        str(out)], capture_output=True, text=True)
    if r.returncode != 0 or not out.exists() or out.stat().st_size == 0:
        raise RuntimeError(f"no audio track in {video.name}: {r.stderr[-200:]}")
    return out




def _decode(path: Path, tempo: float = 1.0):
    import numpy as np

    filt = ["-filter:a", f"atempo={tempo}"] if tempo != 1.0 else []
    cap = ["-t", str(settings.whisper_max_minutes * 60)] if settings.whisper_max_minutes > 0 else []
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", *cap,
                          "-i", str(path), *filt, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768




def _mlx_ready() -> bool:
    """Prefer mlx-whisper (Apple GPU, large-v3-turbo) when installed and its model is in the
    shared Hugging Face cache; never trigger a download implicitly."""
    try:
        import mlx_whisper  # type: ignore  # noqa: F401
        from huggingface_hub import scan_cache_dir
    except ImportError:
        return False
    try:
        return any(r.repo_id == settings.whisper_mlx_model and r.size_on_disk > 500_000_000 for r in scan_cache_dir().repos)
    except Exception:
        return False


GPU_BUSY_GRACE = 90  # s: a low-priority run waits while a normal run used Whisper this recently


@contextlib.contextmanager
def _gpu_slot():
    """One transcription per machine, not just per process: two runs on one GPU only slow each
    other (each ~2x slower). A file lock serialises them; normal runs stamp `whisper.busy`, and a
    low-priority run waits until that stamp is GPU_BUSY_GRACE old, so it yields between files too."""
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    busy = settings.whisper_busy
    low = settings.whisper_priority == "low"
    with open(settings.whisper_lock, "w") as f:
        while low and busy.exists() and time.time() - busy.stat().st_mtime < GPU_BUSY_GRACE:
            time.sleep(5)
        fcntl.flock(f, fcntl.LOCK_EX)
        if not low:
            busy.touch()
        try:
            yield
        finally:
            if not low:
                busy.touch()
            fcntl.flock(f, fcntl.LOCK_UN)


def transcribe_audio(video_id: str, audio_path: Path, prefer_lang: str | None) -> Transcript:
    """One transcription at a time: a second concurrent model on the same GPU/CPU only slows both."""
    global _model
    engine = settings.whisper_engine or ("mlx" if _mlx_ready() else "faster")
    lang = base_lang(prefer_lang) or None
    k = settings.whisper_tempo  # timestamps are scaled back by the same factor
    audio = _decode(audio_path, k)  # ffmpeg decode (+ tempo) sidesteps PyAV version mismatches
    with _model_lock, _gpu_slot():
        if engine == "mlx":
            try:
                import mlx_whisper  # type: ignore
            except ImportError as e:
                raise TranscriptUnavailable("mlx-whisper not installed") from e
            out = mlx_whisper.transcribe(audio, path_or_hf_repo=settings.whisper_mlx_model, language=lang, verbose=None)
            segs = [TranscriptSegment(start=x["start"] * k, duration=(x["end"] - x["start"]) * k,
                                      text=x["text"].strip()) for x in out.get("segments", [])]
            detected = out.get("language")
        else:
            try:
                from faster_whisper import WhisperModel  # type: ignore
            except ImportError as e:
                raise TranscriptUnavailable("whisper fallback not installed (pip install 'tubeproof[whisper]')") from e
            if _model is None:
                _model = WhisperModel(settings.whisper_model, device="cpu",
                                      compute_type="int8", cpu_threads=os.cpu_count() or 4)
            it, info = _model.transcribe(audio, language=lang, vad_filter=True, beam_size=1)
            segs = [TranscriptSegment(start=x.start * k, duration=(x.end - x.start) * k, text=x.text.strip())
                    for x in it]
            detected = info.language
    if not segs:
        raise TranscriptUnavailable("whisper produced no text")
    return Transcript(video_id=video_id, language=detected, is_generated=True, source="whisper", segments=segs)


def _via_whisper(video_id: str, prefer_lang: str | None) -> Transcript:
    with tempfile.TemporaryDirectory() as tmp:
        return transcribe_audio(video_id, download_media(video_id, tmp), prefer_lang)


def fetch_transcript(video_id: str, prefer_lang: str | None = None,
                     allow_whisper: bool = False) -> Transcript:
    global _blocked_until
    errors = []
    # (is a caption step, step): once one caption step hits the rate-limit, the next one would too.
    chain = [(True, lambda: _via_transcript_api(video_id, prefer_lang)), (True, lambda: _via_ytdlp(video_id, prefer_lang))]
    if allow_whisper:
        chain.append((False, lambda: _via_whisper(video_id, prefer_lang)))
    for is_caption, step in chain:
        if is_caption and captions_blocked():
            if CAPTIONS_DEFERRED not in errors:
                errors.append(CAPTIONS_DEFERRED)
            continue
        try:
            return step()
        except Exception as e:  # each backend fails differently; keep trying
            if _is_block(e):
                _blocked_until = time.time() + BLOCK_COOLDOWN
            errors.append(f"{type(e).__name__}: {str(e)[:200]}")
    raise TranscriptUnavailable(" | ".join(errors))
