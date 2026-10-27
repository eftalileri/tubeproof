from datetime import date, timedelta

from tubeproof.core.reduce_stage import Cluster, Member
from tubeproof.core.score import score_cluster


def mk(ref, channel, evidence="verbal_numbers", coi=(), comments=(), months_old=2, ctype="tactic_efficacy"):
    d = (date.today() - timedelta(days=int(months_old * 30.44))).isoformat()
    return Member(ref=ref, video_id=ref.split(":")[0], channel_id=channel, channel=channel, upload_date=d,
                  text_en="x", text_local="x", quote="q", t_start=0, claim_type=ctype, polarity="do",
                  specificity=2, evidence_shown=evidence, conditions={}, is_withheld_teaser=False,
                  survivorship_flags=[], coi=list(coi), clickbait=0.2, comments=list(comments),
                  basis="own_experience")


def verdict(stances, doc="silent", label="consensus"):
    return {"member_stances": [{"ref": r, "stance": s} for r, s in stances.items()],
            "doc_check": {"result": doc}, "label": label}


def test_independent_agreement_beats_single_source():
    c = Cluster("K1", [mk("a:C1", "ch1"), mk("b:C1", "ch2"), mk("c:C1", "ch3")])
    s = score_cluster(c, verdict({"a:C1": "supports", "b:C1": "supports", "c:C1": "supports"}), [])
    assert s["independent_supporting"] == 3 and s["band"] in ("likely", "well_supported")


def test_same_channel_counts_once():
    c = Cluster("K1", [mk("a:C1", "ch1"), mk("b:C1", "ch1")])
    s = score_cluster(c, verdict({"a:C1": "supports", "b:C1": "supports"}), [])
    assert s["independent_supporting"] == 1 and s["band"] == "single_source"


def test_experiential_refutations_and_docs_dominate():
    refute = {"stance": "refutes", "experiential": True, "likes": 50}
    c = Cluster("K1", [mk("a:C1", "ch1", comments=[refute] * 4), mk("b:C1", "ch2")])
    s = score_cluster(c, verdict({"a:C1": "supports", "b:C1": "supports"}, doc="contradicts"), [])
    assert s["confidence"] < 0.4 and s["band"] == "doubtful"


def test_pre_breakpoint_and_coi_lower_weight():
    fresh = score_cluster(Cluster("K", [mk("a:C", "1"), mk("b:C", "2")]),
                          verdict({"a:C": "supports", "b:C": "supports"}), [])
    stale = score_cluster(Cluster("K", [mk("a:C", "1", coi=["sells_course"], months_old=20),
                                        mk("b:C", "2", coi=["sells_course"], months_old=20)]),
                          verdict({"a:C": "supports", "b:C": "supports"}), [date.today() - timedelta(days=300)])
    assert stale["confidence"] < fresh["confidence"]


def test_income_claims_unverifiable():
    c = Cluster("K1", [mk("a:C1", "ch1", ctype="outcome_income"), mk("b:C1", "ch2", ctype="outcome_income")])
    s = score_cluster(c, verdict({"a:C1": "supports", "b:C1": "supports"}), [])
    assert s["band"] == "unverifiable"


def test_docs_echo_counts_once():
    ms = [mk(f"{v}:C1", f"ch{v}") for v in "abcd"]
    for m in ms:
        m.basis = "platform_docs"
    s = score_cluster(Cluster("K1", ms), verdict({m.ref: "supports" for m in ms}), [])
    assert s["independent_supporting"] == 1 and s["docs_echo_members"] == 4 and s["band"] == "single_source"


def test_copied_script_across_channels_merges():
    a, b = mk("a:C1", "ch1"), mk("b:C1", "ch2")
    a.quote = b.quote = "keep the budget in one ad set until you hit fifty conversions per week"
    s = score_cluster(Cluster("K1", [a, b]), verdict({"a:C1": "supports", "b:C1": "supports"}), [])
    assert s["independent_supporting"] == 1


def test_first_hand_outweighs_hearsay():
    fh = [mk("a:C", "1"), mk("b:C", "2")]
    hs = [mk("a:C", "1"), mk("b:C", "2")]
    for m in fh:
        m.basis = "own_experience"
    for m in hs:
        m.basis = "other_creator"
    v = verdict({"a:C": "supports", "b:C": "supports"})
    s_fh, s_hs = score_cluster(Cluster("K", fh), v, []), score_cluster(Cluster("K", hs), v, [])
    assert s_fh["confidence"] > s_hs["confidence"] and s_fh["first_hand_supporting"] == 2
