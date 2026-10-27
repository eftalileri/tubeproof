"""MCP server: a thin shell over tubeproof.core, same as the CLI.

A full research takes tens of minutes, longer than an MCP call should block, so
`research_topic` starts a background job and returns its run id; the client then
polls `research_status` and reads `get_report`.
"""

from __future__ import annotations

import json
import threading
import traceback

from mcp.server.mcpserver import MCPServer

from tubeproof.config import settings
from tubeproof import research
from tubeproof.sources.youtube import innertube

mcp = MCPServer("tubeproof")
_jobs: dict[str, dict] = {}
_lock = threading.Lock()


def _job_log(key: str):
    def log(msg: str) -> None:
        with _lock:
            _jobs[key]["log"] = (_jobs[key]["log"] + [str(msg)])[-40:]
    return log


def _research(key: str, topic: str, run_id: str | None, pack: str | None, queries: list[str], months: float,
              videos: int, playlists: int) -> None:
    from tubeproof.core.pipeline import process
    from tubeproof.llm.base import get_backend

    log = _job_log(key)
    try:
        cfg = research.load_config(run_id, pack)
        llm = get_backend()
        run_dir = research.harvest(cfg, topic=topic, extra_queries=queries, run_id=run_id, months=months,
                                   llm=llm, log=log, n_videos=videos, n_playlists=playlists, pack_name=pack,
                                   plan_only=True)
        rid = run_dir.parent.name
        with _lock:
            _jobs[key]["run_id"] = rid
        process(rid, llm, research.load_config(rid, pack), log=log)
        with _lock:
            _jobs[key].update(state="done", usd=round(llm.meter.usd, 3))
    except Exception as e:
        with _lock:
            _jobs[key].update(state="failed", error=f"{type(e).__name__}: {e}",
                              trace=traceback.format_exc()[-1500:])


@mcp.tool()
def research_topic(topic: str, run_id: str | None = None, pack: str | None = None,
                   queries: list[str] | None = None, months: float = 12, videos: int = 30,
                   playlists: int = 5) -> dict:
    """Start a full YouTube practitioner-knowledge research in the background.

    Searches popular videos and course playlists (any language) in the last `months`,
    harvests transcripts, comments and description links, strips paid/sales parts,
    cross-checks claims and writes a confidence-scored report in the pack's report_lang.
    `run_id` names the research folder (research/<run_id>/, its pack.yaml is used when present).
    Give extra search `queries` in several languages for better coverage, or a topic
    `pack` such as "meta-ads". Returns a job id; poll research_status.
    """
    key = f"job-{len(_jobs) + 1}"
    with _lock:
        _jobs[key] = {"state": "running", "topic": topic, "log": [], "run_id": None}
    threading.Thread(target=_research, args=(key, topic, run_id, pack, queries or [], months, videos, playlists),
                     daemon=True).start()
    return {"job_id": key, "state": "running"}


@mcp.tool()
def research_status(job_id: str) -> dict:
    """Progress of a research job: state, run_id, cost and the last log lines."""
    with _lock:
        job = dict(_jobs.get(job_id) or {"state": "unknown"})
    job["log"] = job.get("log", [])[-12:]
    return job


@mcp.tool()
def get_report(run_id: str) -> str:
    """The finished public Markdown report (research/<run_id>/REPORT.md)."""
    path = settings.research_path(run_id) / "REPORT.md"
    return path.read_text() if path.exists() else f"No report yet for {run_id}."


@mcp.tool()
def list_runs() -> list[dict]:
    """Runs stored locally (id, topic, stage)."""
    from tubeproof.store.db import Store

    return Store().list_runs()


@mcp.tool()
def search_videos(query: str, months: float = 12, limit: int = 15, playlists: bool = False,
                  region: str = "US") -> list[dict]:
    """Quick YouTube search sorted by popularity within the time window (no API key)."""
    kind = "playlist" if playlists else "video"
    return [h.model_dump() for h in innertube.search(query, kind=kind, months=months, limit=limit, gl=region)]


@mcp.tool()
def query_claims(run_id: str, text: str = "", band: str | None = None, limit: int = 20) -> list[dict]:
    """Search the scored claim clusters of a run by keyword and/or band
    (well_supported, likely, contested, doubtful, single_source, unverifiable)."""
    path = settings.run_dir(run_id) / "scored.json"
    if not path.exists():
        return []
    words = [w for w in text.casefold().split() if w]
    out = []
    for c in json.loads(path.read_text()):
        if band and c["score"]["band"] != band:
            continue
        hay = (c["claim_local"] + " " + " ".join(m["quote"] for m in c["members"])).casefold()
        if all(w in hay for w in words):
            out.append({k: c[k] for k in ("cluster_id", "claim_local", "claim_type", "label", "scope_local",
                                          "reasoning_local", "score")}
                       | {"sources": [f"https://youtu.be/{m['video_id']}?t={int(m['t'] or 0)}"
                                      for m in c["members"]][:5]})
    out.sort(key=lambda c: -c["score"]["confidence"])
    return out[:limit]


def main() -> None:
    mcp.run()


if __name__ == "__main__":
    main()
