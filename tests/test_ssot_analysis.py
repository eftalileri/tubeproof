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
        synth_stage.build_scored(tmp_path, [])


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
