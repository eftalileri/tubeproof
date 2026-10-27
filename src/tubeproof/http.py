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
