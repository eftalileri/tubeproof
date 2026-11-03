# Status

Working state for the next session. Decisions and their reasons: `ARCHITECTURE.md`; method: `PRINCIPLES.md`.

## Done (v0.1, 2026-10-27)

- End-to-end pipeline: plan → streaming harvest (parallel audio, one Whisper) → map → reduce (+ merge pass) →
  verify (mandatory official-docs lookup) → score (rubric r3) → public and private reports.
- First research: `research/2026-10-meta-app-ads-subscription/` (35 videos, 26 channels, 752 claims, 561 clusters).
- Repository layout per research folder; English tool with per-pack `report_lang`; SSOT registry; push privacy check.

## Next

1. YouTube video strategy researches are grouped in `research/youtube-video-strategies/` (advice:
   `2026-10-youtube-retention/`, 40 videos; exemplar mode: one folder per channel, e.g. MrBeast's latest 30). Exemplar mode is built (K24, SSOT-34); its rules come from the
   retention runbook as hypotheses in the exemplar research's private context.
2. Evaluation set (hand-labelled videos) for free-knowledge retention and quote accuracy.
3. PyPI release once the CLI is stable.

## Known limits

- The relevance gate uses the research's question; a public pack re-run without a private context selects
  more broadly.
- The YouTube caption service rate-limits home IPs (HTTP 429); Whisper covers it.
- The `claude -p` backend shares the account's weekly usage limit; a reached limit stops the run loudly
  (`LLMLimitError`), finished work is kept and the run resumes after the reset.
- Too many watch-page loads trip YouTube's IP bot check (`/watch` answers 429; search and browse keep working). Runs stop
  loudly and resume after it lifts; tubeproof never works around it (no cookies, no client spoofing).
