# tubeproof — agent rules

A tool that collects real practitioner experience from YouTube, strips out the paid/sales parts, and scores claims by independence.

**Read first:** `docs/PRINCIPLES.md`. It is binding; every research, on any topic, follows these principles. Architecture and rationale: `docs/ARCHITECTURE.md`.

- If a principle changes, change `docs/PRINCIPLES.md` first, then the code in the same piece of work. If the scoring rule changes, bump `RUBRIC_VERSION` in `core/score.py`.
- If a prompt changes, bump the `PROMPT_VERSION` of the relevant stage (map, exemplar, verify) so old outputs are not mixed with new ones.
- The reader's business data never enters the repo; private topic packs live in the reader's own folder (`--pack <path>`).
- `tubeproof-data/` is never committed (YouTube data policy).
- Tests: `.venv/bin/pytest -q`. Model names live in `llm/base.py` → `DEFAULT_MODELS` (tiers: extract/verify/synth), not in the code.
- The tool itself, code, logs and docs are written in English. The report language is set per pack (`report_lang`, e.g. `tr`).
  A committed (public) research MUST have `report_lang: en` and an English pack topic; a research in another language
  stays unpublished until it is regenerated in English. Reason: the public repo serves an international audience
  (owner decision, 2026-11-03).
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
- A research's configuration (pack and private context) MUST be checked for shape when it is loaded, before
  any harvesting: a plain-string hypothesis passed every stage and crashed the private report after a full
  run (2026-10-31).
- A saved stage output (extraction, verdict) MUST be reused only when every input that shaped it matches:
  prompt version, report language and the content it was made from. Keyed by file existence and refs alone, a
  research re-done in English reused its Turkish claims and verdicts (2026-11-01).
- A stage MUST NOT ask the model to write the same knowledge twice (e.g. the English claim and its "report
  language" copy when the report is English): the second copy drifted, 128 of 693 came back in Turkish or German
  (2026-11-01).
- An account-level stop (YouTube bot check, LLM usage limit) MUST stop the stage loudly and MUST NOT be
  retried or counted as a per-item failure: a usage limit was retried 3× per call and would have marked
  every remaining video "failed" while the report went ahead on a partial sample (2026-11-01).
- A saved record MUST NOT hold an absolute path: it stores paths relative to the folder `config.Layout` gives it
  and its loader resolves them. Reason: moving researches into a group folder broke all 144 exemplar records
  (2026-11-03).
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

Every research lives in its own folder: `research/<YYYY-MM-topic-slug>/`. Researches of one theme are grouped in a
parent folder, `research/<theme>/<YYYY-MM-topic-slug>/` (e.g. `research/youtube-video-strategies/`, which lists its
children in its `README.md`); the research id is then `<theme>/<YYYY-MM-topic-slug>`.

- A research id MUST be resolved to a folder only by `config.research_path` (the pack's `name` holds the same
  id): a stage or caller joining paths itself would miss a grouped research or recreate a moved one empty.
- An unpublished research (sold, private or not yet English) MUST be excluded in `.git/info/exclude`, never in
  `.gitignore`: the ignore line would publish its name.

| Path | Contents | Committed? |
|---|---|---|
| `pack.yaml` | Public, generic topic pack: topic, queries, official domains, breakpoints | yes |
| `plan.json` / selection list | The videos and playlists selected for harvesting | yes |
| `REPORT.md` (+ `report_body.md`) | Generic, shareable findings in English: short quotes with timestamped YouTube links, dated, with a "re-run after 3–6 months" note | yes |
| `guide/` (optional) | Hand-written, generic how-to guides built on the report: every evidence statement cites a `REPORT.md` cluster (video links come from the report, never typed by hand), an official document, a named public repository, or the guide's own stated audit; no reader data, brand or business | yes |
| `data/` | Run data: transcripts and comments cache | never |
| `private/` | Reader-specific context, hypotheses, and the reader-tailored report | never |

- Folder names never contain a client or business name.
- Full transcripts and raw comments are never published.
