"""Stage 8 (score): deterministic, versioned confidence from LLM labels.

Additive log-odds so one strong source and several weak ones are comparable;
confidence = sigmoid(logit). The LLM never produces the number.

Independence is by *source*, not by channel: five creators repeating Meta's docs are one
vote ("docs echo"), channels reading near-identical scripts are merged, and only first-hand
claims (own runs, client accounts) count as practitioner evidence.
"""

from __future__ import annotations

import math
from datetime import date

from rapidfuzz import fuzz

from tubeproof.config import DAYS_PER_MONTH
from tubeproof.core.reduce_stage import Cluster, Member

RUBRIC_VERSION = "r3"

COMMENT_CONFIRM, COMMENT_CONFIRM_CAP = 0.4, 1.6
COMMENT_REFUTE, COMMENT_REFUTE_CAP = -0.5, -2.0  # asymmetric: creators can delete criticism
DOC_SUPPORT, DOC_CONTRADICT = 2.0, -3.0
# Practitioner evidence (PRINCIPLES 9). A tuple: the verify prompt and schema list it in this order.
FIRST_HAND = ("own_experience", "client_data")
# Bands from strongest to weakest; reports sort and filter by this order.
BANDS = ("well_supported", "likely", "contested", "doubtful", "single_source", "unverifiable")
BASIS_FACTOR = {"own_experience": 1.0, "client_data": 1.0, "general_knowledge": 0.7, "other_creator": 0.5,
                "platform_docs": 1.0}
# Evidence the platform's own dashboard or another company's data shows on screen (PRINCIPLES 10).
SHOWN_EVIDENCE = ("screen_ads_manager", "third_party")
# Conflict of interest halves efficacy claims, not "how the interface works" claims (PRINCIPLES 11).
COI_EXEMPT_TYPES = ("platform_mechanic", "setup_instruction")
# Claim types halved again when made before a platform breakpoint (PRINCIPLES 12).
BREAKPOINT_TYPES = ("platform_mechanic", "tactic_efficacy")
DOCS_ECHO = "DOCS_ECHO"
SCRIPT_DUP = 88  # token-set similarity of quotes above which two channels count as one script
# Clickbait score above which a source is down-weighted and its video listed as high-hype in the report.
CLICKBAIT_HIGH = 0.7


def org_key(channel: str) -> str:
    """Channels of one company are one source: "Sub Club by RevenueCat" = "RevenueCat",
    "App Leaders Club Türkiye by Adapty" = "App Leaders by Adapty" (2026-10-27)."""
    name = channel.casefold().strip()
    return "org:" + (name.rsplit(" by ", 1)[1].strip() if " by " in name else name)


def independence_groups(members: list[Member]) -> dict[str, str]:
    """ref -> independence group."""
    parent = {m.ref: (DOCS_ECHO if m.basis == "platform_docs" else org_key(m.channel)) for m in members}

    def find(g: str) -> str:
        while parent.get(g, g) != g:
            g = parent[g]
        return g

    roots = {m.ref: org_key(m.channel) for m in members if m.basis != "platform_docs"}
    for ch in set(roots.values()):
        parent.setdefault(ch, ch)
    parent.setdefault(DOCS_ECHO, DOCS_ECHO)
    others = [m for m in members if m.basis != "platform_docs" and len(m.quote) > 30]
    for i, a in enumerate(others):
        for b in others[i + 1:]:
            ka, kb = org_key(a.channel), org_key(b.channel)
            if ka != kb and fuzz.token_set_ratio(a.quote, b.quote) >= SCRIPT_DUP:
                ra, rb = find(ka), find(kb)
                if ra != rb:
                    parent[rb] = ra
    return {m.ref: find(parent[m.ref]) if m.basis != "platform_docs" else DOCS_ECHO for m in members}


HALF_LIFE_MONTHS = 12.0  # a source's weight halves every 12 months (PRINCIPLES 12)
# A source with no upload date is weighted as one half-life old: neither fresh nor discarded.
UNKNOWN_AGE_MONTHS = HALF_LIFE_MONTHS


def age_months(upload_date: str | None) -> float:
    if not upload_date:
        return UNKNOWN_AGE_MONTHS
    return max((date.today() - date.fromisoformat(upload_date)).days / DAYS_PER_MONTH, 0.0)


def _source_weight(m: Member, breakpoints: list[date]) -> float:
    w = 1.0 if m.evidence_shown in SHOWN_EVIDENCE else 0.6
    w *= BASIS_FACTOR[m.basis]
    if m.coi and m.claim_type not in COI_EXEMPT_TYPES:
        w *= 0.5
    w *= 0.5 ** (age_months(m.upload_date) / HALF_LIFE_MONTHS)
    if m.upload_date and m.claim_type in BREAKPOINT_TYPES:
        if any(date.fromisoformat(m.upload_date) < bp for bp in breakpoints):
            w *= 0.5
    if m.clickbait > CLICKBAIT_HIGH:
        w *= 0.7
    if m.is_withheld_teaser:
        w *= 0.5
    return w


def _like_factor(likes: int) -> float:
    return 0.5 + 0.5 * min(1.0, math.log10(1 + likes) / 2)


def score_cluster(c: Cluster, verdict: dict | None, breakpoints: list[date]) -> dict:
    stances = {s["ref"]: s["stance"] for s in (verdict or {}).get("member_stances", [])}
    if verdict is None:  # single-source cluster, not LLM-verified
        stances = {m.ref: "supports" for m in c.members}
    groups = independence_groups(c.members)
    logit = 0.0
    best: dict[tuple[str, str], float] = {}  # one vote per independence group per side
    first_hand: dict[str, set[str]] = {"supports": set(), "contradicts": set()}
    echo = 0
    for m in c.members:
        st = stances.get(m.ref, "unrelated")
        if st not in ("supports", "contradicts", "qualifies"):
            continue
        side = "contradicts" if st == "contradicts" else "supports"
        w = _source_weight(m, breakpoints) * (0.6 if st == "qualifies" else 1.0)
        key = (groups[m.ref], side)
        best[key] = max(best.get(key, 0.0), w)
        if m.basis in FIRST_HAND:
            first_hand[side].add(groups[m.ref])
        if m.basis == "platform_docs":
            echo += 1
    support_g = {g for (g, side) in best if side == "supports"}
    contra_g = {g for (g, side) in best if side == "contradicts"}
    for (g, side), w in best.items():
        logit += w if side == "supports" else -0.7 * (w / 0.6)  # -0.7 for a verbal-strength source

    conf_sum = refute_sum = 0.0
    n_conf = n_ref = 0
    for m in c.members:
        st = stances.get(m.ref, "unrelated")
        if st == "unrelated":
            continue
        flip = st == "contradicts"  # comment stance is toward the member claim
        for e in m.comments:
            k = _like_factor(int(e["likes"]))
            s = e["stance"]
            if s == "confirms" and e["experiential"]:
                if flip:
                    refute_sum += COMMENT_REFUTE * k
                    n_ref += 1
                else:
                    conf_sum += COMMENT_CONFIRM * k
                    n_conf += 1
            elif s == "refutes":
                val = (COMMENT_REFUTE if e["experiential"] else COMMENT_REFUTE / 2) * k
                if flip:
                    conf_sum += -val * 0.8
                    n_conf += 1
                else:
                    refute_sum += val
                    n_ref += 1
    logit += min(conf_sum, COMMENT_CONFIRM_CAP) + max(refute_sum, COMMENT_REFUTE_CAP)

    doc = (verdict or {}).get("doc_check", {}).get("result")
    if doc == "supports":
        logit += DOC_SUPPORT
    elif doc == "contradicts":
        logit += DOC_CONTRADICT

    conf = 1 / (1 + math.exp(-logit))
    independent = support_g | contra_g
    volume = len(independent) + n_conf + n_ref
    label = (verdict or {}).get("label")
    claim_types = {m.claim_type for m in c.members}
    if label in ("hype_or_sales", "unverifiable") or claim_types == {"outcome_income"}:
        band = "unverifiable"
    elif len(independent) < 2 and doc not in ("supports", "contradicts"):
        band = "single_source"
    elif conf >= 0.80:
        band = "well_supported"
    elif conf >= 0.60:
        band = "likely"
    elif conf >= 0.40:
        band = "contested"
    else:
        band = "doubtful"
    return {
        "rubric_version": RUBRIC_VERSION, "logit": round(logit, 3), "confidence": round(conf, 3),
        "band": band, "independent_supporting": len(support_g), "independent_contradicting": len(contra_g),
        "first_hand_supporting": len(first_hand["supports"]),
        "first_hand_contradicting": len(first_hand["contradicts"]),
        "docs_echo_members": echo, "channels": len({m.channel_id for m in c.members}),
        "comment_confirms": n_conf, "comment_refutes": n_ref, "evidence_volume": volume,
        "doc": doc or "not_checked",
    }
