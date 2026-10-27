"""Discovery: run every query (videos + playlists), merge, rank, pick a diverse set."""

from __future__ import annotations

import math
from collections import defaultdict
from dataclasses import dataclass, field

from tubeproof.config import DAYS_PER_MONTH
from tubeproof.models import SearchHit
from tubeproof.sources.youtube import innertube


@dataclass
class Query:
    text: str
    hl: str = "en"
    gl: str = "US"


@dataclass
class Candidates:
    videos: dict[str, SearchHit] = field(default_factory=dict)
    playlists: dict[str, SearchHit] = field(default_factory=dict)
    queries_by_id: dict[str, list[str]] = field(default_factory=lambda: defaultdict(list))


def discover(queries: list[Query], months: float, per_query: int = 30,
             playlist_queries: list[Query] | None = None, playlists_per_query: int = 8,
             min_duration_s: int = 120, on_progress=None) -> Candidates:
    """Videos come from `queries`; playlists from `playlist_queries` (course-style
    phrasings like "full course" surface playlists far better), defaulting to `queries`."""
    cand = Candidates()
    max_age = months * DAYS_PER_MONTH
    for q in queries:
        # Both orders: popularity alone drifts off-topic, relevance alone misses proven videos.
        hits = list(innertube.search(q.text, kind="video", months=months, limit=per_query // 2,
                                     sort="popularity", hl=q.hl, gl=q.gl))
        hits += list(innertube.search(q.text, kind="video", months=months, limit=per_query,
                                      sort="relevance", hl=q.hl, gl=q.gl))
        for hit in hits:
            if hit.id in cand.videos and q.text in cand.queries_by_id[hit.id]:
                continue
            if hit.approx_age_days is not None and hit.approx_age_days > max_age + 31:
                continue  # coarse server bucket; exact check happens on metadata
            if hit.duration_s is not None and hit.duration_s < min_duration_s:
                continue  # Shorts carry little transferable know-how
            cand.queries_by_id[hit.id].append(q.text)
            cand.videos.setdefault(hit.id, hit)
        if on_progress:
            on_progress(q, cand)
    for q in (playlist_queries if playlist_queries is not None else queries) if playlists_per_query else []:
        for hit in innertube.search(q.text, kind="playlist", months=months,
                                    limit=playlists_per_query, hl=q.hl, gl=q.gl):
            cand.queries_by_id[hit.id].append(q.text)
            cand.playlists.setdefault(hit.id, hit)
        if on_progress:
            on_progress(q, cand)
    return cand


def rank_score(views: int | None, age_days: int | None, likes: int | None = None,
               comments: int | None = None, query_hits: int = 1) -> float:
    """Popularity that does not just reward old mega-videos.

    log views + log views/day + engagement + bonus for matching several queries
    (a video several phrasings agree on is more on-topic).
    """
    v = max(views or 0, 1)
    age = max(age_days or 365, 1)
    score = math.log10(v) + 0.8 * math.log10(v / age + 1)
    if likes is not None and views:
        score += 25 * min(likes / views, 0.1)
    if comments is not None and views:
        score += 40 * min(comments / views, 0.02)
    score += 0.4 * math.log2(query_hits)
    return round(score, 3)
