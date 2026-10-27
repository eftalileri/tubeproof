"""Stage 1–4: discover → rank → harvest bundles → pre-filter. Resumable and cached."""

from __future__ import annotations

import json
import math
import re
import time
from collections import Counter
from datetime import date, timedelta
from pathlib import Path

from tubeproof.config import DAYS_PER_MONTH, layout, settings
from tubeproof.core.discover import Query, discover, rank_score
from tubeproof.core.screen import MIN_SCORE, TOP_SCORE, screen
from tubeproof.i18n import base_lang
from tubeproof.fetch.links import process_links
from tubeproof.filters.spam import flag_spam
from tubeproof.models import Comment, Link, PlaylistMeta, SearchHit, Transcript, VideoBundle, VideoMeta
from tubeproof.sources.youtube import comments as yt_comments
from tubeproof.sources.youtube import metadata as yt_meta
from tubeproof.sources.youtube import transcript as yt_transcript
from tubeproof.store.db import Store


def slug(text: str) -> str:
    s = re.sub(r"[^\w]+", "-", text.lower(), flags=re.UNICODE).strip("-")
    return s[:40] or "run"


def new_run_id(topic: str) -> str:
    """The id of a research that neither the caller nor its pack names."""
    return f"{date.today():%Y%m%d}-{slug(topic)}"


def _cached(store: Store, kind: str, key: str, fn, model=None):
    hit = store.get(kind, key)
    if hit is not None:
        if model is None:
            return hit
        return [model(**x) for x in hit] if isinstance(hit, list) else model(**hit)
    value = fn()
    if isinstance(value, list):
        store.put(kind, key, [v.model_dump(mode="json") for v in value])
    else:
        store.put(kind, key, value.model_dump(mode="json") if hasattr(value, "model_dump") else value)
    return value


PLAN_FIELDS = ("id", "title", "channel", "upload_date", "views", "duration_s", "language", "relevance", "reason",
               "playlists")


def read_manifest(run_dir: Path) -> dict:
    """The run's manifest. Its `topic` is the topic the corpus was collected for and is the one
    every stage uses (a later pack edit must not make verify and synth disagree)."""
    return json.loads(layout.manifest(run_dir).read_text())


def _manifest_row(vid: str, m: VideoMeta, relevance, reason, score, queries: list, playlists: list) -> dict:
    """One video row of the manifest (plan.json reads PLAN_FIELDS from it; a second row builder
    once left duration_s out)."""
    return {"id": vid, "title": m.title, "channel": m.channel, "views": m.views,
            "upload_date": str(m.upload_date), "duration_s": m.duration_s, "language": m.language,
            "relevance": relevance, "reason": reason, "score": score, "found_by_queries": queries,
            "playlists": playlists}


def video_titles(manifest: dict) -> dict[str, str]:
    return {v["id"]: v["title"] for v in manifest["videos"]}


def write_manifest(run_dir: Path, manifest: dict) -> None:
    """The run's manifest (data/, private) plus its public video list `research/<id>/plan.json`:
    which videos were selected and why, without queries or reader context."""
    layout.manifest(run_dir).write_text(json.dumps(manifest, ensure_ascii=False, indent=1))
    public = {"topic": manifest["topic"], "cutoff": manifest.get("cutoff"),
              "selected": manifest.get("harvested") or manifest.get("created"),
              "videos": [{k: v.get(k) for k in PLAN_FIELDS} for v in manifest["videos"]],
              "playlists": [{k: p.get(k) for k in ("id", "title", "channel")} for p in manifest.get("playlists", [])]}
    layout.plan(run_dir).write_text(json.dumps(public, ensure_ascii=False, indent=1))


# Exemplar analysis reads picture + transcript only: no comments, links or paid-promotion check (each
# is another YouTube request per video). Comments (~22 s) and description links (~6 s) were 28 of
# ~30 s per bundle on MrBeast videos and fed nothing (2026-10-27).
EXEMPLAR_BUNDLE = {"comments_popular": 0, "comments_recent": 0, "fetch_links": False, "paid_promotion": False}
# Uploads per channel when a pack's `channels` entry gives no `latest`.
EXEMPLAR_LATEST = 30


def harvest(topic: str, queries: list[Query], *, playlist_queries: list[Query] | None = None,
            months: float = 12, n_videos: int = 30,
            n_playlists: int = 5, playlist_videos: int = 5, per_channel: int = 2,
            market_lang: str | None = None, market_share: float = 0.25, plan_only: bool = False,
            min_views: int = 200, min_views_market: int = 100, on_bundle=None,
            comments_popular: int = 150, comments_recent: int = 60, fetch_links: bool = True, paid_promotion: bool = True,
            allow_whisper: bool = False, pack_name: str | None = None, run_id: str,
            max_duration_s: int = 90 * 60, llm=None, question: str | None = None,
            relevance_notes: str | None = None, channels: list[dict] | None = None,
            log=print) -> Path:
    """Select videos into a plan (the manifest, `planned: true`), then, unless `plan_only`, harvest
    exactly that plan. A run that already has a plan is harvested from it without re-selecting.
    On a harvested run this adds a focused pass (already-harvested videos are excluded from
    selection, the manifest is merged). `channels` ([{"id": "UC…", "latest": N}]) selects those
    channels' latest long-form uploads instead of searching (exemplar mode)."""
    store = Store()
    run_dir = settings.run_dir(run_id)
    layout.videos(run_dir).mkdir(parents=True, exist_ok=True)
    prev = read_manifest(run_dir) if layout.manifest(run_dir).exists() else None
    fill = dict(comments_popular=comments_popular, comments_recent=comments_recent, fetch_links=fetch_links,
                allow_whisper=allow_whisper, paid_promotion=paid_promotion)
    if prev and prev.get("planned"):
        if plan_only:
            raise ValueError(f"{run_id} already has a plan that is not harvested yet: run `process` on it")
        return _harvest_plan(prev, run_dir, store, fill, log, on_bundle)
    existing = {f.stem for f in layout.videos(run_dir).glob("*.json")}
    if prev:
        topic = prev["topic"]
        pack_name = prev["params"].get("pack") or pack_name
    params = dict(months=months, n_videos=n_videos, n_playlists=n_playlists, pack=pack_name,
                  market_lang=market_lang, market_share=market_share,
                  queries=[q.__dict__ for q in queries])
    store.upsert_run(run_id, topic, params, "discover")
    cutoff = date.today() - timedelta(days=round(months * DAYS_PER_MONTH))

    if channels:
        # Exemplar selection: a channel's own latest long-form uploads, no search and no gate.
        chosen, metas, reason, rel, playlists, queries_by_id = _channel_latest(channels, store, log)
        scored = {v: None for v in chosen}
    else:
        # 1. discover
        log(f"[1/4] Discovery: {len(queries)} queries")
        cand = discover(queries, months, playlist_queries=playlist_queries,
                        **({} if n_playlists else {"playlists_per_query": 0}),
                        on_progress=lambda q, c: log(f"   · {q.text!r} → {len(c.videos)} video, {len(c.playlists)} playlist"))

        # 1b. relevance gate (extract-tier LLM on titles), before any heavy fetching
        rel: dict[str, int] = {}
        if llm is not None:
            hits = [h for h in cand.videos.values() if h.id not in existing] + list(cand.playlists.values())
            rel = screen(llm, topic, question, hits, log=log, store=store, notes=relevance_notes)
            kept_v = {k: v for k, v in cand.videos.items() if rel.get(k, 0) >= MIN_SCORE}
            kept_p = {k: v for k, v in cand.playlists.items() if rel.get(k, 0) >= MIN_SCORE}
            log(f"   relevance gate: videos {len(cand.videos)} → {len(kept_v)}, playlists {len(cand.playlists)} → "
                f"{len(kept_p)} · ${llm.meter.usd:.3f}")
            cand.videos, cand.playlists = kept_v, kept_p

        # 2. metadata pool, then exact date/duration filter. Relevance comes first, popularity only
        #    orders videos *within* a relevance tier; the reader's market language gets a quota so
        #    low-view local videos are not crushed by English view counts.
        hl_of_query = {q.text: q.hl for q in queries + (playlist_queries or [])}

        def tier(vid: str) -> int:
            return rel.get(vid, MIN_SCORE)

        def pre_score(h) -> float:
            return rank_score(h.views, h.approx_age_days, query_hits=len(cand.queries_by_id[h.id]))

        def is_market(vid: str, meta: VideoMeta | None = None) -> bool:
            if not market_lang:
                return False
            if meta and meta.language:
                return base_lang(meta.language) == market_lang
            return any(hl_of_query.get(q) == market_lang for q in cand.queries_by_id.get(vid, []))

        ordered = sorted(cand.videos.values(), key=lambda h: (-tier(h.id), -pre_score(h)))
        pool_ids: list[str] = []
        for group, cap in (([h for h in ordered if tier(h.id) >= TOP_SCORE], 60),
                           ([h for h in ordered if tier(h.id) == MIN_SCORE], n_videos * 2),
                           ([h for h in ordered if is_market(h.id)], n_videos)):
            pool_ids += [h.id for h in group[:cap] if h.id not in pool_ids]
        log(f"[2/4] Metadata + ranking: {len(pool_ids)} candidates (total {len(cand.videos)})")
        metas: dict[str, VideoMeta] = {}
        dropped = {"old": 0, "long": 0}

        def fetch_meta(vid: str) -> VideoMeta | None:
            try:
                m = _cached(store, "meta", vid, lambda: yt_meta.video_meta(vid), VideoMeta)
            except Exception as e:
                log(f"   ! meta {vid}: {str(e)[:120]}")
                return None
            if m.upload_date and m.upload_date < cutoff:
                dropped["old"] += 1
                return None
            if m.duration_s and m.duration_s > max_duration_s:
                dropped["long"] += 1  # multi-hour streams: costly to analyse, rarely denser than a focused video
                return None
            return m

        for vid in pool_ids:
            if (m := fetch_meta(vid)) is not None:
                metas[vid] = m

        def age(m: VideoMeta) -> int | None:
            return (date.today() - m.upload_date).days if m.upload_date else None

        def popular_enough(vid: str, m: VideoMeta) -> bool:
            # views are a weak validation signal; local-language videos get a lower bar
            return (m.views or 0) >= (min_views_market if is_market(vid, m) else min_views)

        low = [v for v, m in metas.items() if not popular_enough(v, m)]
        scored = {vid: rank_score(m.views, age(m), m.likes, m.comment_count, len(cand.queries_by_id[vid]))
                  for vid, m in metas.items() if vid not in existing and popular_enough(vid, m)}
        chosen: list[str] = []
        reason: dict[str, str] = {}
        per_ch: dict[str, int] = {}

        def pick(ids: list[str], k: int, why: str) -> None:
            for vid in sorted(ids, key=lambda v: (-tier(v), -scored[v])):
                if k <= 0:
                    return
                ch = metas[vid].channel_id or vid
                if vid in chosen or per_ch.get(ch, 0) >= per_channel:
                    continue
                chosen.append(vid)
                reason[vid] = why
                per_ch[ch] = per_ch.get(ch, 0) + 1
                k -= 1

        if market_lang:
            pick([v for v in scored if is_market(v, metas[v])], math.ceil(n_videos * market_share),
                 f"market language ({market_lang})")
        pick([v for v in scored if tier(v) >= TOP_SCORE], n_videos - len(chosen), "relevance 3")
        pick(list(scored), n_videos - len(chosen), "relevance 2")

        # playlists = course sets; their items pass the same date, duration and relevance gates
        playlists: list[PlaylistMeta] = []
        pl_hits = sorted(cand.playlists.values(),
                         key=lambda h: (-tier(h.id), -len(cand.queries_by_id[h.id]), -(h.video_count or 0)))
        for h in pl_hits[:n_playlists]:
            try:
                pl = _cached(store, "playlist", h.id, lambda: yt_meta.playlist_meta(h.id), PlaylistMeta)
            except Exception as e:
                log(f"   ! playlist {h.id}: {str(e)[:120]}")
                continue
            items: dict[str, VideoMeta] = {}
            for vid in pl.video_ids[: playlist_videos * 3]:
                if vid in chosen or vid in existing:
                    continue
                if (m := fetch_meta(vid)) is not None:
                    items[vid] = m
            if llm is not None and items:
                item_hits = [SearchHit(kind="video", id=v, title=m.title, channel=m.channel, views=m.views)
                             for v, m in items.items()]
                item_rel = screen(llm, topic, question, item_hits, log=log, store=store, notes=relevance_notes)
                rel.update(item_rel)
                # a course earns corpus slots only with lessons on the reader's exact situation
                items = {v: m for v, m in items.items() if item_rel.get(v, 0) >= TOP_SCORE}
            taken = 0
            for vid, m in items.items():
                if taken >= playlist_videos:
                    break
                metas[vid] = m
                scored[vid] = rank_score(m.views, age(m), m.likes, m.comment_count)
                chosen.append(vid)
                reason[vid] = f"course set: {pl.title[:40]}"
                taken += 1
            if taken:
                playlists.append(pl)
        log(f"   dropped: {dropped['old']} old (<{cutoff}), {dropped['long']} long (>{max_duration_s // 60} min), "
            f"{len(low)} low-view (<{min_views})")
        log(f"   selected: {len(chosen)} videos (incl. {len(playlists)} course sets)")
        queries_by_id = cand.queries_by_id

    in_playlists = {vid: [p.id for p in playlists if vid in p.video_ids] for vid in chosen}
    manifest = {
        "run_id": run_id, "topic": topic, "planned": True, "created": time.strftime("%Y-%m-%d %H:%M"),
        "params": params, "cutoff": str(cutoff),
        "videos": [_manifest_row(v, metas[v], rel.get(v), reason.get(v), scored.get(v), queries_by_id.get(v, []),
                                 in_playlists[v]) for v in chosen],
        "playlists": [p.model_dump(mode="json") for p in playlists],
    }
    if prev:  # a focused pass keeps the earlier passes' videos, playlists and queries
        seen_v = {v["id"] for v in manifest["videos"]}
        seen_p = {p["id"] for p in manifest["playlists"]}
        manifest["videos"] = [v for v in prev["videos"] if v["id"] not in seen_v] + manifest["videos"]
        manifest["playlists"] = [p for p in prev["playlists"] if p["id"] not in seen_p] + manifest["playlists"]
        manifest["params"] = {**prev["params"], "passes": prev["params"].get("passes", [prev["params"]["queries"]])
                              + [params["queries"]]}
    write_manifest(run_dir, manifest)
    store.upsert_run(run_id, topic, manifest["params"], "planned")
    log(f"   plan saved ({len(chosen)} videos) → {layout.manifest(run_dir)}")
    if plan_only:
        return run_dir
    return _harvest_plan(manifest, run_dir, store, fill, log, on_bundle)


def _channel_latest(channels: list[dict], store: Store, log=print) -> tuple:
    """Latest long-form uploads per channel. YouTube's "UULF" + channel-id playlist holds only
    long-form videos (no Shorts, no streams), so `playlist_meta` lists them without a new API."""
    chosen, metas, reason = [], {}, {}
    for ch in channels:
        cid, n = ch["id"], int(ch.get("latest", EXEMPLAR_LATEST))
        if not cid.startswith("UC"):
            raise ValueError(f"channel id must start with UC: {cid!r}")
        pl = yt_meta.playlist_meta("UULF" + cid[2:], max_items=n + 10)
        for vid in pl.video_ids:
            if sum(1 for v in chosen if metas[v].channel_id == cid) >= n:
                break
            try:
                m = _cached(store, "meta", vid, lambda: yt_meta.video_meta(vid), VideoMeta)
            except Exception as e:  # members-only or removed: skip, the next upload takes its place
                if yt_meta.bot_checked(e):
                    raise
                log(f"   ! meta {vid}: {str(e)[:120]}")
                continue
            chosen.append(vid)
            metas[vid] = m
            reason[vid] = f"exemplar: latest {n} of {pl.channel}"
        log(f"   channel {pl.channel}: {sum(1 for v in chosen if metas[v].channel_id == cid)} videos")
    return chosen, metas, reason, {}, [], {}


def set_transcript(run_dir: Path, b: VideoBundle, tr: Transcript, store: Store) -> None:
    """The one writer of a transcript found after the harvest (repair, the pipeline's Whisper
    worker): onto the bundle file and into the transcript cache."""
    b.transcript, b.transcript_error = tr, None
    layout.bundle(run_dir, b.meta.id).write_text(b.model_dump_json(indent=1))
    store.put("transcript", b.meta.id, tr.model_dump(mode="json"))


def repair(run_id: str, *, allow_whisper: bool = True, log=print) -> dict:
    """Retry transcripts for bundles harvested without one (e.g. during a caption rate-limit).

    Captions are tried first (fast, if the block has lifted), Whisper on the audio last.
    """
    store = Store()
    run_dir = settings.run_dir(run_id)
    bundles = [b for f in sorted(layout.videos(run_dir).glob("*.json"))
               if not (b := VideoBundle.model_validate_json(f.read_text())).transcript]
    log(f"[repair] {len(bundles)} videos missing a transcript")
    fixed = 0
    for i, b in enumerate(bundles, 1):
        t0 = time.time()
        try:
            tr = yt_transcript.fetch_transcript(b.meta.id, b.meta.language, allow_whisper)
        except Exception as e:
            log(f"   ✗ {i}/{len(bundles)} {b.meta.id} · {str(e)[:160]}")
            continue
        set_transcript(run_dir, b, tr, store)
        fixed += 1
        log(f"   ✓ {i}/{len(bundles)} {b.meta.id} · {tr.source} · {tr.language} · {time.time() - t0:.0f}s")
    return {"fixed": fixed, "remaining": len(bundles) - fixed}


def bundle_stats(b: VideoBundle) -> dict:
    """Counts of one bundle (the harvest log line and the run statistics)."""
    return {"transcripts": int(b.transcript is not None),
            "words": sum(len(s.text.split()) for s in b.transcript.segments) if b.transcript else 0,
            "comments": len(b.comments), "spam": sum(1 for c in b.comments if c.spam_reasons),
            "links": len(b.links), "paid_links": sum(1 for l in b.links if l.is_paid),
            "fetched_pages": sum(1 for l in b.links if l.fetched),
            "paid_promo": int(bool(b.meta.has_paid_promotion))}


def run_stats(run_dir: Path) -> dict:
    """Harvest statistics of a run: summed `bundle_stats`, plus transcripts per language."""
    files = sorted(layout.videos(run_dir).glob("*.json"))
    counts, langs = Counter(), Counter()
    for f in files:
        b = VideoBundle.model_validate_json(f.read_text())
        counts.update(bundle_stats(b))
        if b.transcript:
            langs[b.transcript.language or "?"] += 1
    return {"videos": len(files), **counts, "langs": dict(langs)}


def _harvest_plan(plan: dict, run_dir: Path, store: Store, fill: dict, log=print, on_bundle=None) -> Path:
    """Harvest exactly the videos of a plan (no new search, no re-selection); videos that already
    have a bundle are kept. The one bundle loop for a direct harvest and a saved plan."""
    run_id, topic, params = plan["run_id"], plan["topic"], plan["params"]
    n = len(plan["videos"])
    log(f"[3/4] Harvest: {n} videos of the plan (transcript, comments, links)")
    store.upsert_run(run_id, topic, params, "harvest")
    for i, v in enumerate(plan["videos"], 1):
        out = layout.bundle(run_dir, v["id"])
        if out.exists():
            continue
        m = _cached(store, "meta", v["id"], lambda: yt_meta.video_meta(v["id"]), VideoMeta)
        b = VideoBundle(meta=m, rank_score=v.get("score"), playlist_ids=v.get("playlists", []),
                        found_by_queries=v.get("found_by_queries", []))
        _fill_bundle(b, store, **fill)
        out.write_text(b.model_dump_json(indent=1))
        if on_bundle:
            on_bundle(b)
        st = bundle_stats(b)
        log(f"   {i:>2}/{n} {v['id']} · {(m.title or '')[:48]!r} · "
            f"transcript={'✓ ' + (b.transcript.language or '') + ' ' + b.transcript.source if b.transcript else '✗'}"
            f" · comments={st['comments']} (spam {st['spam']}) · links={st['links']} (paid {st['paid_links']})"
            f"{' · PAID-PROMO' if m.has_paid_promotion else ''}")
    plan = {**plan, "planned": False, "harvested": time.strftime("%Y-%m-%d %H:%M")}
    write_manifest(run_dir, plan)
    store.upsert_run(run_id, topic, params, "harvested")
    log(f"[4/4] Done → {run_dir}")
    return run_dir


def _fill_bundle(b: VideoBundle, store: Store, *, comments_popular: int, comments_recent: int,
                 fetch_links: bool, allow_whisper: bool, paid_promotion: bool) -> None:
    """The one place a bundle is filled (paid-promotion flag, transcript, comments, links)."""
    vid, m = b.meta.id, b.meta
    if paid_promotion and m.has_paid_promotion is None:
        m.has_paid_promotion = yt_meta.has_paid_promotion(vid)
    try:
        b.transcript = _cached(store, "transcript", vid,
                               lambda: yt_transcript.fetch_transcript(vid, m.language, allow_whisper), Transcript)
    except Exception as e:
        b.transcript_error = str(e)[:400]
    if comments_popular or comments_recent:  # 0 + 0 = not wanted: skip the ~20 s comment fetch
        try:
            raw = _cached(store, "comments", vid,
                          lambda: yt_comments.fetch_comments(vid, m.channel_id, comments_popular, comments_recent),
                          Comment)
            b.comments = flag_spam(raw)
        except Exception as e:
            b.comments_error = str(e)[:400]
    if fetch_links:
        b.links = _cached(store, "links", vid, lambda: process_links(m.description), Link)
