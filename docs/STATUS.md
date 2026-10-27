# Status

Working state for the next session. Decisions and their reasons: `ARCHITECTURE.md`; method: `PRINCIPLES.md`.

## Done (v0.1, 2026-10-27)

- End-to-end pipeline: plan → streaming harvest (parallel audio, one Whisper) → map → reduce (+ merge pass) →
  verify (mandatory official-docs lookup) → score (rubric r3) → public and private reports.
- First research: `research/2026-10-meta-app-ads-subscription/` (35 videos, 26 channels, 752 claims, 561 clusters).
- Repository layout per research folder; English tool with per-pack `report_lang`; SSOT registry; push privacy check.

## Next

1. A research on YouTube video presentation (titles/thumbnails, first seconds, retention structure, natural
   script language). It needs an **exemplar mode**: analysing how a channel's own top videos are built
   (opening, promise delivery, pacing), not only advice claims. Add it by extending harvest selection
   (a channel's latest N videos) and the map prompt (named mode), per `SSOT.md`.
2. Evaluation set (hand-labelled videos) for free-knowledge retention and quote accuracy.
3. PyPI release once the CLI is stable.

## Known limits

- The relevance gate uses the research's question; a public pack re-run without a private context selects
  more broadly.
- The YouTube caption service rate-limits home IPs (HTTP 429); Whisper covers it, audio downloads are unaffected.
