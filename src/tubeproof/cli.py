"""Command-line interface. Thin shell over tubeproof.research and tubeproof.core (the MCP server is another one)."""

from __future__ import annotations

import json
from typing import Optional

import typer
from rich.console import Console

from tubeproof import research
from tubeproof.config import layout, settings
from tubeproof.core.harvest import read_manifest, video_titles
from tubeproof.i18n import lang_of
from tubeproof.sources.youtube import innertube
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
    manifest = read_manifest(run_dir)
    cfg = research.load_config(run_id, pack or manifest["params"].get("pack"))
    return run_dir, manifest["topic"], cfg


_WORKERS = typer.Option(4, help="Parallel LLM calls")
_BACKEND = typer.Option(None, help="LLM backend (default claude_cli)")
_PACK = typer.Option(None, help="Topic pack name or path (default: research/<id>/pack.yaml)")


@app.command()
def search(query: str, playlists: bool = False, months: float = 12, limit: int = 15,
           hl: str = "en", gl: str = "US"):
    """Run one search (quick check)."""
    kind = "playlist" if playlists else "video"
    for h in innertube.search(query, kind=kind, months=months, limit=limit, hl=hl, gl=gl):
        extra = f"{h.video_count} videos" if kind == "playlist" else f"{h.views or 0:>12,} views · {h.published_text}"
        console.print(f"{h.rank_in_query:>3}. [bold]{h.id}[/] · {extra} · {h.channel} · {h.title[:70]}")


@app.command()
def harvest(
    run_id: Optional[str] = typer.Argument(None, help="Research id = folder name in research/ (default: pack name)"),
    topic: Optional[str] = typer.Option(None, help="Topic (default: the pack's topic)"),
    pack: Optional[str] = _PACK,
    query: list[str] = typer.Option([], "--query", "-q", help="Extra search query (repeatable)"),
    months: Optional[float] = typer.Option(None, help="Time window in months (default: pack, else 12)"),
    videos: Optional[int] = typer.Option(None, help="Number of videos to select (default 30)"),
    playlists: Optional[int] = typer.Option(None, help="Number of course playlists to inspect (default 5)"),
    no_links: bool = typer.Option(False, help="Do not read description links"),
    whisper: bool = typer.Option(False, help="Transcribe with Whisper when there are no captions"),
    no_screen: bool = typer.Option(False, help="Turn off the LLM relevance gate"),
    plan: bool = typer.Option(False, "--plan", help="Only select and save the list; `process` harvests it"),
):
    """Discover + harvest: find videos, download transcript/comment/link bundles."""
    cfg = research.load_config(run_id, pack)
    run_dir = research.harvest(cfg, topic=topic, extra_queries=query, run_id=run_id, months=months,
                               llm=None if no_screen else _llm(None), log=log, n_videos=videos,
                               n_playlists=playlists, fetch_links=not no_links, allow_whisper=whisper,
                               pack_name=pack, plan_only=plan)
    console.print(f"[green]✓[/] {run_dir}")


@app.command("repair")
def repair_cmd(run_id: str, whisper: bool = typer.Option(True, help="Use Whisper when there are no captions")):
    """Retry videos with missing transcripts (captions first, then Whisper)."""
    from tubeproof.core.harvest import repair

    res = repair(run_id, allow_whisper=whisper, log=log)
    console.print(f"[green]✓[/] fixed {res['fixed']}, remaining {res['remaining']}")


@app.command()
def process(run_id: str, downloads: int = typer.Option(6, help="Parallel audio downloads"),
            workers: int = _WORKERS, backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK):
    """Streaming run: harvest the plan + parallel audio + one Whisper + analysis as transcripts land,
    then cluster, verify and write the reports. Resumes where it stopped; plans first when there is no plan."""
    from tubeproof.core.pipeline import process as run_process

    if not layout.manifest(settings.run_dir(run_id)).exists():
        log("no plan yet → planning first (review plan.json afterwards)")
        research.harvest(research.load_config(run_id, pack), run_id=run_id, llm=_llm(backend), log=log,
                         pack_name=pack, plan_only=True)
    _run_dir, _topic, cfg = _ctx(run_id, pack)
    out = run_process(run_id, _llm(backend), cfg, downloads=downloads, map_workers=workers, log=log)
    console.print(f"[green]✓[/] {out}")


@app.command()
def analyze(run_id: str, workers: int = _WORKERS,
            only: list[str] = typer.Option([], "--only", help="Only these video ids"),
            backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK):
    """Map stage: claim extraction, sales tagging, comment evidence per video."""
    from tubeproof.core.map_stage import run_map

    run_dir, topic, cfg = _ctx(run_id, pack)
    res = run_map(_llm(backend), run_dir, topic, lang_of(cfg), workers=workers, only=only or None,
                  mode=research.mode_of(cfg), log=log)
    console.print(f"[green]✓[/] {res['done']} videos, {len(res['failed'])} failed, ${res['usd']:.3f}")


@app.command()
def reduce(run_id: str, workers: int = _WORKERS, backend: Optional[str] = _BACKEND,
           no_llm: bool = typer.Option(False, help="Cluster by embedding threshold only")):
    """Reduce stage: cluster claims."""
    from tubeproof.core.reduce_stage import run_reduce

    run_reduce(settings.run_dir(run_id), None if no_llm else _llm(backend), workers, log=log)


@app.command()
def verify(run_id: str, workers: int = _WORKERS, backend: Optional[str] = _BACKEND,
           pack: Optional[str] = _PACK):
    """Verification: member stances and the official-docs check."""
    from tubeproof.core.verify_stage import run_verify

    run_dir, topic, cfg = _ctx(run_id, pack)
    llm = _llm(backend)
    run_verify(llm, run_dir, topic, cfg, workers=workers, log=log)
    console.print(f"[green]✓[/] ${llm.meter.usd:.2f}")


@app.command()
def report(run_id: str, backend: Optional[str] = _BACKEND, pack: Optional[str] = _PACK,
           render: bool = typer.Option(False, help="Only re-render links and appendix (no model call)")):
    """Score + synthesize: the public REPORT.md, and private/REPORT.md when a private context exists."""
    from tubeproof.core.synth_stage import build_scored, render_report, report_dir, BODY_FILE, write_reports

    run_dir, _topic, cfg = _ctx(run_id, pack)
    if not render:
        for out in write_reports(_llm(backend), run_id, cfg, log=log):
            console.print(f"[green]✓[/] {out}")
        return
    if research.mode_of(cfg) == "exemplar":
        from tubeproof.core.synth_stage import render_exemplar

        vids = read_manifest(run_dir)["videos"]
        for private in (False, True):
            if (report_dir(run_id, private) / BODY_FILE).exists():
                console.print(f"[green]✓[/] {render_exemplar(run_id, private, vids, lang_of(cfg))}")
        return
    scored = build_scored(run_dir, research.breakpoints(cfg))
    titles = video_titles(read_manifest(run_dir))
    for private in (False, True):
        if (report_dir(run_id, private) / BODY_FILE).exists():
            console.print(f"[green]✓[/] {render_report(run_id, private, scored, titles, lang_of(cfg))}")


@app.command()
def runs():
    """List stored runs."""
    for r in Store().list_runs():
        console.print(f"{r['id']} · {r['stage']} · {r['topic']}")


@app.command()
def stats(run_id: str):
    """Harvest statistics of a run."""
    run_dir = settings.run_dir(run_id)
    files = sorted(layout.videos(run_dir).glob("*.json"))
    tot = dict(videos=len(files), transcripts=0, words=0, comments=0, spam=0, links=0, paid_links=0,
               fetched_pages=0, paid_promo=0, langs={})
    for f in files:
        b = json.loads(f.read_text())
        if b.get("transcript"):
            tot["transcripts"] += 1
            tot["words"] += sum(len(s["text"].split()) for s in b["transcript"]["segments"])
            lang = b["transcript"].get("language") or "?"
            tot["langs"][lang] = tot["langs"].get(lang, 0) + 1
        tot["comments"] += len(b["comments"])
        tot["spam"] += sum(1 for c in b["comments"] if c["spam_reasons"])
        tot["links"] += len(b["links"])
        tot["paid_links"] += sum(1 for l in b["links"] if l["is_paid"])
        tot["fetched_pages"] += sum(1 for l in b["links"] if l["fetched"])
        tot["paid_promo"] += 1 if b["meta"].get("has_paid_promotion") else 0
    console.print_json(json.dumps(tot, ensure_ascii=False))


if __name__ == "__main__":
    app()
