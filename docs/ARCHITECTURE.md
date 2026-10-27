# tubeproof — Architecture Document v1.0

> An open-source tool that collects real practitioner experience from YouTube, strips out the paid/sales parts, cross-checks claims, and produces a confidence-scored report.
> Date: 2026-10-27 · Status: Phases 1–3 coded and tested end to end (v0.1). MCP server (Phase 4) is next.

---

## 1. Problem

Given a topic (first test: **"getting through the learning phase on low budget in Meta/Reels ads"**), the tool:

1. Finds popular videos and **training sets (playlists)** on YouTube, date-filtered (default: last 12 months), in **any language**.
2. For each video, reads the **transcript, description, the content of links in the description, and the comments**.
3. **Discards only the paid/sales part**; keeps the free information in the same video.
4. Flags clickbait, exaggeration and unverifiable "I made X" claims.
5. Cross-checks claims across videos, against "I tried it, it worked / didn't work" feedback in comments, and against official documentation.
6. Produces a confidence-scored report that ties every piece of information to its source video and second.

**Constraint:** No dependency on Firecrawl. The official YouTube API and LLM use are allowed.

---

## 2. Research findings (summary)

### 2.1 Is there a ready-made project? → **None end to end.**

I reviewed about 40 repos. Stars, last-update and license data were taken from the GitHub API on 2026-10-27.

| Candidate | What it does | What is missing |
|---|---|---|
| `mvanhorn/last30days-skill` (65k★, MIT) | Date-range search, popularity ranking, transcript, comments, LLM summary. Runs as a Claude Code plugin. | YouTube is a side source there: no playlists, truncates descriptions, does not read links, no sales removal or verification. |
| `kevinwatt/yt-dlp-mcp` (297★, MIT) | Keyless search, date filter, transcript, comments | No playlists, no link reading, no analysis |
| `ZubeidHendricks/youtube-mcp-server` (589★, MIT) | API search (`order=viewCount`), playlists | No comments, no analysis |
| `danielmiessler/Fabric` (44k★) | Ready-made `analyze_claims` claim-analysis prompt | No search; works on a single URL |
| GPT-Researcher, STORM, local-deep-research | Web deep-research frameworks | None has a YouTube source. open_deep_research is archived. |
| SurfSense | Has a good YouTube plugin | **BSL licensed**, unusable in open source |

**Conclusion:**
- The **data-fetching layer** is solved by mature libraries: yt-dlp, youtube-transcript-api, youtube-comment-downloader, trafilatura.
- The **analysis layer** (sales removal, reliability scoring, cross-video and comment–claim verification) **exists nowhere**. This is where the project's real value is.

### 2.2 Data access: the real situation as of 2026

Tests were run on a Mac over a home connection.

- **YouTube Data API v3**
  - Since June 2026, `search.list` has its own quota: **100 calls per day**.
  - `videos.list`, comments and playlist calls cost 1 unit each from the daily 10,000-unit quota.
  - **The API does not provide captions of other people's videos** (requires the video owner's authorization).
- **Keyless search (innertube)**
  - Popularity ordering and today/week/month/year filters work (`sp=CAM=`, `EgIIBA==` etc.).
  - **Sorting by date was removed in January 2026.**
  - An exact date range can only be obtained via the API.
- **Transcript**
  - youtube-transcript-api succeeded 5/5 from a home IP.
  - In yt-dlp, `.*-orig` (original language) subtitles work. **Translated subtitles consistently return 429 errors.**
  - Last resort: download the audio and transcribe it with **mlx-whisper** (fast on an M4).
- **Comments**
  - youtube-comment-downloader fetched 55 comments in 4.6 seconds, including replies and the "heart" flag.
- **Links**
  - trafilatura extracted a page in 1.1 seconds.
  - linktr.ee content is read from `__NEXT_DATA__`.
  - Playwright for pages that need JavaScript, markitdown for PDF/DOCX.
- **Sponsor detection**
  - The "Includes paid promotion" marker on the watch page (`paidContentOverlayRenderer`) was verified.
  - SponsorBlock was unreachable from the test network. It remains an optional source.

### 2.3 Analysis: scientific basis

- **Claim extraction:** SAFE, VeriScore and Claimify methods. Each claim must be atomic and readable independently of its context; only verifiable ones are kept.
- **Clickbait:** Ready-made models look only at the title. What we need is "is the promise in the title delivered in the video?" An LLM reading the transcript does this far better.
- **Comments:**
  - Like count is not an indicator of truth; even fake comments can get more likes.
  - The creator can delete critical comments, so **refuting comments weigh more**.
  - Bot and scam comments (WhatsApp/Telegram numbers, accounts impersonating the channel owner) are removed by code before reaching the LLM.
- **Independence:** 5 channels repeating the same mentor's course do not count as 5 sources; they count as **one source**.
- **Recency:** Meta's Andromeda infrastructure (December 2024) changed the rules. The weight of older videos is halved.

---

## 3. Architecture decisions (with rationale)

| # | Decision | Rationale |
|---|---|---|
| K1 | **No fork; a from-scratch core plus mature libraries** | No repo meets even 40% of the need. A fork means carrying code we do not want. Ideas will be borrowed: last30days' ranking, Fabric's `analyze_claims` prompt, coyaSONG's timestamped quotes. |
| K2 | **Python 3.12+** | All critical libraries are Python: yt-dlp, transcript-api, comment-downloader, trafilatura, mlx-whisper. |
| K3 | **One core, two thin shells: CLI + MCP** | All business logic lives in `tubeproof.core`. The CLI (Typer) and the MCP server (official `mcp` SDK, FastMCP) are only calling layers. We do not write the same code twice. |
| K4 | **Staged pipeline that resumes where it left off** | Each stage's output is written to the database and keyed by content hash. An interrupted job does not start over; if a prompt changes, only that stage re-runs. |
| K5 | **SQLite (WAL) + 30-day cache** | No setup, a single file. The YouTube API rule requires data to be kept at most 30 days. Storage sits behind an interface; if scale is needed, move to Postgres. |
| K6 | **Source adapters (`Source` interface)** | YouTube is the first adapter. Because the interface is fixed, Reddit, podcasts and forums can plug into the same pipeline later. |
| K7 | **Layered fallback chain for every data type** (see §4) | YouTube changes often; a system tied to one method breaks. If one method fails, the next takes over. |
| K8 | **Pluggable LLM backend: default `claude -p` (bare mode), optional Anthropic API** | Claude Code is installed; `claude -p` uses the user's own Claude login/billing, so no separate key management. The API and Batch API (half price) are supported for others. Calls are bare: custom system prompt, no tools, no MCP, no settings → per-call overhead dropped ~20x (measured: $0.0036 → $0.00018). Structured output via `--json-schema`. |
| K9 | **Model allocation** | Haiku 5.5 → bulk extraction (cheap, fast) · Sonnet 5.5 → verification · Opus 5.5 → final synthesis |
| K10 | **Code computes the confidence score; the LLM only provides labels** | Numbers given by an LLM are inconsistent. The LLM produces labels such as "supports / refutes / has conflict of interest"; the score comes from code via a log-odds rule. This makes the result reproducible and auditable. |
| K11 | **Quote verification** | Every quote the LLM returns is looked up in the transcript with fuzzy matching. A claim whose quote cannot be found is dropped; this is the main defense against fabricated quotes. |
| K12 | **Topic packs** | The core is topic-independent. Topic-specific knowledge (official source domains, glossary, date thresholds) lives in a YAML pack. First pack: `meta-ads`. |
| K13 | **Observed content is untrusted data** | Comment and page text goes to the LLM marked "data, not instructions". This is the defense against prompt injection. |
| K14 | **Claude in Chrome is only the last fallback** | The MCP server cannot call Chrome directly. For the few blocked pages it returns a `needs_browser` list and Claude Code reads them in the browser. It is not used for bulk YouTube work: slow, puts the account at risk, spends many tokens. |
| K15 | **Two-stage clustering: local embeddings → LLM arbitration** | In measurement, a small embedding model (bge-small, local, free) could not tell "same topic" from "same claim" (two opposing claims 0.775, two unrelated ones 0.757). So embeddings only build coarse topic blocks (≤30 claims); within a block, Haiku groups by "are they making the same point?". Opposing claims deliberately fall into the same cluster; the stance is decided by the verification stage. |
| K16 | **Audio: whole file through yt-dlp's native chunked downloader, original track only** | A ranged download (`download_ranges`) goes through ffmpeg, which YouTube throttles to near playback speed and which hung once with no timeout (13 MB: 6 s native vs 12+ min ranged). Many videos carry 20+ AI-dubbed tracks; only the original is taken. |
| K17 | **Whisper transcribes the whole video; coverage check** | The key part of a talk is often late. A cut-off audio file once gave 48 s of text for a 60-min talk: transcripts under 80% of the duration are re-fetched once. |
| K18 | **Claim budget scales with length** | A flat 25 claims gave a 59-min interview as many claims as an 11-min video. Budget = 25 up to ~31 min, then 0.8/min, max 50. |
| K19 | **Second clustering pass over group centroids** | A claim lands in exactly one embedding block, so the same point in other words could split across groups (one claim was split 4+4). Groups are blocked by centroid and the model joins those answering the same question. |
| K20 | **Company-level independence (`org_key`)** | Channels of one company counted as two sources and inflated scores. |
| K21 | **Mandatory official-docs lookup for every claim type but income stories, one forced retry** | Only mechanics were checked and the model skipped lookups on most clusters; "practice only" labels were therefore unproven. |
| K22 | **One research = one folder; two reports from one evidence base** | `research/<id>/`: `pack.yaml`, `plan.json`, `REPORT.md` public; `data/` and `private/` never committed. The public report is written from the topic; the private one adds the reader's question, context and decisions. Paid model text is saved (`report_body.md`) so links and the appendix re-render for free. |
| K24 | **Exemplar mode: measure what a channel does, then test rules against it** | Advice says what should work; a top channel's own videos show what is done. `mode: exemplar` + `channels` selects a channel's latest long-form uploads (the `UULF` playlist, no Shorts), measures cuts, speech rate and frames by code, and has the model describe packaging, opening, beats and language from the transcript, thumbnail and frames (quotes grounded). No clustering or verification; the report tests the reader's rules (hypotheses) against the videos. |
| K25 | **Images reach the model as content blocks, never through a tool** | Frames and thumbnails go over `claude -p` stream-json input as base64 image blocks, so analysis calls stay tool-free (K13). |
| K26 | **One Whisper per machine; low-priority runs yield** | Two runs on one GPU each ran ~2x slower and delayed the run on the critical path. A file lock serialises transcription across processes; `TUBEPROOF_WHISPER_PRIORITY=low` waits until no normal run has used Whisper for 90 s. |
| K23 | **English tool, per-pack report language** | Code, logs, prompts and docs are English. `report_lang` in the pack picks the report language; fixed report labels live in `i18n.py`; prompts load only through `prompts.load`. |

---

## 4. Data layer: primary method and fallback chain

| Data | Primary | Fallback 1 | Fallback 2 |
|---|---|---|---|
| Search (video + playlist) | innertube `sp` filters (keyless, popularity + date range) | API `search.list` (exact date, `order=viewCount`, 100/day) | — |
| Metadata (views, likes, date) | yt-dlp `--dump-json` | API `videos.list` (50 videos/unit) | — |
| Playlist / training set | yt-dlp `--flat-playlist` | API `playlistItems.list` | — |
| Transcript | youtube-transcript-api (original language) | yt-dlp `.*-orig` + Node JS runner | mlx-whisper (audio → text) |
| Comments | youtube-comment-downloader (top + newest, both) | API `commentThreads` | yt-dlp `--write-comments` |
| Description links | httpx + trafilatura; markitdown (PDF/DOCX) | Render with Playwright | `needs_browser` → Claude in Chrome |
| Sponsor / paid | "Paid promotion" marker on the page + link regex classifier | SponsorBlock (if reachable) | LLM segment labeling |

Common rules:
- Wait 3–5 seconds between YouTube requests; per-host rate limiter.
- Exponential backoff on 429.
- The yt-dlp version is pinned and updated regularly.

---

## 5. Pipeline

```
 TOPIC ──► [0] Gen queries ──► [1] Discover ──► [2] Rank/select ──► [3] Harvest
           (LLM, multilingual)  (innertube      (log views,         (transcript,
                                 + API)          views/day,          description,
                                                 engagement,         links,
                                                 channel diversity)  comments)
                                                                        │
 ┌──────────────────────────────────────────────────────────────────────┘
 ▼
 [4] Pre-filter (CODE) ──► [5] Map (Haiku)       ──► [6] Reduce
     link regex,            segment label,              normalize claims,
     paid marker,           claim extraction,           embed + cluster,
     spam comments,         promise → delivered?,       in-cluster contradiction (NLI),
     SponsorBlock           comment stance              merge non-independent ones
                                                              │
 ┌────────────────────────────────────────────────────────────┘
 ▼
 [7] Verify (Sonnet) ──► [8] Score (CODE) ──► [9] Synthesize (Opus) ──► REPORT
     mechanical claim →     log-odds rule,        consensus recipe,        .md / .html
       official doc         confidence band,      disputed claims,         + .json
     efficacy claim →       evidence volume       platform facts,          (every sentence
       evidence pack                              single-source claims,    linked to
                                                  discarded sales/hype     video + second)
```

### Claim types and how they are verified

| Type | Example | How verified |
|---|---|---|
| Platform mechanics | "The learning phase needs ~50 conversions in 7 days" | The official Meta document is fetched at run time and compared |
| Tactic efficacy | "On a low budget, broad targeting works better than interests" | Consensus of independent sources + comment evidence |
| Result / income | "I made $50k per month" | **Not verified.** Evidence is graded and a survivorship-bias flag is set |

### Sales-removal rule

Each transcript is split into 60–90 second segments and each segment is labeled:

`free_knowledge | sponsor | own_offer_pitch | lead_magnet | interaction | intro_outro | mixed`

**A `mixed` segment is never discarded:** the information in it is extracted, and the sales part is labeled.

Teasers that withhold information, such as "the rest is in my course", are flagged separately.

---

## 6. Confidence scoring rule (in code, versioned)

The computation is a sum of log-odds, then `confidence = sigmoid(total)`.

| Signal | Effect |
|---|---|
| Independent source supports, no conflict of interest, shows evidence on screen | +1.0 |
| Same, narrated only | +0.6 |
| Same, with a conflict of interest (sells a course/agency) | +0.3 |
| Independent source refutes | −0.7 / source |
| Comment describing concrete experience supports | +0.4 / comment (max +1.6) |
| Comment describing concrete experience refutes | −0.5 / comment (max −2.0; asymmetric because of deleted criticism) |
| Official document supports / refutes | +2.0 / −3.0 |
| Recency | Each term × 0.5^(age_months / 12); for a delivery claim from before Andromeda, additionally × 0.5 |
| Source video's clickbait score > 0.7 | That source's contribution × 0.7 |

**Bands:**
- ≥ 0.80 solid
- 0.60–0.80 likely
- 0.40–0.60 disputed
- < 0.40 doubtful

If the evidence volume is below 2, the **"single source"** label is applied whatever the score.

---

## 7. Cost

Estimated cost for 50 videos (Claude pricing page, 2026-10-27):

| Route | Cost |
|---|---|
| `claude -p` (your own subscription) | **No extra charge.** Subscription usage limits apply. |
| Anthropic API, standard | ≈ $15–20 |
| Anthropic API, Batch | ≈ $8–10 |

Most of the cost is in the verification stage. For this reason only clusters worth verifying are verified: those with at least 2 sources, or mechanical claims that can be checked against documentation.

---

## 8. Directory structure

```
tubeproof/
├── pyproject.toml
├── src/tubeproof/
│   ├── core/          # pipeline, stages, models (pydantic), scoring
│   ├── sources/
│   │   └── youtube/   # search, metadata, transcript, comments, playlist
│   ├── fetch/         # link resolving, trafilatura, linktree, markitdown, playwright
│   ├── filters/       # link regex, spam comments, paid marker, sponsorblock
│   ├── llm/           # backends: claude_cli, anthropic_api (+batch)
│   ├── store/         # SQLite cache, stage outputs
│   ├── packs/         # topic packs (meta-ads.yaml)
│   ├── prompts/       # versioned prompt files (embedded in the package)
│   ├── research.py    # research folder config → stage calls (shared by CLI and MCP)
│   ├── i18n.py        # report languages and fixed report labels
│   ├── cli.py         # Typer
│   └── mcp_server.py  # MCP server
├── research/<id>/     # pack.yaml · plan.json · REPORT.md (public) · data/ · private/ (never committed)
├── tests/
└── docs/              # ARCHITECTURE · PRINCIPLES · SSOT (registry) · STATUS
```

**MCP tools:**

| Tool | What it does |
|---|---|
| `research_topic` | Runs the full pipeline, returns a job ID |
| `research_status` | Shows which stage the job is in |
| `get_report` | Fetches the report |
| `search_videos` | Searches for videos |
| `get_video_bundle` | Returns transcript, description, links and comments together |
| `get_comments` | Returns comments |
| `query_claims` | Searches the clustered claims |

---

## 9. Legal and open-source rules

- The YouTube API key is taken **from the user**; a key is never put in the repo.
- The cache is kept at most 30 days (API policy).
- Raw transcripts and comments are **not redistributed**. The report consists of summaries and quotes.
- Comment authors' names are hashed by default.
- SponsorBlock data is licensed CC BY-NC-SA 4.0: attribution is given, no commercial use.
- The API route and the scraping route are separate backends; the user chooses which to use.
- License: **MIT**.

---

## 10. Risks

| Risk | Mitigation |
|---|---|
| If PO-tokens become widespread, the transcript library breaks | yt-dlp fallback + bgutil plugin + Whisper |
| YouTube silently changes search filters | `sp` codes live in a config file; tests warn when they break |
| Rate limit (429, ~300 videos/hour as a guest) | Waiting, cache, staged resume |
| LLM fabricated quotes | Verify the quote in the transcript with fuzzy matching |
| Prompt injection from comments and pages | Untrusted-data marking; tool-less LLM calls |
| Turkish channels repeating the same mentor | Independence group detection |

---

## 11. Roadmap

| Phase | Scope | Done when |
|---|---|---|
| **1** | Skeleton + data layer: discovery, ranking, harvest, pre-filter, SQLite, CLI | `tubeproof harvest "topic"` → the full package of 30+ videos lands on disk |
| **2** | Map stage (LLM backends, schemas, quote verification) | A verified `VideoExtraction` JSON for every video |
| **3** | Reduce + verification + scoring + synthesis | First confidence-scored report for the Meta topic |
| **4** | MCP server + topic pack system | `research_topic` works from inside Claude Code |
| **5** | Evaluation set (5 hand-labeled videos), README, GitHub release | Free-information retention rate ≥ 0.95 |

---

## 12. Measured values (v0.1, 2026-10-27)

| Measurement | Value |
|---|---|
| Map (Haiku): per video (transcript + comments) | ≈ $0.02 |
| 4-video end-to-end test (map + clustering + verification + synthesis) | $0.95 (verification $0.60, synthesis $0.28) |
| Fabricated quotes (not found in the transcript) | 0 / 72 across 4 videos |
| Whisper, 300 s of Turkish audio (M4) | faster-whisper medium CPU: 125 s (RTF 0.42) · mlx large-v3-turbo GPU: 24.5 s (RTF 0.08) → turbo is the default if it is in the cache |
| YouTube subtitle block (home IP) | Started after ~60 minutes of harvesting, lifted in about 1 hour; audio download was never affected |
| Spam filter false positive fixed | "WhatsApp" is a legitimate channel on this topic; only contact solicitations (link/number/"write to him") are flagged |
| Audio download, 36-min video (13 MB) | native chunked: 6 s · ranged via ffmpeg: 12+ min, one stall without end |
| Whisper mlx turbo at 1.5× tempo | ~2–4 min per 60-min video; 98–99% identical text to 1× |
| Claims, 35-video run | 752 claims → 561 clusters; 0 ungrounded quotes |
| Verification with mandatory doc lookup | ~50 s and ~$0.05 per cluster (Sonnet + WebSearch/WebFetch), 8 in parallel |
| Synthesis (Opus), ~300 KB digest | ~$1.7 per report |
| Plan-bundle harvest, exemplar (no comments/links) | ~3 s per video instead of ~30 s (comments 22 s, links 6 s skipped) |
| Whisper backlog, 2026-10-27 | RTF 0.076 (mlx turbo, 1.5×); 1366 min of audio ≈ 104 min of GPU |
| Exemplar, 43-min video at 360p picture | 118 MB, ffmpeg cut detection 38 s, 25 cuts/min; frames + thumbnail + Haiku analysis ≈ $0.005–0.02 per video |
| YouTube watch-page loads per exemplar video | was 3–4 (meta, paid-promotion check, yt-dlp subtitles, picture download, audio download); now 1: `metadata.extract` is reused by download and subtitles, one download carries picture + original audio, no paid-promotion check in exemplar mode, captions retried only where they were deferred. ~45 videos at the old rate tripped YouTube's IP bot check (`/watch` → 429 "sorry" page; search, browse and thumbnails kept working), 2026-10-27 |
| Visual changes (scene score > 0.02, merged within 1 s) | Code Aesthetic: 0 cuts/min but 2.2–10.9 changes/min; Kurzgesagt: 10–18 changes/min, ~3 s apart. Checked by eye on frames before/after |

## 13. CLI

```bash
tubeproof harvest <id> --plan               # select videos for research/<id>/ (pack.yaml) and save the plan
                                            # (exemplar packs: the channels' latest uploads; use --no-screen)
tubeproof process <id>                      # harvest the plan, transcribe, analyse, cluster, verify, write reports
tubeproof analyze|reduce|verify|report <id> # stages one by one; `report --render` re-renders for free
tubeproof stats <id>
```
