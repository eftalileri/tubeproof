"""Shared HTTP client with a per-host politeness delay and retry on 429/5xx."""

from __future__ import annotations

import random
import threading
import time
from urllib.parse import urlparse

import httpx

from tubeproof.config import settings

_last_hit: dict[str, float] = {}
_lock = threading.Lock()

YOUTUBE_HOSTS = ("youtube.com", "youtu.be")

YOUTUBE_HOME = "https://www.youtube.com/"  # throttle key for every YouTube request; base of every fetch URL
SEARCH_URL = YOUTUBE_HOME + "youtubei/v1/search?prettyPrint=false"  # InnerTube web search endpoint


def watch_url(video_id: str, **query) -> str:
    """The canonical watch-page URL (fetching: metadata, captions, audio, comments)."""
    extra = "".join(f"&{k}={v}" for k, v in query.items())
    return f"{YOUTUBE_HOME}watch?v={video_id}{extra}"


def playlist_url(playlist_id: str) -> str:
    """The playlist page yt-dlp lists (search playlists and a channel's uploads playlist)."""
    return f"{YOUTUBE_HOME}playlist?list={playlist_id}"


def short_url(video_id: str, t: int | float | None = None) -> str:
    """The youtu.be link a report cites; `t` jumps to that second."""
    return f"https://youtu.be/{video_id}" + (f"?t={int(t)}" if t is not None else "")


def norm_host(url: str) -> str:
    """Lower-case host without a leading "www.", for host-list and domain checks."""
    return (urlparse(url).hostname or "").lower().removeprefix("www.")


def url_under(url: str, prefixes: list[str]) -> bool:
    """`url` (host + path, no www.) starts with one of `prefixes`, e.g. "facebook.com/business"."""
    full = norm_host(url) + urlparse(url).path
    return any(full.startswith(p) for p in prefixes)


def host_match(host: str, hosts: tuple[str, ...]) -> bool:
    """`host` is one of `hosts` or a subdomain of one (www., m., ...)."""
    return any(host == h or host.endswith("." + h) for h in hosts)


def throttle(url: str) -> None:
    host = urlparse(url).hostname or ""
    delay = settings.youtube_delay if host_match(host, YOUTUBE_HOSTS) else settings.web_delay
    with _lock:
        wait = _last_hit.get(host, 0) + delay - time.monotonic()
        _last_hit[host] = max(time.monotonic(), _last_hit.get(host, 0) + delay)
    if wait > 0:
        time.sleep(wait + random.uniform(0, delay * 0.3))


def client() -> httpx.Client:
    return httpx.Client(
        headers={"User-Agent": settings.user_agent, "Accept-Language": "en-US,en;q=0.8"},
        timeout=settings.http_timeout,
        follow_redirects=True,
        max_redirects=8,
    )


def request(c: httpx.Client, method: str, url: str, retries: int = 3, **kw) -> httpx.Response:
    for attempt in range(retries + 1):
        throttle(url)
        resp = c.request(method, url, **kw)
        if resp.status_code not in (429, 500, 502, 503, 504) or attempt == retries:
            return resp
        time.sleep(2 ** (attempt + 1) + random.random())
    return resp
