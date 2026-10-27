"""Video and playlist metadata via yt-dlp (no API key), plus the paid-promotion flag."""

from __future__ import annotations

import copy
import re
import threading
import time
from datetime import datetime

import yt_dlp

from tubeproof import http
from tubeproof.config import settings
from tubeproof.models import Chapter, PlaylistMeta, VideoMeta


def ydl_opts(**extra) -> dict:
    """Every yt-dlp option set in the project starts here (JS runtime, quiet, no per-request sleep)."""
    return {
        "quiet": True,
        "no_warnings": True,
        "skip_download": True,
        "js_runtimes": {settings.js_runtime: {}},
        # No per-request sleep: callers already throttle once per video, and yt-dlp makes
        # several requests per extraction (sleeping on each tripled metadata time).
        **extra,
    }


# YouTube's anti-bot wall: every request from this IP fails until it lifts, so callers must stop,
# never skip the video (a skip once silently swapped a channel's latest uploads for older ones).
BOT_CHECK = "not a bot"


def bot_checked(e: BaseException) -> bool:
    return BOT_CHECK in str(e)


# The last full extraction per video, so the download and the subtitle fetch of the same run reuse it
# instead of loading the watch page again: one watch-page load per video, not three (2026-10-27).
# Stream URLs in it expire after ~6 h; INFO_TTL_S keeps well inside that.
INFO_TTL_S = 3600
_info: dict[str, tuple[float, dict]] = {}
_info_lock = threading.Lock()


def extract(video_id: str) -> dict:
    """Full yt-dlp extraction of one video (a private copy; reused for INFO_TTL_S)."""
    with _info_lock:
        hit = _info.get(video_id)
    if not hit or time.time() - hit[0] > INFO_TTL_S:
        http.throttle(http.YOUTUBE_HOME)
        with yt_dlp.YoutubeDL(ydl_opts()) as ydl:
            hit = (time.time(), ydl.extract_info(http.watch_url(video_id), download=False))
        with _info_lock:
            _info[video_id] = hit
    return copy.deepcopy(hit[1])  # yt-dlp mutates an info dict while it downloads from it


def video_meta(video_id: str) -> VideoMeta:
    info = extract(video_id)
    upload = info.get("upload_date")
    return VideoMeta(
        id=info["id"],
        title=info.get("title") or "",
        description=info.get("description") or "",
        channel=info.get("channel"),
        channel_id=info.get("channel_id"),
        channel_followers=info.get("channel_follower_count"),
        upload_date=datetime.strptime(upload, "%Y%m%d").date() if upload else None,
        duration_s=info.get("duration"),
        views=info.get("view_count"),
        likes=info.get("like_count"),
        comment_count=info.get("comment_count"),
        language=info.get("language"),
        categories=info.get("categories") or [],
        tags=info.get("tags") or [],
        chapters=[Chapter(title=c.get("title", ""), start=c.get("start_time", 0), end=c.get("end_time"))
                  for c in info.get("chapters") or []],
    )


def playlist_meta(playlist_id: str, max_items: int = 200) -> PlaylistMeta:
    http.throttle(http.YOUTUBE_HOME)
    opts = ydl_opts(extract_flat="in_playlist", playlistend=max_items)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(http.playlist_url(playlist_id), download=False)
    entries = [e for e in info.get("entries") or [] if e and e.get("id")]
    return PlaylistMeta(
        id=playlist_id, title=info.get("title") or "",
        channel=info.get("channel") or info.get("uploader"),
        channel_id=info.get("channel_id"),
        video_ids=[e["id"] for e in entries],
        video_count=info.get("playlist_count") or len(entries),
    )


# The renderer *object*, not the bare name (which also appears in generic renderer lists).
_PAID_RE = re.compile(r'"paidContentOverlay"\s*:\s*\{')


def has_paid_promotion(video_id: str) -> bool:
    """YouTube's own "Includes paid promotion" disclosure on the watch page. A page that cannot be read
    raises (with YouTube's text, so `bot_checked` sees a bot check): "unknown" must not pass silently."""
    url = http.watch_url(video_id, hl="en")
    with http.client() as c:
        resp = http.request(c, "GET", url)
    if resp.status_code != 200:
        raise RuntimeError(f"paid-promotion check of {video_id}: HTTP {resp.status_code}: {resp.text[:200]}")
    return bool(_PAID_RE.search(resp.text))
