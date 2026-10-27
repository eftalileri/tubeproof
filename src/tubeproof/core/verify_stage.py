"""Stage 7 (verify): per cluster, the verify-tier model decides each member's stance,
writes the canonical claim and, for platform mechanics, checks official docs.

Single-source, non-mechanic clusters skip the LLM (nothing to cross-check); they are
scored as single-source.
"""

from __future__ import annotations

import hashlib
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Literal
from urllib.parse import urlparse

from pydantic import BaseModel, Field

from tubeproof.core.reduce_stage import Cluster, load_clusters
from tubeproof.core.segment import fmt_ts
from tubeproof.llm.base import LLM
from tubeproof.i18n import lang_of
from tubeproof.prompts import load as load_prompt

MECHANIC_TYPES = {"platform_mechanic", "numeric_threshold"}
# Platforms document settings and best practices too, so every type but income stories is checked
# (only mechanics were, and 11 of the first 17 clusters went unchecked; 2026-10-27).
DOC_CHECK_TYPES = MECHANIC_TYPES | {"setup_instruction", "tactic_efficacy"}
DOC_RULE = ("You MUST run WebSearch (restricted to the allowed domains, e.g. with site:) before "
            "answering, and WebFetch the most relevant official page. not_checked is NOT allowed: "
            "if the official docs say nothing relevant, answer silent.")


class MemberStance(BaseModel):
    ref: str
    stance: Literal["supports", "contradicts", "qualifies", "unrelated"]


class DocCheck(BaseModel):
    result: Literal["supports", "contradicts", "silent", "not_checked"]
    url: str | None = None
    quote: str | None = Field(None, description="Verbatim sentence from the official page")


class ClusterVerdict(BaseModel):
    canonical_en: str
    canonical_local: str = Field(description="The claim as one clear sentence in the report language")
    claim_type: Literal["platform_mechanic", "tactic_efficacy", "numeric_threshold", "setup_instruction",
                        "outcome_income", "opinion"]
    scope_local: str | None = Field(None, description="When it applies: budget band, objective, vertical, period")
    member_stances: list[MemberStance]
    doc_check: DocCheck
    label: Literal["consensus", "conditional", "contested", "contradicted_by_docs", "hype_or_sales",
                   "unverifiable"]
    reasoning_local: str
    contradiction_local: str | None = Field(None, description="Why sources disagree, if they do")
    practice_vs_docs: Literal["agree", "practice_contradicts_docs", "practice_only", "docs_only", "unclear"] = Field(
        description="Do first-hand practitioners (basis own_experience/client_data) agree with what the platform's docs or "
                    "platform_docs-based members say?")
    test_local: str | None = Field(None, description="If contested, contradicting docs or only single-source: one cheap "
                                "experiment the reader can run with their own data to decide (what, how long, "
                                "success metric)")
    caveats_local: list[str] = []


def cluster_key(c: Cluster) -> str:
    """Content key: re-clustering renumbers clusters, so verdicts are keyed by their members."""
    return hashlib.sha1(",".join(sorted(m.ref for m in c.members)).encode()).hexdigest()[:16]


def needs_llm(c: Cluster) -> bool:
    return len(c.channels) >= 2 or any(m.claim_type in MECHANIC_TYPES for m in c.members)


def _input(c: Cluster) -> str:
    lines = []
    for m in c.members:
        coi = ",".join(m.coi) or "none"
        lines.append(
            f"- ref={m.ref} channel={m.channel} date={m.upload_date} type={m.claim_type} polarity={m.polarity} "
            f"basis={m.basis} evidence={m.evidence_shown} coi={coi} clickbait={m.clickbait:.2f}"
            f"{' WITHHELD_TEASER' if m.is_withheld_teaser else ''}\n  claim: {m.text_en}\n"
            f"  conditions: {json.dumps({k: v for k, v in m.conditions.items() if v}, ensure_ascii=False)}\n"
            f"  quote@{fmt_ts(m.t_start or 0)}: \"{m.quote}\""
        )
        for e in m.comments[:6]:
            lines.append(f"    comment[{e['stance']}{', experiential' if e['experiential'] else ''}, "
                         f"likes={e.get('likes', 0)}]: {e.get('specifics') or ''}")
    return f"CLUSTER {c.cluster_id}\n<untrusted_data>\n" + "\n".join(lines) + "\n</untrusted_data>"


def _official(url: str | None, domains: list[str]) -> bool:
    if not url:
        return False
    p = urlparse(url)
    full = (p.hostname or "").removeprefix("www.") + p.path
    return any(full.startswith(d) for d in domains)


def _changes(cfg: dict) -> str:
    bps = cfg.get("breakpoints") or []
    return "; ".join(f"{b.get('name', 'change')} ({b['date']})" for b in bps) or "none listed"


def verify_cluster(llm: LLM, c: Cluster, topic: str, cfg: dict) -> dict:
    official_domains = cfg.get("official_domains", [])
    mechanic = any(m.claim_type in DOC_CHECK_TYPES for m in c.members)
    system = load_prompt(
        "verify_cluster.md", lang_of(cfg), topic=topic, changes=_changes(cfg), domains=", ".join(official_domains) or "(none)",
        doc_rule=(DOC_RULE if mechanic and official_domains
                  else "Do not look anything up; set doc_check.result=not_checked."),
    )
    tools = ["WebSearch", "WebFetch"] if mechanic and official_domains else None
    v = ClusterVerdict.model_validate(llm.json("verify", system, _input(c), ClusterVerdict.model_json_schema(),
                                               tools=tools))
    if v.doc_check.result in ("supports", "contradicts") and not _official(v.doc_check.url, official_domains):
        v.doc_check = DocCheck(result="not_checked")  # never trust a non-official "doc"
    if tools and v.doc_check.result == "not_checked":
        # The model skipped the lookup on 16 of 25 clusters (2026-10-27): one forced retry.
        retry = _input(c) + ("\n\nYour previous answer returned doc_check=not_checked. That is not allowed "
                             "here: search the allowed domains now; answer silent if they say nothing.")
        v2 = ClusterVerdict.model_validate(llm.json("verify", system, retry, ClusterVerdict.model_json_schema(),
                                                    tools=tools))
        if v2.doc_check.result in ("supports", "contradicts") and not _official(v2.doc_check.url, official_domains):
            v2.doc_check = DocCheck(result="not_checked")
        v = v2
    refs = {m.ref for m in c.members}
    v.member_stances = [s for s in v.member_stances if s.ref in refs]
    return v.model_dump(mode="json")


def run_verify(llm: LLM, run_dir: Path, topic: str, cfg: dict, workers: int = 4, log=print) -> dict:
    clusters = load_clusters(run_dir)
    out_path = run_dir / "verdicts.json"
    verdicts: dict = json.loads(out_path.read_text()) if out_path.exists() else {}
    todo = [c for c in clusters if needs_llm(c) and cluster_key(c) not in verdicts]
    log(f"[verify] {len(todo)} clusters to verify ({len(clusters) - len(todo)} skipped/ready)")
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futs = {ex.submit(verify_cluster, llm, c, topic, cfg): c for c in todo}
        for n, fut in enumerate(as_completed(futs), 1):
            c = futs[fut]
            try:
                verdicts[cluster_key(c)] = fut.result()
            except Exception as e:
                log(f"   ✗ {c.cluster_id}: {str(e)[:160]}")
                continue
            v = verdicts[cluster_key(c)]
            log(f"   ✓ {n}/{len(todo)} {c.cluster_id} [{v['label']}|{v['practice_vs_docs']}] "
                f"doc={v['doc_check']['result']} · "
                f"{v['canonical_local'][:70]} · ${llm.meter.usd:.2f}")
            out_path.write_text(json.dumps(verdicts, ensure_ascii=False, indent=1))
    out_path.write_text(json.dumps(verdicts, ensure_ascii=False, indent=1))
    return verdicts
