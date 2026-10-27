# Status

Working state for the next session. Decisions and their reasons: `ARCHITECTURE.md`; method: `PRINCIPLES.md`.

## Done (v0.1, 2026-10-27)

- End-to-end pipeline: plan → streaming harvest (parallel audio, one Whisper) → map → reduce (+ merge pass) →
  verify (mandatory official-docs lookup) → score (rubric r3) → public and private reports.
- First research: `research/2026-10-meta-app-ads-subscription/` (35 videos, 26 channels, 752 claims, 561 clusters).
- Repository layout per research folder; English tool with per-pack `report_lang`; SSOT registry; push privacy check.

## Next

1. Running: `research/2026-10-youtube-retention/` (advice, 40 videos) and `research/2026-10-mrbeast-exemplar/`
   (exemplar mode, MrBeast's latest 30). Exemplar mode is built (K24, SSOT-34); its rules come from the
   retention runbook as hypotheses in the exemplar research's private context.
2. Evaluation set (hand-labelled videos) for free-knowledge retention and quote accuracy.
3. PyPI release once the CLI is stable.

## Known limits

- The relevance gate uses the research's question; a public pack re-run without a private context selects
  more broadly.
- The YouTube caption service rate-limits home IPs (HTTP 429); Whisper covers it, audio downloads are unaffected.
