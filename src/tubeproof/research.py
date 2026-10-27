"""One research = one folder `research/<id>/` (layout in `config.py`).

This module is the single place that turns a research's configuration into stage calls, so the
CLI and the MCP server stay thin and cannot drift apart.

- `pack.yaml`             public topic pack: topic, queries, official domains, breakpoints, report_lang
- `private/context.yaml`  the reader's question, context and hypotheses (never committed)
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

import yaml

from tubeproof.config import settings
from tubeproof.core.discover import Query
from tubeproof.packs import load_pack

PRIVATE_KEYS = ("question", "context", "hypotheses")


def load_config(run_id: str | None = None, pack: str | None = None) -> dict:
    """`pack` (a name in packs/ or a path) wins; otherwise the research folder's own pack.
    The private context is merged in when it exists."""
    cfg: dict = {}
    if pack:
        cfg = load_pack(pack)
    elif run_id and (settings.research_path(run_id) / "pack.yaml").exists():
        cfg = yaml.safe_load((settings.research_path(run_id) / "pack.yaml").read_text())
    if run_id:
        priv = settings.research_path(run_id) / "private" / "context.yaml"
        if priv.exists():
            cfg = {**cfg, **(yaml.safe_load(priv.read_text()) or {})}
    return cfg


def breakpoints(cfg: dict) -> list[date]:
    return [date.fromisoformat(str(b["date"])) for b in cfg.get("breakpoints", [])]


def has_private(cfg: dict) -> bool:
    return any(cfg.get(k) for k in PRIVATE_KEYS)


def harvest(cfg: dict, *, topic: str | None = None, extra_queries: list[str] = (), run_id: str | None = None,
            llm=None, log=print, **opts) -> Path:
    """Harvest (or plan, with plan_only=True) from a config. `opts` pass through to core harvest."""
    from tubeproof.core.harvest import harvest as core_harvest

    topic = topic or cfg.get("topic")
    if not topic:
        raise ValueError("a topic or a pack with a topic is required")
    queries = [Query(**q) for q in cfg.get("queries", [])] + [Query(text=q) for q in extra_queries]
    market = cfg.get("market") or {}
    return core_harvest(topic, queries or [Query(text=topic)],
                        playlist_queries=[Query(**q) for q in cfg.get("playlist_queries", [])] or None,
                        months=opts.pop("months", None) or cfg.get("months", 12), run_id=run_id or cfg.get("name"),
                        llm=llm, question=cfg.get("question"), market_lang=market.get("lang"),
                        market_share=market.get("min_share", 0.25), log=log, **opts)
