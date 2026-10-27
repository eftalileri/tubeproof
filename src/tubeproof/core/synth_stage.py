"""Stage 9 (synthesize): the synth-tier model writes the report from scored clusters.

Two reports from the same evidence: the public one (`research/<id>/REPORT.md`, no reader data)
and, when the research has a private context, the reader's one (`private/REPORT.md`).
The model only cites cluster ids like [K12]; code turns those into anchors and builds the
evidence appendix (video + timestamp links) itself, so citations can't be invented.
"""

from __future__ import annotations

import json
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

from pydantic import BaseModel

from tubeproof.core import exemplar
from tubeproof.core.harvest import read_manifest, video_titles
from tubeproof.core.reduce_stage import load_clusters
from tubeproof.core.score import BANDS, FIRST_HAND, RUBRIC_VERSION, score_cluster
from tubeproof.core.segment import fmt_ts
from tubeproof.core.verify_stage import cluster_key
from tubeproof.config import layout, settings
from tubeproof.http import short_url
from tubeproof.i18n import labels, lang_of
from tubeproof.llm.base import LLM
from tubeproof.prompts import load as load_prompt

class Report(BaseModel):
    markdown: str


def build_scored(run_dir: Path, breakpoints: list[date]) -> list[dict]:
    clusters = load_clusters(run_dir)
    vpath = layout.verdicts(run_dir)
    if not vpath.exists():
        raise FileNotFoundError(f"{vpath} missing: run `tubeproof verify` before the report")
    verdicts = json.loads(vpath.read_text())
    scored = []
    for c in clusters:
        v = verdicts.get(cluster_key(c))
        s = score_cluster(c, v, breakpoints)
        top = max(c.members, key=lambda m: (m.specificity, -m.clickbait))
        scored.append({
            "cluster_id": c.cluster_id,
            "claim_local": v["canonical_local"] if v else top.text_local,
            "claim_type": v["claim_type"] if v else top.claim_type,
            "label": v["label"] if v else None,
            "scope_local": v.get("scope_local") if v else None,
            "reasoning_local": v.get("reasoning_local") if v else None,
            "contradiction_local": v.get("contradiction_local") if v else None,
            "caveats_local": v.get("caveats_local", []) if v else [],
            "practice_vs_docs": v.get("practice_vs_docs") if v else None,
            "test_local": v.get("test_local") if v else None,
            "doc_url": v["doc_check"].get("url") if v else None,
            "doc_quote": v["doc_check"].get("quote") if v else None,
            "score": s,
            "stances": {x["ref"]: x["stance"] for x in v["member_stances"]} if v else {},
            "members": [{"ref": m.ref, "video_id": m.video_id, "channel": m.channel, "date": m.upload_date,
                         "t": m.t_start, "quote": m.quote, "coi": m.coi, "basis": m.basis} for m in c.members],
        })
    layout.scored(run_dir).write_text(json.dumps(scored, ensure_ascii=False, indent=1))
    return scored


def _first_hand(r: dict) -> bool:
    return any(m["basis"] in FIRST_HAND for m in r["members"])


def _digest(scored: list[dict], extractions_dir: Path, max_single: int = 60) -> str:
    """Single-source clusters: every first-hand one goes in, plus the best `max_single` others.
    A flat cap of 60 by confidence left out 95 of 137 first-hand single-source clusters, the
    practitioner evidence the tool exists for (2026-10-27)."""
    rows = sorted(scored, key=lambda x: (BANDS.index(x["score"]["band"]), not _first_hand(x),
                                         -x["score"]["confidence"]))
    lines, singles = [], 0
    for r in rows:
        s = r["score"]
        if s["band"] == "single_source" and not _first_hand(r):
            singles += 1
            if singles > max_single:
                continue
        lines.append(
            f"[{r['cluster_id']}] band={s['band']} conf={s['confidence']} type={r['claim_type']} "
            f"label={r['label']} independent+={s['independent_supporting']} "
            f"independent-={s['independent_contradicting']} "
            f"first_hand+={s.get('first_hand_supporting', 0)} first_hand-={s.get('first_hand_contradicting', 0)} "
            f"docs_echo={s.get('docs_echo_members', 0)} channels={s.get('channels', '?')} "
            f"comments+={s['comment_confirms']} comments-={s['comment_refutes']} doc={s['doc']} "
            f"practice_vs_docs={r.get('practice_vs_docs')}\n"
            f"   claim: {r['claim_local']}"
            + (f"\n   scope: {r['scope_local']}" if r["scope_local"] else "")
            + (f"\n   reasoning: {r['reasoning_local']}" if r["reasoning_local"] else "")
            + (f"\n   contradiction: {r['contradiction_local']}" if r["contradiction_local"] else "")
            + (f"\n   test: {r['test_local']}" if r.get("test_local") else "")
        )
    tips, sales, hype = [], [], []
    for f in sorted(extractions_dir.glob("*.json")):
        ex = json.loads(f.read_text())
        tips += (ex.get("comments") or {}).get("new_tips", [])[:4]
        v = ex["video"]
        sales += [f"{o['kind']}: {o['description'][:90]}" for o in v["offers"]][:3]
        if v["hype"]["clickbait_score"] >= 0.6:
            hype.append(f"{f.stem}: {v['hype']['rationale'][:160]}")
    return ("SCORED CLAIM CLUSTERS:\n" + "\n".join(lines)
            + "\n\nCOMMENT TIPS (unscored, from viewers):\n" + "\n".join(f"- {t}" for t in tips[:60])
            + "\n\nOFFERS SEEN (for the 'what was filtered' section):\n" + "\n".join(f"- {s}" for s in sales[:40])
            + "\n\nHIGH-HYPE VIDEOS:\n" + "\n".join(f"- {h}" for h in hype[:15]))


def _appendix(scored: list[dict], titles: dict[str, str], cited: set[str], lang: str) -> str:
    """Only the clusters the report cites: all 561 made a 425 KB file nobody reads (2026-10-27)."""
    L = labels(lang)
    out = [f"\n\n---\n\n## {L['appendix']}\n", L["appendix_intro"].format(rubric=RUBRIC_VERSION) + "\n"]
    for r in scored:
        s = r["score"]
        if r["cluster_id"] not in cited:
            continue
        out.append(f"\n### <a id=\"{r['cluster_id'].lower()}\"></a>{r['cluster_id']} · {L['band'][s['band']]} "
                   f"· {L['confidence']} {s['confidence']:.2f}\n\n{r['claim_local']}\n")
        if r.get("reasoning_local"):
            out.append(f"\n*{L['assessment']}:* {r['reasoning_local']}\n")
        if r.get("test_local"):  # the report cites these as "[K<n> <test_ref>]"
            out.append(f"\n*{L['test']}:* {r['test_local']}\n")
        if r["doc_url"]:
            out.append(f"\n- {L['official']}: [{r['doc_url']}]({r['doc_url']}) — “{(r['doc_quote'] or '')[:200]}”")
        for m in r["members"]:
            st = r["stances"].get(m["ref"], "—")
            if st == "unrelated":
                continue
            t = int(m["t"] or 0)
            coi = f" · {L['coi']}: {', '.join(m['coi'])}" if m["coi"] else ""
            basis = L["basis"].get(m.get("basis", ""), m.get("basis", ""))
            out.append(f"\n- [{titles.get(m['video_id'], m['video_id'])[:70]}]({short_url(m['video_id'], t)}) "
                       f"@{fmt_ts(t)} · {m['channel']} · {m['date']} · *{st}* · {L['basis_label']}: {basis}{coi}\n"
                       f"  > {m['quote'][:220]}")
    return "\n".join(out)


BODY_FILE = "report_body.md"
REPORT_FILE = "REPORT.md"


def report_dir(run_id: str, private: bool) -> Path:
    base = settings.research_path(run_id)
    return settings.private_dir(run_id) if private else base


def render_report(run_id: str, private: bool, scored: list[dict], titles: dict[str, str], lang: str) -> Path:
    """Model text + links + evidence appendix. Re-runnable without calling the model."""
    d = report_dir(run_id, private)
    body = (d / BODY_FILE).read_text()
    cite = re.compile(rf"\[(K\d+)( {re.escape(labels(lang)['test_ref'])})?\]")
    cited = {m.group(1) for m in cite.finditer(body)}
    md = cite.sub(lambda m: f"[{m.group(1)}{m.group(2) or ''}](#{m.group(1).lower()})", body)
    out = d / REPORT_FILE
    out.write_text(md + _appendix(scored, titles, cited, lang))
    return out


_DECISIONS = """
## The reader's decisions against the evidence
One row per decision above, as a Markdown table: Decision | What the evidence says | Status
(supported / conditional / contradicted / no evidence) | Clusters. Be blunt; "no evidence" is valid.
"""


_RULES = """
## The reader's rules against these videos
One row per rule above, as a Markdown table: Rule | What these videos do (counts, cited) |
Verdict (validated / partly / differs / no evidence) | Adopt instead, and why. "Differs" means
the videos clearly do something else: state exactly what, with numbers and citations, so the
rule can be rewritten. Do not soften a difference; "no evidence" is valid.
"""


def _exemplar_digest(run_dir: Path, vids: list[dict]) -> str:
    rows = {r["video_id"]: r for r in exemplar.table(run_dir)}
    out = []
    for n, v in enumerate(vids, 1):
        f = layout.extraction(run_dir, v["id"])
        if not f.exists():
            continue
        ex = json.loads(f.read_text())
        x, m = ex["video"], rows.get(v["id"], {})
        measured = {k: m.get(k) for k in exemplar.PICTURE_METRICS} | (ex.get("speech") or {})
        beats = "; ".join(f"{int(b['t'])}s {b['kind']}: {b['what']}" for b in x["beats"])
        loops = "; ".join(f"{l['question']} ({int(l['opened_at_s'])}s→"
                          f"{int(l['closed_at_s']) if l.get('closed_at_s') is not None else '-'}s)" for l in x["open_loops"])
        out.append(
            f"[V{n}] {v['title']} · {v.get('views')} views · {v.get('upload_date')}\n"
            f"   MEASURED: {json.dumps(measured, ensure_ascii=False)}\n"
            f"   packaging: {json.dumps(x['packaging'], ensure_ascii=False)}\n"
            f"   opening: {json.dumps(x['opening'], ensure_ascii=False)}\n"
            f"   beats: {beats}\n   open loops: {loops or '-'}\n   re-hooks: {x['rehook_interval_note']}\n"
            f"   language: {json.dumps(x['language'], ensure_ascii=False)}\n   visuals: {x['visual_style']}\n"
            f"   teaching: {json.dumps(x.get('teaching'), ensure_ascii=False)}\n"
            f"   summary: {x['summary_local']}")
    return "\n\n".join(out)


_VCITE = re.compile(r"\[V(\d+)(?: (\d+)s)?\]")


def render_exemplar(run_id: str, private: bool, vids: list[dict], lang: str) -> Path:
    """Model text with [V<n> <s>s] turned into links, plus the code-built measurement table."""
    from statistics import median

    d = report_dir(run_id, private)
    body = (d / BODY_FILE).read_text()

    def link(mt: re.Match) -> str:
        i, t = int(mt.group(1)), mt.group(2)
        if not 1 <= i <= len(vids):
            return mt.group(0)
        url = short_url(vids[i - 1]["id"], int(t) if t else None)
        return f"[V{i}{' ' + fmt_ts(int(t)) if t else ''}]({url})"

    rows = {r["video_id"]: r for r in exemplar.table(settings.run_dir(run_id))}
    L = labels(lang)
    cols = tuple(c for c in exemplar.PICTURE_METRICS if c not in ("duration_s", "cuts_first_60s"))
    scols = ("wpm", "wpm_first_10s", "wpm_first_30s", "first_speech_s")
    head = "| # | " + " | ".join(L["exemplar_cols"][c] for c in ("video", "views") + cols + scols) + " |"
    lines = [f"\n\n---\n\n## {L['exemplar_table']}\n", L["exemplar_intro"] + "\n", head,
             "|" + "---|" * (len(cols) + len(scols) + 3)]
    vals: dict[str, list] = {c: [] for c in cols + scols}
    for n, v in enumerate(vids, 1):
        r = rows.get(v["id"]) or {}
        sp = r.get("speech") or {}
        cells = [r.get(c) for c in cols] + [sp.get(c) for c in scols]
        for c, x in zip(cols + scols, cells):
            if isinstance(x, (int, float)):
                vals[c].append(x)
        lines.append(f"| V{n} | [{v['title'][:60]}]({short_url(v['id'])}) | {v.get('views') or ''} | "
                     + " | ".join("" if x is None else str(x) for x in cells) + " |")
    lines.append(f"| | **{L['exemplar_cols']['median']}** | | "
                 + " | ".join(str(round(median(vals[c]), 1)) if vals[c] else "" for c in cols + scols) + " |")
    out = d / REPORT_FILE
    out.write_text(_VCITE.sub(link, body) + "\n".join(lines) + "\n")
    return out


def _run_exemplar_synth(llm: LLM, run_id: str, cfg: dict, *, private: bool, log=print) -> Path:
    run_dir = settings.run_dir(run_id)
    lang = lang_of(cfg)
    manifest = read_manifest(run_dir)
    vids = manifest["videos"]
    topic = manifest["topic"]
    hyps = cfg.get("hypotheses") if private else None
    reader = ""
    if private:
        reader = ("\nThe reader's situation (use it to make findings concrete, never as evidence):\n"
                  f"{(cfg.get('context') or '(none given)').strip()}\n")
        if hyps:
            reader += "\nThe reader's rules to test against these videos:\n" + \
                      "\n".join(f"- {h['id']}: {h['text']}" for h in hyps) + "\n"
    system = load_prompt(
        "synthesize_exemplar.md", lang, topic=topic, question=(cfg.get("question") if private else None) or topic,
        audience="the reader described below" if private else "creators studying this channel's craft",
        n_videos=len(vids), channels=", ".join(sorted({v["channel"] or "?" for v in vids})), today=date.today(),
        reader_block=reader, rules_section=_RULES if hyps else "")
    kind = "private" if private else "public"
    log(f"[synth] {kind} exemplar report from {len(vids)} videos")
    rep = Report.model_validate(llm.json("synth", system, _exemplar_digest(run_dir, vids),
                                         Report.model_json_schema()))
    d = report_dir(run_id, private)
    d.mkdir(parents=True, exist_ok=True)
    (d / BODY_FILE).write_text(rep.markdown)
    out = render_exemplar(run_id, private, vids, lang)
    log(f"[synth] → {out} · ${llm.meter.usd:.2f}")
    return out


def run_synth(llm: LLM, run_id: str, cfg: dict, *, private: bool, log=print) -> Path:
    """`private=False` writes the public report from the topic alone; `private=True` writes the
    reader's report with their question, context and decisions. Exemplar research gets the
    exemplar report (how the videos are built, the reader's rules tested against them)."""
    from tubeproof.research import breakpoints, mode_of

    if mode_of(cfg) == "exemplar":
        return _run_exemplar_synth(llm, run_id, cfg, private=private, log=log)
    run_dir = settings.run_dir(run_id)
    lang = lang_of(cfg)
    scored = build_scored(run_dir, breakpoints(cfg))
    manifest = read_manifest(run_dir)
    titles = video_titles(manifest)
    topic = manifest["topic"]
    hyps = cfg.get("hypotheses") if private else None
    reader = ""
    if private:
        reader = ("\nThe reader's situation (their own data and plan; use it to make advice concrete, "
                  f"never as evidence):\n{(cfg.get('context') or '(none given)').strip()}\n")
        if hyps:
            reader += "\nThe reader's current decisions to test against the evidence:\n" + \
                      "\n".join(f"- {h['id']}: {h['text']}" for h in hyps) + "\n"
    system = load_prompt(
        "synthesize.md", lang, topic=topic,
        question=(cfg.get("question") if private else None) or topic,
        audience="the reader described below" if private else "practitioners researching this topic",
        n_videos=len(manifest["videos"]), n_channels=len({v["channel"] for v in manifest["videos"]}),
        today=date.today(), reader_block=reader, decision_section=_DECISIONS if hyps else "",
        fit_column="Which fits the reader better, and why" if private else "When each one applies",
        levers_rule=("The reader's goal is stated in their question." if private
                     else "The goal is the one in the question."),
        test_ref=labels(lang)["test_ref"])
    kind = "private" if private else "public"
    log(f"[synth] {kind} report from {len(scored)} clusters")
    rep = Report.model_validate(llm.json("synth", system, _digest(scored, layout.extractions(run_dir)),
                                         Report.model_json_schema()))
    d = report_dir(run_id, private)
    d.mkdir(parents=True, exist_ok=True)
    (d / BODY_FILE).write_text(rep.markdown)  # the paid part; rendering below is free to redo
    out = render_report(run_id, private, scored, titles, lang)
    log(f"[synth] → {out} · ${llm.meter.usd:.2f}")
    return out


def write_reports(llm: LLM, run_id: str, cfg: dict, log=print) -> list[Path]:
    """The public report always; the reader's report too when the research has a private context."""
    from tubeproof.research import has_private

    # The two reports read the same inputs and are independent: write them at the same time.
    kinds = [False, True] if has_private(cfg) else [False]
    with ThreadPoolExecutor(len(kinds)) as ex:
        return list(ex.map(lambda private: run_synth(llm, run_id, cfg, private=private, log=log), kinds))
