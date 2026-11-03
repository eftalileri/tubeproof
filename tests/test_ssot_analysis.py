"""SSOT bindings of the analysis and report layer: every copy reads its one authority."""

import json
from dataclasses import asdict
from datetime import date, timedelta
from typing import get_args

import pytest

from tubeproof import research
from tubeproof.core import synth_stage, verify_stage
from tubeproof.core.extraction import (BEATS, NO_COI, QUOTE_WORDS, STYLE_EXAMPLES, Basis, Claim, ClaimType, Coi,
                                       ExemplarExtraction)
from tubeproof.core.reduce_stage import Cluster, Member
from tubeproof.core.score import (BANDS, BASIS_FACTOR, BREAKPOINT_TYPES, COI_EXEMPT_TYPES, FIRST_HAND,
                                  HALF_LIFE_MONTHS, SHOWN_EVIDENCE, UNKNOWN_AGE_MONTHS, score_cluster)
from tubeproof.i18n import LABELS, lang_rule
from tubeproof.llm.base import CostMeter
from tubeproof.prompts import load


def mk(ref, channel, basis="own_experience", ctype="tactic_efficacy", t=12.0, coi=()):
    d = (date.today() - timedelta(days=60)).isoformat()
    return Member(ref=ref, video_id=ref.split(":")[0], channel_id=channel, channel=channel, upload_date=d,
                  text_en="x", text_local="x", quote="q", t_start=t, claim_type=ctype, polarity="do",
                  specificity=2, evidence_shown="verbal_numbers", conditions={}, is_withheld_teaser=False,
                  survivorship_flags=[], coi=list(coi), clickbait=0.2, basis=basis)


class FakeLLM:
    def __init__(self, answers):
        self.answers, self.calls, self.meter = list(answers), [], CostMeter()

    def json(self, tier, system, user, schema, tools=None, images=None):
        self.calls.append({"system": system, "user": user, "tools": tools})
        return self.answers.pop(0)


def test_labels_cover_every_value_their_authority_defines():
    stances = set(get_args(verify_stage.MemberStance.model_fields["stance"].annotation)) - {"unrelated"}
    for lang, L in LABELS.items():
        assert set(L["band"]) == set(BANDS), lang
        assert set(L["basis"]) == set(get_args(Basis)), lang
        assert set(L["coi_kind"]) == set(get_args(Coi)) - {NO_COI}, lang
        assert set(L["stance"]) == stances, lang


def test_rubric_constants_name_known_values():
    assert set(BASIS_FACTOR) == set(get_args(Basis)) and set(FIRST_HAND) <= set(get_args(Basis))
    types = set(get_args(ClaimType))
    for s in (COI_EXEMPT_TYPES, BREAKPOINT_TYPES, verify_stage.MECHANIC_TYPES, verify_stage.DOC_CHECK_TYPES):
        assert set(s) <= types
    assert set(SHOWN_EVIDENCE) <= set(get_args(Claim.model_fields["evidence_shown"].annotation))
    assert UNKNOWN_AGE_MONTHS == HALF_LIFE_MONTHS


def test_unknown_basis_fails_loudly():
    c = Cluster("K1", [mk("a:C1", "a", basis="hearsay")])
    with pytest.raises(KeyError):
        score_cluster(c, None, [])


def test_prompt_numbers_come_from_the_schema_constants():
    p = load("map_exemplar.md", "en", topic="t", frame_times="0s", beats=BEATS, quote_words=QUOTE_WORDS,
             examples=STYLE_EXAMPLES)
    assert f"{BEATS} beats" in p and f"({QUOTE_WORDS} words" in p and f"{STYLE_EXAMPLES} verbatim" in p
    schema = json.dumps(ExemplarExtraction.model_json_schema())
    assert f"{BEATS} beats" in schema and f"{QUOTE_WORDS} words" in schema and f"{STYLE_EXAMPLES} VERBATIM" in schema


def test_first_hand_in_verify_prompt_and_schema_reads_the_rubric():
    p = load("verify_cluster.md", "en", topic="t", changes="", domains="", doc_rule="", first_hand=", ".join(FIRST_HAND))
    assert f"first-hand members ({', '.join(FIRST_HAND)})" in p
    desc = verify_stage.ClusterVerdict.model_json_schema()["properties"]["practice_vs_docs"]["description"]
    assert f"(basis {'/'.join(FIRST_HAND)})" in desc


def test_prompt_without_report_language_gets_no_language_rule():
    assert lang_rule("tr")
    p = load("group_claims.md", None)
    assert p.startswith("You group claims") and lang_rule("tr") not in p


def test_beat_at_second_zero_is_recorded_by_its_second():
    from tubeproof.core.extraction import Beat
    from tubeproof.core.map_stage import ground
    from tubeproof.core.segment import Window

    class Ext:
        beats = [Beat(t=0.0, kind="hook", what="w", quote="an invented line nobody said", seg_ids=["s1"])]

    g = ground(Ext, [Window("s1", 0, 30, "hello and welcome to the show")], field="beats")
    assert g["dropped"][0]["id"] == 0.0  # was None: `t or name` skipped a falsy 0.0


def _verdict(doc, url=None):
    return {"canonical_en": "c", "canonical_local": "c", "claim_type": "platform_mechanic",
            "member_stances": [{"ref": "a:C1", "stance": "supports"}], "doc_check": {"result": doc, "url": url},
            "label": "consensus", "reasoning_local": "r", "practice_vs_docs": "unclear"}


def test_verify_retries_once_and_guards_both_answers():
    c = Cluster("K1", [mk("a:C1", "a", ctype="platform_mechanic")])
    cfg = research.verify_args({"official_domains": ["facebook.com"]})
    llm = FakeLLM([_verdict("supports", "https://blog.example.com/x"), _verdict("supports", "https://evil.com/y")])
    v = verify_stage.verify_cluster(llm, c, "topic", **cfg)
    assert len(llm.calls) == 2 and "previous answer" in llm.calls[1]["user"]
    assert v["doc_check"]["result"] == "not_checked"  # a non-official "doc" is never trusted, on either attempt
    llm = FakeLLM([_verdict("supports", "https://www.facebook.com/business/help/1")])
    assert verify_stage.verify_cluster(llm, c, "topic", **cfg)["doc_check"]["result"] == "supports"
    assert len(llm.calls) == 1


def test_unverified_cluster_stops_the_report(tmp_path):
    from tubeproof.config import layout

    c = Cluster("K1", [mk("a:C1", "a"), mk("b:C1", "b")])  # two channels: needs the verify stage
    layout.clusters(tmp_path).write_text(json.dumps([{"cluster_id": "K1", "members": [asdict(m) for m in c.members]}]))
    layout.verdicts(tmp_path).write_text("{}")
    with pytest.raises(RuntimeError, match="not verified"):
        synth_stage.build_scored(tmp_path, [], "en")


def test_appendix_labels_and_unknown_moment():
    s = {"band": "single_source", "confidence": 0.5}
    row = {"cluster_id": "K1", "score": s, "claim_local": "c", "reasoning_local": None, "test_local": None,
           "doc_url": None, "doc_quote": None, "stances": {"v1:C1": "qualifies"},
           "members": [{"ref": "v1:C1", "video_id": "v1", "channel": "ch", "date": "2026-01-01", "t": None,
                        "quote": "q", "coi": ["sells_course"], "basis": "client_data"},
                       {"ref": "v2:C1", "video_id": "v2", "channel": "ch2", "date": "2026-01-01", "t": 0.0,
                        "quote": "q", "coi": [], "basis": "own_experience"}]}
    out = synth_stage._appendix([row], {"v1": "T1", "v2": "T2"}, {"K1"}, "tr")
    assert "[T1](https://youtu.be/v1) ch · " in out  # no invented @0:00
    assert "*koşullu*" in out and "kurs satıyor" in out and "müşteri verisi" in out
    assert "[T2](https://youtu.be/v2?t=0) @0:00 · ch2" in out and "*—*" in out  # unverified member


def test_report_modes_match_research_modes():
    from tubeproof.research import MODES

    assert set(synth_stage._MODES) == set(MODES)


def test_claims_report_links_citations_and_cites_only_what_it_uses(tmp_path, monkeypatch):
    monkeypatch.setattr(synth_stage, "report_dir", lambda run_id, private: tmp_path)
    (tmp_path / synth_stage.BODY_FILE).write_text("A [K1] and test [K1 test].")
    row = {"cluster_id": "K1", "score": {"band": "likely", "confidence": 0.7}, "claim_local": "c",
           "reasoning_local": None, "test_local": None, "doc_url": None, "doc_quote": None, "stances": {},
           "members": []}
    other = dict(row, cluster_id="K2")
    out = synth_stage.render_report("r", False, [row, other], {}, "en").read_text()
    assert out.startswith("A [K1](#k1) and test [K1 test](#k1).")
    assert '<a id="k1">' in out and '<a id="k2">' not in out


def test_digest_first_hand_is_the_scores_count():
    """A first-hand member the verifier found unrelated does not make the cluster first-hand."""
    side = {"score": {"first_hand_supporting": 0, "first_hand_contradicting": 0},
            "members": [{"basis": FIRST_HAND[0]}]}
    taken = {"score": {"first_hand_supporting": 0, "first_hand_contradicting": 1}, "members": []}
    assert not synth_stage._first_hand(side)
    assert synth_stage._first_hand(taken)


def test_usage_limit_is_not_retried(monkeypatch):
    """A reached usage limit raises LLMLimitError on the first answer (retries only repeated it)."""
    import subprocess

    from tubeproof.llm import claude_cli
    from tubeproof.llm.base import LLMLimitError

    calls = []
    out = json.dumps({"is_error": True, "result": "You've hit your weekly limit · resets Nov 3 at 8am"})
    monkeypatch.setattr(claude_cli.shutil, "which", lambda _: "/bin/claude")
    monkeypatch.setattr(claude_cli.time, "sleep", lambda _: None)
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: calls.append(1) or
                        subprocess.CompletedProcess(a, 0, stdout=out, stderr=""))
    with pytest.raises(LLMLimitError, match="weekly limit"):
        claude_cli.ClaudeCLI().json("extract", "s", "u", {})
    assert len(calls) == 1


def test_usage_limit_stops_the_verify_loop(tmp_path, monkeypatch):
    """A limit is not a per-item failure: the loop stops instead of logging every cluster as failed."""
    from tubeproof.llm.base import LLMLimitError

    calls = []

    def limited(*a, **k):
        calls.append(1)
        raise LLMLimitError("limit")

    clusters = [Cluster(f"K{i}", [mk(f"a{i}:C1", "a"), mk(f"b{i}:C1", "b")]) for i in range(3)]
    monkeypatch.setattr(verify_stage, "load_clusters", lambda run_dir: clusters)
    monkeypatch.setattr(verify_stage, "verify_cluster", limited)
    monkeypatch.setattr(verify_stage.layout, "verdicts", lambda run_dir: tmp_path / "verdicts.json")
    with pytest.raises(LLMLimitError):
        verify_stage.run_verify(None, tmp_path, "t", lang="en", changes=[], domains=[], workers=1,
                                log=lambda m: None)


def test_saved_outputs_are_reused_only_when_what_shaped_them_matches(tmp_path):
    """An analysis or a verdict made in another report language (or prompt version, or from other claim
    text) is re-done: a run re-done in English once reused its Turkish claims and verdicts."""
    from tubeproof.config import layout
    from tubeproof.core.map_stage import PROMPT_VERSION, extraction_stamp, is_mapped

    p = layout.extraction(tmp_path, "v1")
    p.parent.mkdir(parents=True)
    p.write_text(json.dumps({"prompt_version": PROMPT_VERSION, "video_id": "v1"}))  # before stamps: no lang
    assert not is_mapped(tmp_path, "v1", "claims", "tr")
    p.write_text(json.dumps({**extraction_stamp("claims", "tr"), "video_id": "v1"}))
    assert is_mapped(tmp_path, "v1", "claims", "tr")
    assert not is_mapped(tmp_path, "v1", "claims", "en") and not is_mapped(tmp_path, "v1", "exemplar", "tr")

    c = Cluster("K1", [mk("a:C1", "a"), mk("b:C1", "b")])
    same = Cluster("K9", [mk("b:C1", "b"), mk("a:C1", "a")])  # renumbered and reordered: same verdict
    assert verify_stage.cluster_key(c, "tr") == verify_stage.cluster_key(same, "tr")
    assert verify_stage.cluster_key(c, "tr") != verify_stage.cluster_key(c, "en")
    reworded = Cluster("K1", [mk("a:C1", "a"), mk("b:C1", "b")])
    reworded.members[0].text_en = "another claim"  # same refs, re-analysed text
    assert verify_stage.cluster_key(c, "tr") != verify_stage.cluster_key(reworded, "tr")
    retranslated = Cluster("K1", [mk("a:C1", "a"), mk("b:C1", "b")])
    retranslated.members[0].text_local = "başka çeviri"  # only the rendering: same verdict
    assert verify_stage.cluster_key(c, "tr") == verify_stage.cluster_key(retranslated, "tr")


def test_english_report_text_is_the_english_claim(monkeypatch):
    """With an English report the model is not trusted to write the English claim twice: asked for both,
    it wrote 128 of 693 'English' copies in Turkish or German (2026-11-01)."""
    from pydantic import BaseModel

    from tubeproof.core import map_stage
    from tubeproof.models import Transcript, TranscriptSegment, VideoBundle, VideoMeta

    class C(BaseModel):
        text_en: str
        text_local: str

    class X(BaseModel):  # the extraction schema reduced to what the derivation touches
        claims: list[C]

    seg = TranscriptSegment(start=0.0, duration=10.0, text="set up search console first")
    b = VideoBundle(meta=VideoMeta(id="v1", title="t", channel="c", channel_id="c"),
                    transcript=Transcript(video_id="v1", language="en", source="whisper", segments=[seg]))

    class Llm:
        meter = CostMeter()

        def json(self, tier, system, user, schema, **kw):
            return {"claims": [{"text_en": "Set up Search Console first.", "text_local": "Önce Search Console kur."}]}

    monkeypatch.setattr(map_stage, "VideoExtraction", X)
    monkeypatch.setattr(map_stage, "ground", lambda ext, wins, **kw: {"dropped": []})
    assert map_stage.map_video(Llm(), "t", b, "en")["video"]["claims"][0]["text_local"] == "Set up Search Console first."
    assert map_stage.map_video(Llm(), "t", b, "tr")["video"]["claims"][0]["text_local"] == "Önce Search Console kur."
