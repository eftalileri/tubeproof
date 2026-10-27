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
from tubeproof.models import Transcript, TranscriptSegment
from tubeproof.sources.youtube.metadata import ydl_opts


class TranscriptUnavailable(Exception):
    pass


BLOCK_COOLDOWN = 900
# 0 = whole video (default): the key part of a talk is often late, and selection already drops
# videos over 90 min. Set TUBEPROOF_WHISPER_MAX_MINUTES to cap transcription time.
WHISPER_MAX_MINUTES = int(os.environ.get("TUBEPROOF_WHISPER_MAX_MINUTES", "0"))
_blocked_until = 0.0
_model = None
_model_lock = threading.Lock()


def _is_block(e: Exception) -> bool:
    text = f"{type(e).__name__} {e}"
    return any(k in text for k in ("IpBlocked", "RequestBlocked", "429", "Too Many Requests"))


def captions_blocked() -> bool:
    return time.time() < _blocked_until


def _via_transcript_api(video_id: str, prefer_lang: str | None) -> Transcript:
    http.throttle("https://www.youtube.com/")
    tlist = YouTubeTranscriptApi().list(video_id)
    tracks = list(tlist)
    if not tracks:
        raise TranscriptUnavailable("no tracks")
    base = (prefer_lang or "").split("-")[0]

    def score(t) -> tuple:
        same_lang = bool(base) and t.language_code.split("-")[0] == base
        return (same_lang, not t.is_generated)

    track = max(tracks, key=score)
    fetched = track.fetch()
    segs = [TranscriptSegment(start=s.start, duration=s.duration, text=s.text) for s in fetched]
    return Transcript(video_id=video_id, language=track.language_code,
                      is_generated=track.is_generated, source="youtube_transcript_api", segments=segs)


def _via_ytdlp(video_id: str, prefer_lang: str | None) -> Transcript:
    base = (prefer_lang or "").split("-")[0]
    langs = [f"{base}-orig", base] if base else []
    langs.append(".*-orig")
    with tempfile.TemporaryDirectory() as tmp:
        opts = ydl_opts(writesubtitles=True, writeautomaticsub=True, subtitleslangs=langs,
                        subtitlesformat="json3", outtmpl=str(Path(tmp) / "%(id)s.%(ext)s"))
        http.throttle("https://www.youtube.com/")
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
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


def download_audio(video_id: str, dest_dir: str | Path) -> Path:
    """Smallest original-language audio track. The media CDN is not covered by the
    caption rate-limit, so this is safe to run in parallel."""

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
                    format="ba[format_note*=original][ext=m4a]/ba[format_note*=original]/ba",
                    format_sort=["lang", "+abr"], outtmpl=str(dest / f"{video_id}.%(ext)s"),
                    socket_timeout=30, http_chunk_size=10 * 1024 * 1024)
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])
    return next(p for p in dest.glob(f"{video_id}.*") if p.suffix not in (".part", ".ytdl"))


# Speech fed 1.5x faster: 38% less Whisper time, 98-99% identical text (measured on Turkish and
# Arabic, 2026-10-27); timestamps are scaled back. TUBEPROOF_WHISPER_TEMPO=1 disables it.
WHISPER_TEMPO = float(os.environ.get("TUBEPROOF_WHISPER_TEMPO", "1.5"))


def _decode(path: Path, tempo: float = 1.0):
    import numpy as np

    filt = ["-filter:a", f"atempo={tempo}"] if tempo != 1.0 else []
    cap = ["-t", str(WHISPER_MAX_MINUTES * 60)] if WHISPER_MAX_MINUTES > 0 else []
    raw = subprocess.run(["ffmpeg", "-nostdin", "-loglevel", "error", *cap,
                          "-i", str(path), *filt, "-f", "s16le", "-ac", "1", "-ar", "16000", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.int16).astype(np.float32) / 32768


MLX_MODEL = os.environ.get("TUBEPROOF_WHISPER_MLX_MODEL", "mlx-community/whisper-large-v3-turbo")


def _mlx_ready() -> bool:
    """Prefer mlx-whisper (Apple GPU, large-v3-turbo) when installed and its model is in the
    shared Hugging Face cache; never trigger a download implicitly."""
    try:
        import mlx_whisper  # type: ignore  # noqa: F401
        from huggingface_hub import scan_cache_dir
    except ImportError:
        return False
    try:
        return any(r.repo_id == MLX_MODEL and r.size_on_disk > 500_000_000 for r in scan_cache_dir().repos)
    except Exception:
        return False


def transcribe_audio(video_id: str, audio_path: Path, prefer_lang: str | None) -> Transcript:
    """One transcription at a time: a second concurrent model on the same GPU/CPU only slows both."""
    global _model
    engine = os.environ.get("TUBEPROOF_WHISPER") or ("mlx" if _mlx_ready() else "faster")
    lang = (prefer_lang or "").split("-")[0] or None
    k = WHISPER_TEMPO
    audio = _decode(audio_path, k)  # ffmpeg decode (+ tempo) sidesteps PyAV version mismatches
    with _model_lock:
        if engine == "mlx":
            try:
                import mlx_whisper  # type: ignore
            except ImportError as e:
                raise TranscriptUnavailable("mlx-whisper not installed") from e
            out = mlx_whisper.transcribe(audio, path_or_hf_repo=MLX_MODEL, language=lang, verbose=None)
            segs = [TranscriptSegment(start=x["start"] * k, duration=(x["end"] - x["start"]) * k,
                                      text=x["text"].strip()) for x in out.get("segments", [])]
            detected = out.get("language")
        else:
            try:
                from faster_whisper import WhisperModel  # type: ignore
            except ImportError as e:
                raise TranscriptUnavailable("whisper fallback not installed (pip install 'tubeproof[whisper]')") from e
            if _model is None:
                _model = WhisperModel(os.environ.get("TUBEPROOF_WHISPER_MODEL", "large-v3-turbo"), device="cpu",
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
        return transcribe_audio(video_id, download_audio(video_id, tmp), prefer_lang)


def fetch_transcript(video_id: str, prefer_lang: str | None = None,
                     allow_whisper: bool = False) -> Transcript:
    global _blocked_until
    errors = []
    chain = []
    if not captions_blocked():
        chain = [lambda: _via_transcript_api(video_id, prefer_lang), lambda: _via_ytdlp(video_id, prefer_lang)]
    else:
        errors.append("captions deferred: YouTube rate-limit cooldown")
    if allow_whisper:
        chain.append(lambda: _via_whisper(video_id, prefer_lang))
    for step in chain:
        try:
            return step()
        except Exception as e:  # each backend fails differently; keep trying
            if _is_block(e):
                _blocked_until = time.time() + BLOCK_COOLDOWN
            errors.append(f"{type(e).__name__}: {str(e)[:200]}")
    raise TranscriptUnavailable(" | ".join(errors))
