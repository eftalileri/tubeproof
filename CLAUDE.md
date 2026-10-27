# tubeproof — agent rules

A tool that collects real practitioner experience from YouTube, strips out the paid/sales parts, and scores claims by independence.

**Read first:** `docs/PRINCIPLES.md`. It is binding; every research, on any topic, follows these principles. Architecture and rationale: `docs/ARCHITECTURE.md`.

- If a principle changes, change `docs/PRINCIPLES.md` first, then the code in the same piece of work. If the scoring rule changes, bump `RUBRIC_VERSION` in `core/score.py`.
- If a prompt changes, bump the `PROMPT_VERSION` of the relevant stage (so old outputs are not mixed with new ones).
- The reader's business data never enters the repo; private topic packs live in the reader's own folder (`--pack <path>`).
- `tubeproof-data/` is never committed (YouTube data policy).
- Tests: `.venv/bin/pytest -q`. Model names live in `llm/base.py` → `DEFAULT_MODELS` (tiers: extract/verify/synth), not in the code.
- The tool itself, code, logs and docs are written in English. The report language is set per pack (`report_lang`, e.g. `tr`).
- Stage code and prompts MUST stay topic-neutral; topic-specific wording goes in the pack (e.g. `relevance_notes`). Reason: an ad-campaign rubric in code mis-screened a YouTube-craft research (2026-10-27).
- Each video MUST be downloaded from YouTube once, as one file (`transcript.download_media`); audio, frames and picture metrics are cut from it locally, never fetched as separate audio/picture requests. Reason: every extra request moves the home IP toward YouTube's bot check (two fetches per video tripped it after ~45 videos), and audio-only streams answer 403 (2026-10-27).
- Text written in Turkish must use correct characters (ç, ğ, ı, İ, ö, ş, ü).

## SSOT — every task

One authority (single owner and writer) per datum, operation, threshold or derivation. Derived values read
their authority and never write back; on conflict the authority wins. SSOT is not "everything in one file":
different knowledge has different authorities, each registered in `docs/SSOT.md`.

**Before writing code**
1. Trace the change: input → where it is decided → where it is written → what derives from it → who consumes it.
2. Search `docs/SSOT.md` and read only the matching rows.
3. Then exactly one of:
   - **Authority exists and fits** → use it (import; never copy its logic, constant or regex).
   - **Authority exists but is insufficient** → change the authority itself (mutate it: new parameter,
     named mode, new constant in the same module). No new parallel function, wrapper or "v2".
   - **Duplicates exist** → collapse them into the one authority in the same change and delete the copies.
   - **No authority exists** → create exactly one, add its registry row (next `SSOT-NN`) in the same change,
     then add consumers.
4. Before merging two look-alike derivations, compare their outputs on the real inputs. Equal → merge.
   Different → keep one authority with an explicitly named mode that reproduces the other exactly, and
   delete the copy in the same change. Resemblance is not proof; a blind merge is a silent behaviour change.

**Forbidden:** "copy for now", a temporary second path or second state, a second definition of a constant,
list or regex that already has an owner, a stage re-deriving a value it was handed, hidden fallbacks that
substitute a default for missing data (fail loudly instead).

- A paired list (frames and their times, items and their ids) MUST be paired where it is produced, never
  re-aligned by slicing downstream: one missing frame shifted every later timestamp (2026-10-27).
- A lifetime, worker count or id prefix MUST be read from its owner, never passed as a literal by a caller:
  a caller-side TTL disagreed with the purge and deleted relevance ratings after 30 days (2026-10-27).

**Defect found → fix the whole class.** Name the wrong logic, search the whole repository for every
occurrence, bind all of them to one authority, and prove the fix on real output (a run, a measured number).
An SSOT violation seen during any task is fixed in that task; it is never deferred or dropped for cost.

**Done =** root cause fixed in its authority · `docs/SSOT.md` current (a stale registry is a bug) · a
reusable new rule written into `docs/PRINCIPLES.md` or this file as MUST / MUST NOT with a one-line reason ·
tests green · the stage output re-checked.

**Quality ratchet:** every change is a net improvement; never trade a single-authority, measured or
observable approach for a weaker one because it is faster to write.

## Research layout

Every research lives in its own folder: `research/<YYYY-MM-topic-slug>/`.

| Path | Contents | Committed? |
|---|---|---|
| `pack.yaml` | Public, generic topic pack: topic, queries, official domains, breakpoints | yes |
| `plan.json` / selection list | The videos and playlists selected for harvesting | yes |
| `REPORT.md` | Generic, shareable findings: short quotes with timestamped YouTube links, dated, with a "re-run after 3–6 months" note | yes |
| `data/` | Run data: transcripts and comments cache | never |
| `private/` | Reader-specific context, hypotheses, and the reader-tailored report | never |

- Folder names never contain a client or business name.
- Full transcripts and raw comments are never published.
