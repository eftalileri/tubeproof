"""Command-line interface. Thin shell over tubeproof.research and tubeproof.core (the MCP server is another one)."""

from __future__ import annotations

import inspect
import json
from typing import Optional

import typer
from rich.console import Console

from tubeproof import research
from tubeproof.config import settings
from tubeproof.core import harvest as core_harvest
from tubeproof.core.harvest import read_manifest
from tubeproof.i18n import lang_of
from tubeproof.research import given
from tubeproof.store.db import Store

app = typer.Typer(help="tubeproof: research real practitioner experience on YouTube, free knowledge only, "
                       "claims cross-checked and confidence-scored.", no_args_is_help=True)
console = Console()


def log(msg: str) -> None:
    # Stage logs contain "[label]" text; rich must not parse it as markup.
    console.print(msg, markup=False, highlight=False)


def _llm(backend: str | None):
    from tubeproof.llm.base import get_backend

    return get_backend(backend)


def _ctx(run_id: str, pack: str | None) -> tuple:
    run_dir = settings.run_dir(run_id)
    return run_dir, read_manifest(run_dir)["topic"], research.load_config(run_id, pack)


# Help texts quote the selection policy's own defaults (SSOT-14); options left unset pass nothing.
_POLICY = {k: p.default for k, p in inspect.signature(core_harvest.harvest).parameters.items()}
_WORKERS = typer.Option(None, help=f"Parallel LLM calls (default {settings.llm_workers})")
_BACKEND = typer.Option(None, help=f"LLM backend (default {settings.llm_backend})")
_PACK = typer.Option(None, help="Topic pack name or path (default: the run's pack, else research/<id>/pack.yaml)")


@app.command()
def search(query: str, playlists: bool = False, months: Optional[float] = None,
           limit: int = research.SEARCH_LIMIT, gl: Optional[str] = None):
    """Run one search (quick check)."""
    for h in research.search(query, playlists=playlists, **given(months=months, limit=limit, gl=gl)):
        extra = f"{h.video_count} videos" if playlists else f"{h.views or 0:>12,} views · {h.published_text}"
        console.print(f"{h.rank_in_query:>3}. [bold]{h.id}[/] · {extra} · {h.channel} · {h.title[:70]}")


@app.command()
def harvest(
    run_id: Optional[str] = typer.Argument(None, help="Research id = folder name in research/ (default: pack name)"),
    topic: Optional[str] = typer.Option(None, help="Topic (default: the pack's topic)"),
    pack: Optional[str] = _PACK,
    query: list[str] = typer.Option([], "--query", "-q", help="Extra search query (repeatable)"),
    months: Optional[float] = typer.Option(None, help=f"Time window in months (default: pack, else {_POLICY['months']:g})"),
    videos: Optional[int] = typer.Option(None, help=f"Number of videos to select (default {_POLICY['n_videos']})"),
    playlists: Optional[int] = typer.Option(None, help=f"Number of course playlists to inspect "
                                                       f"(default {_POLICY['n_playlists']})"),
    links: Optional[bool] = typer.Option(None, "--links/--no-links",
                                         help=f"Read description links (default {_POLICY['fetch_links']})"),
    whisper: Optional[bool] = typer.Option(None, "--whisper/--no-whisper",
                                           help="Transcribe with Whisper when there are no captions "
                                                f"(default {_POLICY['allow_whisper']})"),
    no_screen: bool = typer.Option(False, help="Turn off the LLM relevance gate"),
    plan: bool = typer.Option(False, "--plan", help="Only select and save the list; `process` harvests it"),
):
    """Discover + harvest: find videos, download transcript/comment/link bundles."""
    cfg = research.load_config(run_id, pack)
    run_dir = research.harvest(cfg, topic=topic, extra_queries=query, run_id=run_id,
                               llm=None if no_screen else _llm(None), log=log, pack_name=pack, plan_only=plan,
                               **given(months=months, n_videos=videos, n_playlists=playlists, fetch_links=links,
                                       allow_whisper=whisper))
    console.print(f"[green]✓[/] {run_dir}")


@app.command("repair")
def repair_cmd(run_id: str, whisper: Optional[bool] = typer.Option(
        None, "--whisper/--no-whisper", help="Use Whisper when there are no captions (default: "
        f"{inspect.signature(core_harvest.repair).parameters['allow_whisper'].default})")):
    """Retry videos with missing transcripts (captions first, then Whisper)."""
    res = core_harvest.repair(run_id, log=log, **given(allow_whisper=whisper))
    console.print(f"[green]✓[/] fixed {res['fixed']}, remaining {res['remaining']}")


@app.command()
def process(run_id: str, downloads: Optional[int] = typer.Option(None, help="Parallel audio downloads "
                                                                           "(default: the pipeline's)"),
            workers: Optional[int] = _WORKERS, backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK):
    """Streaming run: harvest the plan + parallel audio + one Whisper + analysis as transcripts land,
    then cluster, verify and write the reports. Resumes where it stopped; plans first when there is no plan."""
    out = research.process(run_id, _llm(backend), pack=pack, downloads=downloads, map_workers=workers, log=log)
    console.print(f"[green]✓[/] {out}")


@app.command()
def analyze(run_id: str, workers: Optional[int] = _WORKERS,
            only: list[str] = typer.Option([], "--only", help="Only these video ids"),
            backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK):
    """Map stage: claim extraction, sales tagging, comment evidence per video."""
    from tubeproof.core.map_stage import run_map

    run_dir, topic, cfg = _ctx(run_id, pack)
    res = run_map(_llm(backend), run_dir, topic, lang_of(cfg), only=only or None, mode=research.mode_of(cfg),
                  log=log, **given(workers=workers))
    console.print(f"[green]✓[/] {res['done']} videos, {len(res['failed'])} failed, ${res['usd']:.3f}")


@app.command()
def reduce(run_id: str, workers: Optional[int] = _WORKERS, backend: Optional[str] = _BACKEND,
           no_llm: bool = typer.Option(False, help="Cluster by embedding threshold only")):
    """Reduce stage: cluster claims."""
    from tubeproof.core.reduce_stage import run_reduce

    run_reduce(settings.run_dir(run_id), None if no_llm else _llm(backend), log=log, **given(workers=workers))


@app.command()
def verify(run_id: str, workers: Optional[int] = _WORKERS, backend: Optional[str] = _BACKEND,
           pack: Optional[str] = _PACK):
    """Verification: member stances and the official-docs check."""
    from tubeproof.core.verify_stage import run_verify

    run_dir, topic, cfg = _ctx(run_id, pack)
    llm = _llm(backend)
    run_verify(llm, run_dir, topic, **research.verify_args(cfg), log=log, **given(workers=workers))
    console.print(f"[green]✓[/] ${llm.meter.usd:.2f}")


@app.command()
def report(run_id: str, backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK,
           render: bool = typer.Option(False, help="Only re-render links and appendix (no model call)")):
    """Score + synthesize: the public REPORT.md, and private/REPORT.md when a private context exists."""
    from tubeproof.core.synth_stage import write_reports

    _run_dir, _topic, cfg = _ctx(run_id, pack)
    for out in write_reports(None if render else _llm(backend), run_id, cfg, log=log, render_only=render):
        console.print(f"[green]✓[/] {out}")


@app.command()
def runs():
    """List stored runs."""
    for r in Store().list_runs():
        console.print(f"{r['id']} · {r['stage']} · {r['topic']}")


@app.command()
def stats(run_id: str):
    """Harvest statistics of a run."""
    console.print_json(json.dumps(core_harvest.run_stats(settings.run_dir(run_id)), ensure_ascii=False))


if __name__ == "__main__":
    app()
