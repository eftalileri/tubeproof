"""Video and playlist metadata via yt-dlp (no API key), plus the paid-promotion flag."""

from __future__ import annotations

import re
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


def video_meta(video_id: str) -> VideoMeta:
    http.throttle("https://www.youtube.com/")
    with yt_dlp.YoutubeDL(ydl_opts()) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
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
    http.throttle("https://www.youtube.com/")
    opts = ydl_opts(extract_flat="in_playlist", playlistend=max_items)
    with yt_dlp.YoutubeDL(opts) as ydl:
        info = ydl.extract_info(f"https://www.youtube.com/playlist?list={playlist_id}", download=False)
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


def has_paid_promotion(video_id: str) -> bool | None:
    """YouTube's own "Includes paid promotion" disclosure on the watch page."""
    url = f"https://www.youtube.com/watch?v={video_id}&hl=en"
    try:
        with http.client() as c:
            resp = http.request(c, "GET", url)
        if resp.status_code != 200:
            return None
        return bool(_PAID_RE.search(resp.text))
    except Exception:
        return None
