"""Orchestration has one authority: plan + harvest in core harvest, the full flow in research.process,
quick search in research.search; the CLI and the MCP server only pass what is set. All offline."""

import json

import pytest

from tubeproof.config import Settings, layout
from tubeproof.models import PlaylistMeta, VideoMeta


class FakeStore:
    def __init__(self):
        self.cache, self.runs = {}, []

    def get(self, kind, key, max_age_days=None):
        return self.cache.get((kind, key))

    def put(self, kind, key, value):
        self.cache[(kind, key)] = value

    def upsert_run(self, run_id, topic, params, stage):
        self.runs.append((run_id, stage))


@pytest.fixture
def offline(tmp_path, monkeypatch):
    """core harvest against a temp research dir, a fake store and fake YouTube calls."""
    from tubeproof import research
    from tubeproof.core import harvest as core

    s = Settings(data_dir=tmp_path / "cache", research_dir=tmp_path / "research")
    for mod in (core, research):
        monkeypatch.setattr(mod, "settings", s)
    store = FakeStore()
    monkeypatch.setattr(core, "Store", lambda: store)
    uploads = {"ids": ["a"]}
    monkeypatch.setattr(core.yt_meta, "playlist_meta", lambda pid, max_items=None: PlaylistMeta(
        id=pid, title="uploads", channel="Ch", video_ids=list(uploads["ids"])))
    monkeypatch.setattr(core.yt_meta, "video_meta", lambda vid: VideoMeta(
        id=vid, title=f"T{vid}", channel="Ch", channel_id="UCx", duration_s=600))

    def no_captions(*a, **kw):
        raise RuntimeError("no captions")

    monkeypatch.setattr(core.yt_transcript, "fetch_transcript", no_captions)
    return s, store, uploads


def _harvest(**kw):
    from tubeproof.core import harvest as core

    return core.harvest("topic", [], run_id="r1", channels=[{"id": "UCx", "latest": 5}], log=lambda m: None,
                        **core.EXEMPLAR_BUNDLE, **kw)


def test_plan_then_harvest_is_one_path(offline):
    s, store, _ = offline
    run_dir = _harvest(plan_only=True)
    plan = json.loads(layout.manifest(run_dir).read_text())
    assert plan["planned"] and [v["id"] for v in plan["videos"]] == ["a"]
    assert not layout.bundle(run_dir, "a").exists()
    with pytest.raises(ValueError, match="already has a plan"):  # --plan twice must not harvest
        _harvest(plan_only=True)
    _harvest()
    done = json.loads(layout.manifest(run_dir).read_text())
    assert done["planned"] is False and layout.bundle(run_dir, "a").exists()
    # The run index is keyed by the run id (it once recorded "data", the folder name).
    assert {rid for rid, _ in store.runs} == {"r1"} and store.runs[-1] == ("r1", "harvested")


def test_direct_harvest_writes_the_same_manifest_as_a_plan(offline):
    run_dir = _harvest()
    m = json.loads(layout.manifest(run_dir).read_text())
    assert m["planned"] is False and "harvested" in m and layout.bundle(run_dir, "a").exists()


def test_new_pass_keeps_earlier_videos(offline):
    """Re-planning a harvested run once overwrote its manifest with the new pass only."""
    _, _, uploads = offline
    run_dir = _harvest()
    uploads["ids"] = ["b"]
    _harvest(plan_only=True)
    m = json.loads(layout.manifest(run_dir).read_text())
    assert [v["id"] for v in m["videos"]] == ["a", "b"] and m["planned"] and len(m["params"]["passes"]) == 2


def test_set_transcript_writes_bundle_and_cache(offline):
    from tubeproof.core import harvest as core
    from tubeproof.models import Transcript, VideoBundle

    _, store, _ = offline
    run_dir = _harvest()
    b = VideoBundle.model_validate_json(layout.bundle(run_dir, "a").read_text())
    assert b.transcript_error
    core.set_transcript(run_dir, b, Transcript(video_id="a", source="whisper", segments=[]), store)
    again = VideoBundle.model_validate_json(layout.bundle(run_dir, "a").read_text())
    assert again.transcript and again.transcript_error is None and ("transcript", "a") in store.cache


def test_load_config_falls_back_to_the_runs_pack(offline):
    from tubeproof import research
    from tubeproof.core import harvest as core

    s, _, _ = offline
    run_dir = s.run_dir("r2")
    run_dir.mkdir(parents=True)
    core.write_manifest(run_dir, {"run_id": "r2", "topic": "t", "params": {"pack": "meta-ads"}, "videos": []})
    assert research.load_config("r2")["name"] == "meta-ads"  # the CLI and the MCP server now agree


def test_process_plans_once_then_resumes(offline, monkeypatch):
    from tubeproof import research
    from tubeproof.core import pipeline

    calls = []
    monkeypatch.setattr(research, "harvest", lambda cfg, **kw: calls.append(("plan", kw)))
    monkeypatch.setattr(pipeline, "process", lambda rid, llm, cfg, log, **kw: calls.append(("process", kw)) or "out")
    assert research.process("r3", None, topic="t", log=lambda m: None) == "out"
    assert calls[0][0] == "plan" and calls[0][1]["plan_only"] and calls[1] == ("process", {})
    s, _, _ = offline
    layout.manifest(s.run_dir("r3")).parent.mkdir(parents=True)
    layout.manifest(s.run_dir("r3")).write_text(json.dumps({"params": {"pack": None}}))
    with pytest.raises(ValueError, match="already has a plan"):  # options a resume would ignore fail loudly
        research.process("r3", None, n_videos=10)
    calls.clear()
    research.process("r3", None, map_workers=2)
    assert calls == [("process", {"map_workers": 2})]


def test_cli_and_mcp_search_share_defaults(monkeypatch):
    from typer.testing import CliRunner

    from tubeproof import cli, mcp_server, research

    seen = []
    monkeypatch.setattr(research.innertube, "search", lambda q, **kw: seen.append(kw) or iter(()))
    assert CliRunner().invoke(cli.app, ["search", "q"]).exit_code == 0
    mcp_server.search_videos("q")
    assert seen[0] == seen[1] == {"kind": "video", "limit": research.SEARCH_LIMIT}


def test_coverage_unknown_is_not_full():
    from tubeproof.core.pipeline import coverage
    from tubeproof.models import Transcript

    assert coverage(Transcript(video_id="a", source="whisper", segments=[]), None) is None


def test_query_claims_fails_loudly(tmp_path, monkeypatch):
    from tubeproof import mcp_server

    monkeypatch.setattr(mcp_server, "settings", Settings(research_dir=tmp_path))
    with pytest.raises(FileNotFoundError):
        mcp_server.query_claims("missing")
    with pytest.raises(ValueError, match="unknown band"):
        mcp_server.query_claims("missing", band="great")
