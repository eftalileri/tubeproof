"""One research = one folder `research/<id>/` (layout in `config.py`).

This module is the single place that turns a research's configuration into stage calls, so the
CLI and the MCP server stay thin and cannot drift apart.

- `pack.yaml`             public topic pack: topic, queries, official domains, breakpoints, report_lang,
                          relevance_notes (topic-specific examples for the relevance gate),
                          mode (claims | exemplar), channels (exemplar: [{id: UC…, latest: N}])
- `private/context.yaml`  the reader's question, context and hypotheses (never committed)
"""

from __future__ import annotations

from dataclasses import fields
from datetime import date
from pathlib import Path
from typing import Sequence

import yaml

from tubeproof.config import layout, settings
from tubeproof.core import harvest as core
from tubeproof.core.discover import Query
from tubeproof.models import SearchHit
from tubeproof.packs import load_pack
from tubeproof.sources.youtube import innertube

PRIVATE_KEYS = ("question", "context", "hypotheses")
# Every key a pack may carry, and the keys of its list/mapping entries. A key outside these is a typo or
# dead data (the example pack's `glossary` and breakpoint `affects` were read by nothing), so it stops the load.
PACK_KEYS = ("name", "topic", "report_lang", "mode", "months", "market", "queries", "playlist_queries",
             "official_domains", "breakpoints", "relevance_notes", "channels", "question")
_ENTRY_KEYS = {"market": ("lang", "min_share"), "breakpoints": ("name", "date"),
               "channels": core.CHANNEL_KEYS, "queries": tuple(f.name for f in fields(Query)),
               "playlist_queries": tuple(f.name for f in fields(Query))}
SEARCH_LIMIT = 15  # hits a quick search lists (CLI `search`, MCP `search_videos`)


def given(**opts) -> dict:
    """Only the options a caller set. Defaults belong to the function called (selection policy:
    core harvest; search window and region: innertube; workers: `settings.llm_workers`), never to a shell."""
    return {k: v for k, v in opts.items() if v is not None}


def load_config(run_id: str | None = None, pack: str | None = None) -> dict:
    """The pack: `pack` (a name in packs/ or a path) when given, else the pack the run was
    harvested with (recorded in its manifest), else the research folder's own pack.yaml.
    The private context is merged in when it exists."""
    if not pack and run_id and layout.manifest(settings.run_dir(run_id)).exists():
        pack = core.read_manifest(settings.run_dir(run_id))["params"].get("pack")
    cfg: dict = {}
    if pack:
        cfg = load_pack(pack)
        _check_pack(cfg, pack)
    elif run_id and settings.pack_path(run_id).exists():
        cfg = load_pack(str(settings.pack_path(run_id)))
        _check_pack(cfg, settings.pack_path(run_id))
    if run_id:
        priv = settings.context_path(run_id)
        if priv.exists():
            ctx = yaml.safe_load(priv.read_text()) or {}
            _check_context(ctx, priv)
            cfg = {**cfg, **ctx}
    return cfg


def _check_pack(cfg: dict, source) -> None:
    """The pack's shape, checked when it is loaded: known keys only, at the top and in each entry."""
    unknown = set(cfg) - set(PACK_KEYS)
    if unknown:
        raise ValueError(f"pack {source}: unknown keys {sorted(unknown)}; allowed: {list(PACK_KEYS)}")
    for key, allowed in _ENTRY_KEYS.items():
        val = cfg.get(key) or []
        for entry in [val] if isinstance(val, dict) else val:
            extra = set(entry) - set(allowed) if isinstance(entry, dict) else {repr(entry)}
            if extra:
                raise ValueError(f"pack {source}: {key} entry {entry!r} has unknown keys {sorted(extra)}; "
                                 f"allowed: {list(allowed)}")


def _check_context(ctx: dict, path: Path) -> None:
    """The private context's shape, checked when it is loaded: each hypothesis is `{id, text}`.
    A plain-string hypothesis once passed every stage and crashed the private report after a full
    run (2026-10-31), so a malformed context stops before any harvesting."""
    unknown = set(ctx) - set(PRIVATE_KEYS)
    if unknown:
        raise ValueError(f"{path}: unknown keys {sorted(unknown)}; allowed: {list(PRIVATE_KEYS)}")
    for h in ctx.get("hypotheses") or []:
        if not (isinstance(h, dict) and h.get("id") and h.get("text")):
            raise ValueError(f"{path}: a hypothesis needs an id and a text, got {h!r}")


def _breakpoints(cfg: dict) -> list[tuple[str, date]]:
    """The pack's platform breakpoints as (name, date). Both fields are required: a nameless change
    would reach the verify prompt as a made-up label."""
    out = []
    for b in cfg.get("breakpoints") or []:
        if not b.get("name") or not b.get("date"):
            raise ValueError(f"breakpoint needs a name and a date: {b!r}")
        out.append((b["name"], date.fromisoformat(str(b["date"]))))
    return out


def breakpoints(cfg: dict) -> list[date]:
    """Breakpoint dates (scoring halves older platform-mechanic claims)."""
    return [d for _, d in _breakpoints(cfg)]


def verify_args(cfg: dict) -> dict:
    """What the verify stage is handed from a config: report language, the known platform changes
    ("name (date)") and the official domains a doc check may cite."""
    from tubeproof.i18n import lang_of

    return {"lang": lang_of(cfg), "changes": [f"{n} ({d})" for n, d in _breakpoints(cfg)],
            "domains": list(cfg.get("official_domains") or [])}


def has_private(cfg: dict) -> bool:
    return any(cfg.get(k) for k in PRIVATE_KEYS)


def topic_of(cfg: dict, topic: str | None = None) -> str:
    topic = topic or cfg.get("topic")
    if not topic:
        raise ValueError("a topic or a pack with a topic is required")
    return topic


def run_id_of(cfg: dict, run_id: str | None = None, topic: str | None = None) -> str:
    """The research id: the one given, else the pack's `name`, else a dated slug of the topic."""
    return run_id or cfg.get("name") or core.new_run_id(topic_of(cfg, topic))


def harvest(cfg: dict, *, topic: str | None = None, extra_queries: Sequence[str] = (), run_id: str | None = None,
            llm=None, log=print, **opts) -> Path:
    """Harvest (or plan, with plan_only=True) from a config. `opts` pass through to core harvest."""
    topic = topic_of(cfg, topic)
    queries = [Query(**q) for q in cfg.get("queries", [])] + [Query(text=q) for q in extra_queries]
    market = cfg.get("market") or {}
    # Selection defaults live in core harvest (SSOT-14): pass only what the caller or pack sets.
    policy = given(**{**opts, "months": opts.get("months") or cfg.get("months"),
                      "market_share": market.get("min_share")})
    return core.harvest(topic, queries or [Query(text=topic)],
                        playlist_queries=[Query(**q) for q in cfg.get("playlist_queries", [])] or None,
                        run_id=run_id_of(cfg, run_id, topic),
                        llm=llm, question=cfg.get("question"), relevance_notes=cfg.get("relevance_notes"),
                        channels=cfg.get("channels"),
                        market_lang=market.get("lang"),
                        log=log, **policy)


def process(run_id: str, llm, *, pack: str | None = None, topic: str | None = None,
            extra_queries: Sequence[str] = (), downloads: int | None = None, map_workers: int | None = None,
            log=print, **plan_opts) -> Path:
    """The whole research, the one flow the CLI and the MCP server run: plan first when the run has
    no plan yet (review plan.json), then the streaming pipeline (SSOT-15), which resumes where it
    stopped. Planning options (`topic`, `extra_queries`, `plan_opts` for core harvest) shape a new
    plan only; given for a run that already has one, they fail loudly instead of being ignored."""
    from tubeproof.core.pipeline import process as run_process

    if layout.manifest(settings.run_dir(run_id)).exists():
        if extra_queries or given(**plan_opts):
            raise ValueError(f"{run_id} already has a plan: planning options apply to a new plan only "
                             "(`tubeproof harvest --plan` adds a pass to a harvested run)")
    else:
        log("no plan yet → planning first (review plan.json afterwards)")
        harvest(load_config(run_id, pack), topic=topic, extra_queries=extra_queries, run_id=run_id, llm=llm,
                log=log, pack_name=pack, plan_only=True, **plan_opts)
    return run_process(run_id, llm, load_config(run_id, pack), log=log,
                       **given(downloads=downloads, map_workers=map_workers))


def search(query: str, *, playlists: bool = False, **opts) -> list[SearchHit]:
    """A quick search (CLI `search`, MCP `search_videos`). `opts` (months, limit, gl) pass only
    when set; the window and region defaults are the search's own (SSOT-05)."""
    return list(innertube.search(query, kind="playlist" if playlists else "video",
                                 **{"limit": SEARCH_LIMIT, **given(**opts)}))


MODES = ("claims", "exemplar")


def mode_of(cfg: dict) -> str:
    """`claims` (default): collect and score advice. `exemplar`: measure how a channel's own videos
    are built and test the reader's rules (hypotheses) against them."""
    mode = cfg.get("mode") or MODES[0]
    if mode not in MODES:
        raise ValueError(f"mode {mode!r} not supported ({MODES})")
    return mode
