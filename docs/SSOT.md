# SSOT registry

Every single source of truth in tubeproof is one row here. **Anything not in this registry is not a source of truth.**
The registry says **where** a change goes: when behaviour must improve, the source itself is changed (mutated);
no copy, wrapper or parallel function is added. Binding rules are in `CLAUDE.md`.

**Registry rules**
- The same knowledge is never written twice; consumers import it from its source.
- Need something new? First look here. If a row covers it, extend that source (new parameter, new branch,
  new constant in the same module). Only genuinely new shared knowledge gets a new row (next `SSOT-NN`),
  added in the same change as the code.
- A removed source keeps its row as `removed`, naming what replaced it.
- Constants carry the date and the measurement that set them in a comment (why this value).

| No | Topic | Single source | Change rule | Consumers | Status |
|---|---|---|---|---|---|
| SSOT-01 | Settings and paths (data/cache dir, research dir and per-research paths, cache TTL, delays, API key, JS runtime; `TUBEPROOF_*` env overrides) | `config.py` → `Settings`, `settings`, `research_path`, `run_dir` | No path or env var read elsewhere; new setting = new field here | all modules | active |
| SSOT-02 | Data models (search hit, video meta, transcript, comment, link, bundle; `SCHEMA_VERSION`) | `models.py` | Shape changes only here; bump `SCHEMA_VERSION` | harvest, stages, MCP | active |
| SSOT-03 | Cache and run index (kinds, TTL, run rows) | `store/db.py` → `Store` | No other SQLite/file cache; new cached thing = new `kind` | harvest, transcript, screen, pipeline | active |
| SSOT-04 | HTTP politeness (per-host throttle, retries, client) and host matching | `http.py` → `throttle`, `client`, `request`, `YOUTUBE_HOSTS`, `host_match` | Every outbound web request goes through here; every host-list check uses `host_match` | links, linkclass, transcript, innertube | active |
| SSOT-05 | YouTube search (innertube `sp` params, buckets, parsing of ages/counts/durations) | `sources/youtube/innertube.py` → `build_params`, `upload_bucket`, `search`, `parse_*` | Search params only here; UI language pinned to English (date parsing) | discover, CLI, MCP | active |
| SSOT-06 | Video and playlist metadata, paid-promotion disclosure, **all yt-dlp option sets** | `sources/youtube/metadata.py` → `video_meta`, `playlist_meta`, `has_paid_promotion`, `ydl_opts` | Every `yt_dlp.YoutubeDL(...)` call takes `ydl_opts(**extra)` | harvest, transcript | active |
| SSOT-07 | Transcript chain (captions → yt-dlp orig → Whisper), caption circuit breaker, audio download (original track, native downloader), Whisper engine/tempo/cap | `sources/youtube/transcript.py` → `fetch_transcript`, `download_audio`, `transcribe_audio`, `captions_blocked`, `BLOCK_COOLDOWN`, `WHISPER_TEMPO`, `WHISPER_MAX_MINUTES`, `MLX_MODEL` | One audio/Whisper path for the whole project; no ranged downloads (measured 100× slower) | harvest, pipeline | active |
| SSOT-08 | Comments (popular + recent, author hashing) | `sources/youtube/comments.py` → `fetch_comments`, `_author_hash` | Author names never stored in clear | harvest | active |
| SSOT-09 | Link classification (affiliate / course / booking / hub / social / docs hosts, sales paths, shorteners) | `filters/linkclass.py` → `classify`, host tuples | New host or pattern = add to the tuple here | links, map input | active |
| SSOT-10 | Description link processing (URL extraction, redirect unwrap, linktree, free-page text) and **URL patterns** | `fetch/links.py` → `extract_urls`, `process_links`, `URL_RE`, `URL_OR_WWW_RE` | No other URL regex in the project | harvest, spam filter | active |
| SSOT-11 | Comment spam rules | `filters/spam.py` → `flag_spam` | New spam pattern = new regex here | map comments | active |
| SSOT-12 | Discovery and candidate ranking (popularity + relevance runs, diversity) | `core/discover.py` → `discover`, `rank_score`, `select_diverse` | — | harvest | active |
| SSOT-13 | Relevance gate (topic-neutral tiers 0–3 + the pack's `relevance_notes` examples, two passes keep the min, cached by rubric hash) | `core/screen.py` → `screen`, `MIN_SCORE`, `PASSES`, `_SYSTEM` | Rubric text change changes the cache key automatically; topic-specific wording goes in the pack, never in `_SYSTEM` | harvest | active |
| SSOT-14 | Selection policy (pool sizes, market-language quota, view floors, per-channel cap, age/length limits, plan mode) | `core/harvest.py` → `harvest`, `_harvest_plan` | Selection rules only here; defaults are the policy | CLI, MCP, pipeline | active |
| SSOT-15 | Streaming pipeline (download pool, single Whisper worker, map pool, coverage check, stage skipping on resume) | `core/pipeline.py` → `process`, `coverage`, `MIN_COVERAGE` | Stage order and resume rules only here | CLI, MCP | active |
| SSOT-16 | Transcript windows and timestamps | `core/segment.py` → `windows`, `fmt_ts` | — | map, synth | active |
| SSOT-17 | Extraction schema (claims, basis, offers, hype, comments) | `core/extraction.py` | Field change = bump map `PROMPT_VERSION` | map, reduce | active |
| SSOT-18 | Map stage (claim budget, quote grounding, input limits) | `core/map_stage.py` → `map_video`, `run_map`, `claim_budget`, `ground`, `QUOTE_MATCH_MIN`, `PROMPT_VERSION` | — | pipeline, CLI | active |
| SSOT-19 | Clustering (embedding model, blocks, LLM adjudication, merge pass) | `core/reduce_stage.py` → `cluster`, `blocks`, `adjudicate`, `merge_pass`, `EMBED_MODEL`, `*_THRESHOLD` | — | verify, score, synth | active |
| SSOT-20 | Verification (stances, official-domain doc check, which claim types are checked, forced lookup) | `core/verify_stage.py` → `verify_cluster`, `needs_llm`, `cluster_key`, `DOC_CHECK_TYPES`, `DOC_RULE`, `_official` | Verdicts keyed by member content, never by cluster number | synth | active |
| SSOT-21 | Scoring rubric (independence groups, company channels = one source, docs echo, basis weights, COI, recency, bands) | `core/score.py` → `score_cluster`, `independence_groups`, `org_key`, `BASIS_FACTOR`, `RUBRIC_VERSION` | Any rule change bumps `RUBRIC_VERSION`; principle first in `PRINCIPLES.md` | synth, MCP | active |
| SSOT-22 | Report evidence (scored clusters, digest for the model, cited-only evidence appendix) | `core/synth_stage.py` → `build_scored`, `_digest`, `_appendix` | Labels come from `i18n` (SSOT-32); first-hand single-source clusters always reach the digest | synth | active |
| SSOT-23 | Prompts and their loading (report-language name and writing rule appended) | `prompts/*.md`; loader `prompts/__init__.py` → `load(name, lang, **kw)` | No stage reads a prompt file itself; edit bumps that stage's version | stages | active |
| SSOT-24 | LLM backends, tiers and model names, cost meter | `llm/base.py` → `DEFAULT_MODELS`, `get_backend`, `CostMeter`; `llm/claude_cli.py` | Model names never appear elsewhere | all LLM stages | active |
| SSOT-25 | Topic packs and research configuration (public pack + private context merge, harvest from config, breakpoints, relevance notes) | `research.py` → `load_config`, `harvest`, `breakpoints`, `has_private`; example packs `packs/` → `load_pack`; per research `research/<id>/pack.yaml` + `private/context.yaml` | CLI and MCP never map config to stage arguments themselves | CLI, MCP | active |
| SSOT-26 | CLI commands | `cli.py` | Commands call `research` and stage functions; no logic here | user | active |
| SSOT-27 | MCP tools | `mcp_server.py` | Tools call `research` and `core.pipeline.process`, the same as the CLI | MCP clients | active |
| SSOT-28 | Research principles (binding method) | `docs/PRINCIPLES.md` | Principle first, code in the same change | all stages | active |
| SSOT-29 | Architecture decisions and measured values | `docs/ARCHITECTURE.md` | New decision = new K-number with reason | maintainers | active |
| SSOT-30 | Agent rules | `CLAUDE.md` | Rules only there; other docs link | agents | active |
| SSOT-31 | Push privacy guard (ignored paths, private-term and secret scan) | `.gitignore`, `scripts/check_private.py` (+ `pre-push` hook), private term list outside the repo `~/.config/tubeproof/private-terms.txt` | Nothing private is pushed; guard runs on every push | git | planned |
| SSOT-32 | Report language: language names, per-language writing rules, fixed report labels (bands, basis, appendix) | `i18n.py` → `lang_of`, `language_name`, `lang_rule`, `labels` | New language = one entry in `LANG_NAMES` + `LABELS`; no label text in stage code | prompts loader, synth | active |
| SSOT-33 | Report writing (public vs private report, paid body saved, free re-render) | `core/synth_stage.py` → `write_reports`, `run_synth`, `render_report`, `report_dir`, `BODY_FILE`, `REPORT_FILE` | Report paths come only from `report_dir` | pipeline, CLI, MCP | active |
