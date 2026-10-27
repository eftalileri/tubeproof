"""Key-less YouTube search through the InnerTube web API.

Filters are a protobuf in the `params` field. Since YouTube's Jan 2026 filter
change only "popularity" sort and the coarse upload-date buckets still work
(sort-by-date silently falls back to relevance), so exact date windows are
enforced afterwards from video metadata.
"""

from __future__ import annotations

import base64
import re
from typing import Iterator

from tubeproof.config import DAYS_PER_MONTH
from tubeproof import http
from tubeproof.models import SearchHit

SEARCH_URL = "https://www.youtube.com/youtubei/v1/search?prettyPrint=false"
CLIENT_VERSION = "2.20261020.00.00"

SORT = {"relevance": 0, "popularity": 3}
UPLOAD = {"hour": 1, "today": 2, "week": 3, "month": 4, "year": 5}
TYPE = {"video": 1, "channel": 2, "playlist": 3}
DURATION = {"short": 1, "long": 2, "medium": 3}  # <4m, >20m, 4–20m


def build_params(sort: str = "popularity", upload: str | None = None,
                 kind: str = "video", duration: str | None = None) -> str:
    filt = bytearray()
    if upload:
        filt += bytes([0x08, UPLOAD[upload]])
    filt += bytes([0x10, TYPE[kind]])
    if duration:
        filt += bytes([0x18, DURATION[duration]])
    raw = bytearray()
    if SORT[sort]:
        raw += bytes([0x08, SORT[sort]])
    raw += bytes([0x12, len(filt)]) + filt
    return base64.b64encode(bytes(raw)).decode()


def upload_bucket(months: float) -> str | None:
    if months <= 0.25:
        return "week"
    if months <= 1:
        return "month"
    if months <= 12:
        return "year"
    return None  # wider windows: no server filter, post-filter only


_AGE_UNITS = {"second": 1 / 86400, "minute": 1 / 1440, "hour": 1 / 24, "day": 1,
              "week": 7, "month": DAYS_PER_MONTH, "year": 365.25}


def parse_age_days(text: str | None) -> int | None:
    m = re.search(r"(\d+)\s+(second|minute|hour|day|week|month|year)", text or "")
    return round(int(m.group(1)) * _AGE_UNITS[m.group(2)]) if m else None


def parse_count(text: str | None) -> int | None:
    """'1,234,567 views' / '1.2M views' / 'No views' -> int."""
    if not text:
        return None
    if text.lower().startswith("no "):
        return 0
    m = re.search(r"([\d.,]+)\s*([KMB])?", text.replace(" ", " "))
    if not m:
        return None
    num = m.group(1).replace(",", "")
    mult = {"K": 1e3, "M": 1e6, "B": 1e9}.get(m.group(2) or "", 1)
    try:
        return int(float(num) * mult)
    except ValueError:
        return None


def parse_duration(text: str | None) -> int | None:
    if not text or not re.fullmatch(r"[\d:]+", text):
        return None
    secs = 0
    for part in text.split(":"):
        secs = secs * 60 + int(part)
    return secs


def _text(node: dict | None) -> str:
    if not node:
        return ""
    if "simpleText" in node:
        return node["simpleText"]
    return "".join(r.get("text", "") for r in node.get("runs", []))


def _video(v: dict, query: str) -> SearchHit:
    owner = (v.get("ownerText") or v.get("longBylineText") or {}).get("runs", [{}])[0]
    published = _text(v.get("publishedTimeText"))
    return SearchHit(
        kind="video", id=v["videoId"], title=_text(v.get("title")),
        channel=owner.get("text"),
        channel_id=owner.get("navigationEndpoint", {}).get("browseEndpoint", {}).get("browseId"),
        views=parse_count(_text(v.get("viewCountText"))),
        published_text=published or None, approx_age_days=parse_age_days(published),
        duration_s=parse_duration(_text(v.get("lengthText"))), query=query,
    )


def _playlist(lv: dict, query: str) -> SearchHit | None:
    if lv.get("contentType") != "LOCKUP_CONTENT_TYPE_PLAYLIST":
        return None
    meta = lv.get("metadata", {}).get("lockupMetadataViewModel", {})
    channel = channel_id = None
    for row in meta.get("metadata", {}).get("contentMetadataViewModel", {}).get("metadataRows", []):
        for part in row.get("metadataParts", []):
            for run in part.get("text", {}).get("commandRuns", []):
                ep = run.get("onTap", {}).get("innertubeCommand", {}).get("browseEndpoint", {})
                if ep.get("browseId", "").startswith("UC") and not channel_id:
                    channel_id = ep["browseId"]
                    channel = part["text"]["content"].strip()
    count = None
    blob = str(lv.get("contentImage", {}))
    m = re.search(r"'text': '([\d,]+) videos?'", blob)
    if m:
        count = int(m.group(1).replace(",", ""))
    return SearchHit(kind="playlist", id=lv["contentId"],
                     title=meta.get("title", {}).get("content", ""),
                     channel=channel, channel_id=channel_id, video_count=count, query=query)


def _walk(node, query: str, hits: list[SearchHit], tokens: list[str]) -> None:
    if isinstance(node, dict):
        for k, v in node.items():
            if k == "videoRenderer" and "videoId" in v:
                hits.append(_video(v, query))
            elif k == "lockupViewModel":
                hit = _playlist(v, query)
                if hit:
                    hits.append(hit)
            elif k == "continuationCommand" and "token" in v:
                tokens.append(v["token"])
            else:
                _walk(v, query, hits, tokens)
    elif isinstance(node, list):
        for x in node:
            _walk(x, query, hits, tokens)


def search(query: str, *, kind: str = "video", months: float = 12, sort: str = "popularity",
           duration: str | None = None, limit: int = 40, hl: str = "en",
           gl: str = "US") -> Iterator[SearchHit]:
    """Yield up to `limit` hits, following continuation pages.

    The UI language is pinned to English so "5 months ago" / "1.2M views" parse
    the same everywhere; `gl` keeps results regional and the query text itself
    drives result language. `hl` is kept for the API backend's relevanceLanguage.
    """
    params = build_params(sort, upload_bucket(months), kind, duration)
    context = {"client": {"clientName": "WEB", "clientVersion": CLIENT_VERSION, "hl": "en", "gl": gl}}
    body: dict = {"context": context, "query": query, "params": params}
    seen: set[str] = set()
    rank = 0
    with http.client() as c:
        for _page in range(10):
            resp = http.request(c, "POST", SEARCH_URL, json=body)
            resp.raise_for_status()
            hits: list[SearchHit] = []
            tokens: list[str] = []
            _walk(resp.json(), query, hits, tokens)
            new = [h for h in hits if h.kind == kind and h.id not in seen]
            for h in new:
                seen.add(h.id)
                rank += 1
                h.rank_in_query = rank
                yield h
                if rank >= limit:
                    return
            if not tokens or not new:
                return
            body = {"context": context, "continuation": tokens[-1]}
