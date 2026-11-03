"""Comments via youtube-comment-downloader (no key).

Both orders are fetched on purpose: "popular" is creator-influenced (pins,
hearts, held-for-review), "recent" surfaces criticism that has not been buried.
"""

from __future__ import annotations

import hashlib
import itertools

from youtube_comment_downloader import SORT_BY_POPULAR, SORT_BY_RECENT, YoutubeCommentDownloader

from tubeproof import http
from tubeproof.models import Comment
from tubeproof.sources.youtube.innertube import parse_count


def _author_hash(name: str) -> str:
    return hashlib.sha256(name.encode()).hexdigest()[:12]


def fetch_comments(video_id: str, channel_id: str | None, popular: int = 150,
                   recent: int = 60) -> list[Comment]:
    dl = YoutubeCommentDownloader()
    url = http.watch_url(video_id)
    out: dict[str, Comment] = {}
    for sort, n in ((SORT_BY_POPULAR, popular), (SORT_BY_RECENT, recent)):
        if n <= 0:
            continue
        http.throttle(url)
        for raw in itertools.islice(dl.get_comments_from_url(url, sort_by=sort), n):
            cid = raw.get("cid")
            if not cid or cid in out:
                continue
            out[cid] = Comment(
                id=cid,
                text=raw.get("text", ""),
                likes=parse_count(str(raw.get("votes") or "0")) or 0,
                author_hash=_author_hash(raw.get("author", "")),
                is_reply=bool(raw.get("reply")),
                parent_id=cid.split(".")[0] if raw.get("reply") else None,
                hearted=bool(raw.get("heart")),
                by_creator=bool(channel_id) and raw.get("channel") == channel_id,
                published_text=raw.get("time"),
            )
    return list(out.values())
