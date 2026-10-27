"""Cross-layer authorities (each value has one owner that every layer reads). All offline."""

import inspect
import json
import time
import types
from dataclasses import replace
from pathlib import Path

import pytest

from tubeproof import http, research
from tubeproof.config import layout, settings
from tubeproof.core import exemplar, map_stage, pipeline, reduce_stage, synth_stage, verify_stage
from tubeproof.core.discover import UNKNOWN_AGE_DAYS, Query, rank_score
from tubeproof.models import Transcript, TranscriptSegment
from tubeproof.prompts import load
from tubeproof.sources.youtube import innertube, metadata
from tubeproof.store import db
from tubeproof.store.db import Store


# 1 · cache TTL per kind: get and purge read the same rule
def test_store_ttl_per_kind(tmp_path, monkeypatch):
    monkeypatch.setattr(db, "settings", types.SimpleNamespace(cache_ttl_days=30))
    s = Store(tmp_path / "c.sqlite")
    s.put("meta", "v", 1)
    s.put("rel:abc123", "v", 3)
    s._conn.execute("UPDATE cache SET fetched_at=?", (time.time() - 40 * 86400,))
    s._conn.commit()
    assert db.ttl_days("rel:abc123") == db.KIND_TTL_DAYS["rel:"] and db.ttl_days("meta") == 30
    assert s.get("meta", "v") is None and s.get("rel:abc123", "v") == 3
    assert s.purge_expired() == 1  # only the meta row
    assert Store(tmp_path / "c.sqlite").get("rel:abc123", "v") == 3  # a new Store (purge on open) keeps it
    assert "max_age_days" not in inspect.signature(Store.get).parameters  # no caller-side TTL


# 2 · YouTube URLs are built in http
def test_thumbnail_url_is_the_one_used(tmp_path, monkeypatch):
    urls = []

    def fake_request(c, method, url, **kw):
        urls.append(url)
        return types.SimpleNamespace(status_code=404, content=b"")

    monkeypatch.setattr(http, "request", fake_request)
    assert exemplar.thumbnail("vid", tmp_path) is None
    assert urls == [http.thumbnail_url("vid", "maxresdefault"), http.thumbnail_url("vid", "hqdefault")]
    assert http.thumbnail_url("vid", "hqdefault") == "https://i.ytimg.com/vi/vid/hqdefault.jpg"


# 3 · a channel's uploads playlist is derived in metadata
def test_uploads_playlist():
    assert metadata.uploads_playlist("UCabc") == "UULFabc"
    with pytest.raises(ValueError, match="must start with UC"):
        metadata.uploads_playlist("@handle")
    assert metadata.is_channel_id("UCx") and not metadata.is_channel_id("VLx")


# 4 · the search has no dead language parameter; Query reads the search's region default
def test_search_language_and_region(monkeypatch):
    assert "hl" not in inspect.signature(innertube.search).parameters
    assert inspect.signature(innertube.search).parameters["gl"].default == innertube.DEFAULT_GL
    assert Query("q").gl == innertube.DEFAULT_GL
    bodies = []

    def fake_request(c, method, url, json=None, **kw):
        bodies.append(json)
        return types.SimpleNamespace(raise_for_status=lambda: None, json=lambda: {})

    monkeypatch.setattr(http, "request", fake_request)
    list(innertube.search("q", gl="TR"))
    assert bodies[0]["context"]["client"]["hl"] == innertube.UI_HL and bodies[0]["context"]["client"]["gl"] == "TR"


# 5 · unknown age is explicit; a video from today is one day old, not a year
def test_rank_score_age():
    assert rank_score(10_000, None) == rank_score(10_000, UNKNOWN_AGE_DAYS)
    assert rank_score(10_000, 0) == rank_score(10_000, 1) > rank_score(10_000, UNKNOWN_AGE_DAYS)


# 6 · per-video record names and listings come from Layout
def test_layout_records(tmp_path):
    for vid in ("b", "a"):
        for path in (layout.bundle(tmp_path, vid), layout.extraction(tmp_path, vid), layout.exemplar_file(tmp_path, vid)):
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("{}")
    assert layout.bundles(tmp_path) == [layout.bundle(tmp_path, "a"), layout.bundle(tmp_path, "b")]
    assert [p.stem for p in layout.extraction_files(tmp_path)] == ["a", "b"]
    assert [p.stem for p in layout.exemplar_files(tmp_path)] == ["a", "b"]
    assert layout.exemplar_assets(tmp_path, "a").parent == layout.exemplar(tmp_path)
    assert layout.bundles(tmp_path / "missing") == []


# 7 · one default for parallel LLM calls
def test_llm_workers_default():
    for fn, name in ((pipeline.process, "map_workers"), (map_stage.run_map, "workers"),
                     (reduce_stage.run_reduce, "workers"), (reduce_stage.cluster, "workers"),
                     (reduce_stage.merge_pass, "workers"), (verify_stage.run_verify, "workers")):
        assert inspect.signature(fn).parameters[name].default == settings.llm_workers, fn.__name__


def _exemplar_run(tmp_path, monkeypatch):
    s = replace(settings, research_dir=tmp_path / "research", data_dir=tmp_path / "cache")
    monkeypatch.setattr(synth_stage, "settings", s)
    run_dir = s.run_dir("r")
    run_dir.mkdir(parents=True)
    layout.manifest(run_dir).write_text(json.dumps({"topic": "t", "videos": [
        {"id": "aaa", "title": "A", "channel": "C", "views": 5}]}))
    layout.exemplar_file(run_dir, "aaa").parent.mkdir(parents=True)
    layout.exemplar_file(run_dir, "aaa").write_text(json.dumps(
        {"video_id": "aaa", **dict.fromkeys(exemplar.PICTURE_METRICS, 1)}))
    layout.extraction(run_dir, "aaa").parent.mkdir(parents=True)
    layout.extraction(run_dir, "aaa").write_text(json.dumps({"speech": dict.fromkeys(exemplar.SPEECH_METRICS, 2)}))
    return s


# 8 · render-only is a mode of write_reports: existing bodies only, no model
def test_write_reports_render_only(tmp_path, monkeypatch):
    s = _exemplar_run(tmp_path, monkeypatch)
    cfg = {"mode": "exemplar", "question": "q"}  # has a private context, but only the public body exists
    with pytest.raises(FileNotFoundError, match="no saved report body"):
        synth_stage.write_reports(None, "r", cfg, render_only=True)
    (s.research_path("r") / synth_stage.BODY_FILE).write_text("See [V1 5s].")
    outs = synth_stage.write_reports(None, "r", cfg, render_only=True)
    assert outs == [s.research_path("r") / synth_stage.REPORT_FILE]
    assert "[V1 0:05](https://youtu.be/aaa?t=5)" in outs[0].read_text()


# 9 · each frame keeps the time it was taken at, also when one is missing
def test_frames_keep_their_times(tmp_path, monkeypatch):
    def fake_run(cmd, **kw):
        if cmd[cmd.index("-ss") + 1] != "2":  # the frame at 2 s fails to extract
            Path(cmd[-1]).write_bytes(b"jpg")

    monkeypatch.setattr(exemplar.subprocess, "run", fake_run)
    monkeypatch.setattr(exemplar, "cuts", lambda video: ([], []))
    monkeypatch.setattr(exemplar, "thumbnail", lambda vid, out: None)
    monkeypatch.setattr(exemplar, "frame_times", lambda dur: [1, 2, 3])
    m = exemplar.measure("vid", tmp_path / "v.mp4", 120, tmp_path)
    assert m["frame_times"] == [1, 3] and [Path(p).name for p in m["frames"]] == ["f0001.jpg", "f0003.jpg"]


# 10 · the report's speech columns are speech() keys owned by exemplar
def test_speech_metrics_are_speech_keys():
    tr = Transcript(video_id="v", language="en", source="yt_dlp",
                    segments=[TranscriptSegment(start=0.5, duration=2, text="one two three.")])
    assert set(exemplar.SPEECH_METRICS) <= set(exemplar.speech(tr))


# 11 · verify is handed its config values by research
def test_verify_args():
    cfg = {"breakpoints": [{"name": "Engine", "date": "2024-12-02"}], "official_domains": ["a.com"], "report_lang": "tr"}
    assert research.verify_args(cfg) == {"lang": "tr", "changes": ["Engine (2024-12-02)"], "domains": ["a.com"]}
    assert research.verify_args({}) == {"lang": research.verify_args({})["lang"], "changes": [], "domains": []}
    with pytest.raises(ValueError, match="name and a date"):
        research.verify_args({"breakpoints": [{"date": "2024-12-02"}]})
    assert "cfg" not in inspect.signature(verify_stage.run_verify).parameters


# 12 · a missing measurement stops the exemplar report (see also test_offline)
def test_exemplar_digest_fails_on_missing_speech(tmp_path, monkeypatch):
    s = _exemplar_run(tmp_path, monkeypatch)
    layout.extraction(s.run_dir("r"), "aaa").write_text(json.dumps({"speech": None}))
    with pytest.raises(RuntimeError, match="no speech metrics"):
        synth_stage.render_exemplar("r", False, [{"id": "aaa", "title": "A"}], "en")


# 14 · the cluster id prefix has one owner: ids, citation links and the prompt
def test_cluster_prefix(tmp_path, monkeypatch):
    raw = (Path(synth_stage.__file__).parents[1] / "prompts" / "synthesize.md").read_text()
    assert "[K" not in raw and "{cluster_prefix}" in raw
    p = load("synthesize.md", "en", topic="t", question="q", audience="a", n_videos=1, n_channels=1, today="d",
             reader_block="", hypotheses_section="", fit_column="f", levers_rule="l", test_ref="TEST",
             cluster_prefix=reduce_stage.CLUSTER_PREFIX)
    assert f"[{reduce_stage.CLUSTER_PREFIX}<number>]" in p
    monkeypatch.setattr(synth_stage, "report_dir", lambda run_id, private: tmp_path)
    (tmp_path / synth_stage.BODY_FILE).write_text(f"x [{reduce_stage.CLUSTER_PREFIX}3]")
    out = synth_stage.render_report("r", False, [], {}, "en").read_text()
    assert f"[{reduce_stage.CLUSTER_PREFIX}3](#{reduce_stage.CLUSTER_PREFIX.lower()}3)" in out
