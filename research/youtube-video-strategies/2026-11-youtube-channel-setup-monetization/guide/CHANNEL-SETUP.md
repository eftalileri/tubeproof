# Setting up a new English-language educational YouTube channel: settings, discovery, dubbing and monetization

Checked: 2026-11-03. Re-check after 3–6 months; the Partner Program thresholds change on **2027-02-01**.

**Where this comes from.** One guide built on three independent sources:

1. **Practitioner videos.** The tubeproof run in this folder covers 30 videos from 27 channels and reduces them to 250 evidence clusters, each checked against YouTube's docs. Cited as [Kn](../REPORT.md).
2. **Official documentation.** YouTube Help, the YouTube blog and the YouTube Data API reference, cited by link. Every number in sections 1–6 comes from these pages.
3. **Open-source tooling on GitHub.** Surveyed read-only (nothing installed or run); star counts and last-push dates come from the GitHub API on the check date. Feature claims come from READMEs and are untested.

Where practitioners and the docs disagree, this guide follows the docs and says so. It assumes a long-form (10–20 min) faceless explainer channel aimed at English-speaking viewers, possibly with a second-language audio track, run by a creator who may live outside the US.

---

## 1. Where the money comes from (decide this first)

- **Viewer location sets the price of a view, not the creator's location.** Advertisers choose the countries they buy, so CPM "will vary by geography" ([answer/9314357](https://support.google.com/youtube/answer/9314357?hl=en)). Practitioners agree: US, UK, Canada, Australia and Western Europe pay many times more per view than lower-income markets [K4](../REPORT.md#k4). RPM also varies by topic and advertiser demand [K5](../REPORT.md#k5).
- **Country-level dollar figures are unreliable.** YouTube publishes no RPM by country, and most public tables copy each other. Treat the *ranking* (Australia, US, Canada, New Zealand, Switzerland, UK at the top) as solid and the exact dollars as noise.
- **Niche framing matters.** The best dataset found (AIR Media-Tech, Studio data from 300 channels, May 2025–May 2026, [air.io](https://air.io)) puts the Education & Science median RPM at about $10 vs about $2 for Gadgets & Tech. Ranking niches against each other is still **contested** in the video evidence [K32](../REPORT.md#k32), so read this as a direction, not a promise.
- **Long-form pays; Shorts discover.** Long-form earns tens of times more per view than Shorts [K15](../REPORT.md#k15) [K31](../REPORT.md#k31). On long-form watch-page ads the creator keeps 55% of net revenue; on Shorts, 45% of their Creator Pool allocation [K28](../REPORT.md#k28) ([answer/12504220](https://support.google.com/youtube/answer/12504220?hl=en)).
- **Off-platform income** (your own product, affiliates, sponsors) often exceeds AdSense on small channels, but the evidence is self-reported, often by sellers [K8](../REPORT.md#k8). Affiliate mechanics themselves are well supported [K233](../REPORT.md#k233).

**What this means in practice:** English narration, English on-screen text and English metadata are the biggest lever on revenue per view. Topics with business or developer-tool advertisers help too. Everything below supports those two choices.

---

## 2. Account and channel settings (one-time)

| Setting | Value | Why | Source |
|---|---|---|---|
| 2-step verification | On | Required for the Partner Program | [answer/72851](https://support.google.com/youtube/answer/72851?hl=en) |
| Feature eligibility → Intermediate | Phone verification, **now** | Unlocks videos **over 15 minutes**, custom thumbnails, live | [answer/9890437](https://support.google.com/youtube/answer/9890437?hl=en), [K12](../REPORT.md#k12) |
| Feature eligibility → Advanced | ID or video verification (or channel history) | Unlocks **multi-language audio**, Test & Compare, chapters, clickable description links, Shorts "Related video", pinned comments, monetization applications | [answer/9890437](https://support.google.com/youtube/answer/9890437?hl=en), [K63](../REPORT.md#k63) |
| Basic info → Country | **Your real country of residence** | Decides Partner Program eligibility, payments and tax. It does not set ad prices. A false country conflicts with payment and tax details. The practitioner claim "the country doesn't matter" is contradicted by the docs | [answer/2976814](https://support.google.com/youtube/answer/2976814?hl=en), [K172](../REPORT.md#k172) |
| Basic info → Keywords | A few honest niche terms, optional | YouTube says nothing about them helping discovery | [answer/2976814](https://support.google.com/youtube/answer/2976814?hl=en) |
| Advanced → Audience | **No, not made for kids** | "Made for kids" removes comments, end screens, cards, personalized ads and notifications | [K37](../REPORT.md#k37), [K41](../REPORT.md#k41) |
| Advanced → Advertisements | Personalized ads **on** | Turning it off "may reduce revenue" | [answer/2976814](https://support.google.com/youtube/answer/2976814?hl=en) |
| Advanced → Automatic dubbing | **On, "Publish manually"** | Lets you review AI dubs before they go live (section 4) | [answer/15569972](https://support.google.com/youtube/answer/15569972?hl=en) |
| Community → Comment moderation | **Basic**, plus a blocked-words list; hold comments with links | Spam control; changes apply to new videos only | [answer/9483359](https://support.google.com/youtube/answer/9483359?hl=en) |
| Branding | Watermark, banner, profile picture | — | [answer/3219384](https://support.google.com/youtube/answer/3219384?hl=en) |
| Home tab | Trailer for non-subscribers, featured video for returning viewers, up to 12 sections built from topic playlists | — | [answer/3027950](https://support.google.com/youtube/answer/3027950?hl=en) |

### Upload defaults (Settings → Upload defaults)

Defaults apply to browser uploads only [K142](../REPORT.md#k142) ([answer/2660027](https://support.google.com/youtube/answer/2660027)).

- Visibility: **Private**, then schedule each video
- Category: **Education**
- Video language and title/description language: **English**
- Caption certification: "This content has never aired on US television"
- Comments: on, moderation Basic
- Automatic chapters: allowed, but write your own (section 3)
- Mid-roll ads: tick once monetized ([answer/6175006](https://support.google.com/youtube/answer/6175006?hl=en))
- Tags: leave empty or add a few. Docs say tags "play a minimal role", mostly for misspellings ([answer/146402](https://support.google.com/youtube/answer/146402?hl=en)). The practitioner claim that tags are a main signal for new channels is **doubtful** [K44](../REPORT.md#k44).

Keep "Publish to subscriptions feed and notify subscribers" ticked; notifications are capped at about 3 per channel per 24 h [K45](../REPORT.md#k45).

---

## 3. Every video: discovery checklist

**What YouTube says it uses.** Viewing behaviour, likes and dislikes, subscriptions, satisfaction surveys, and channel quality ([howyoutubeworks](https://www.youtube.com/intl/en_us/howyoutubeworks/product-features/recommendations/)). Location settings are not used for recommendations ([answer/141805](https://support.google.com/youtube/answer/141805?hl=en)).

1. **Title and the first lines of the description** carry the real search terms, in plain language. Title ≤ 100 characters; description ≤ 5,000 bytes, where non-ASCII letters count 2 bytes ([Data API videos](https://developers.google.com/youtube/v3/docs/videos)).
2. **Keep the promise.** Restate the title/thumbnail promise in the opening seconds [K14](../REPORT.md#k14). Misleading packaging breaks spam policy and hurts satisfaction [K38](../REPORT.md#k38).
3. **Test & Compare.** Up to 3 titles and/or thumbnails. The winner is picked by **watch-time share, not click-through rate**. Results take days to 2 weeks, and editing during a test stops it ([answer/13861714](https://support.google.com/youtube/answer/13861714?hl=en), [K213](../REPORT.md#k213), [K33](../REPORT.md#k33)).
4. **Chapters.** First timestamp 00:00, at least 3, each at least 10 s ([answer/9884579](https://support.google.com/youtube/answer/9884579?hl=en)). Manual chapters override automatic ones [K22](../REPORT.md#k22). If the video is rendered from code (Remotion or similar), take chapters from the scene timings: exact and free.
5. **Hashtags.** Up to 3 show above the title; more than 60 and all are ignored ([answer/6390658](https://support.google.com/youtube/answer/6390658?hl=en), [K106](../REPORT.md#k106)).
6. **End screen.** Video ≥ 25 s, last 5–20 s, up to 4 elements ([answer/6388789](https://support.google.com/youtube/answer/6388789?hl=en)). Whether end screens and playlists raise growth has **no verified evidence** either way; they are cheap, so use them.
7. **Captions.** Speak clearly at a moderate pace and add English captions [K25](../REPORT.md#k25). If you have the script and timestamped TTS output, build captions from those instead of speech recognition.
8. **Age-restriction triggers.** Avoid them; age restriction cuts reach and ad eligibility [K102](../REPORT.md#k102).
9. **Publish time.** "Publish time is not known to impact a video's long-term performance", and growth "is not correlated with time between uploads" ([answer/141805](https://support.google.com/youtube/answer/141805?hl=en)). Publishing when your audience is awake helps only the first hours. For a US audience from UTC+3, mid-afternoon to early evening local time lands on the US morning. That is a reasonable default, not an evidence-backed lever.

**Keywords.** In the AI-coding niche (Google Trends, worldwide, 12 months to 2026-11-03), tool names beat buzzwords: "claude code" averaged 46 vs "vibe coding" at about 3 and flat. Put tool names and the viewer's problem ("…keeps breaking my app") in titles. Use concept words ("idempotency", "single source of truth") inside the video, where browse traffic finds them. Check your own niche the same way: Google Trends (YouTube search) plus the Analytics **Trends** tab. The Inspiration tab is being phased out for **Ask Studio** from August 2026 ([answer/15575509](https://support.google.com/youtube/answer/15575509?hl=en)).

---

## 4. Second languages: multi-language audio, auto-dubbing, translated metadata

**Your own second-language track**
- Needs Advanced features and desktop Studio: Languages → Add language → Add dub → upload ([answer/13338784](https://support.google.com/youtube/answer/13338784?hl=en)).
- The file must be audio-only and roughly the same length as the video. Thumbnails can be set per language. Analytics shows views and watch time by audio language.
- **The Data API cannot upload extra audio tracks.** The videos resource has no write field for it. Tools that drive Studio with a headless browser to work around this are fragile and use non-API access; avoid them.

**Auto-dubbing** ([answer/15569972](https://support.google.com/youtube/answer/15569972?hl=en))
- On by default for eligible creators. Skipped for videos over 120 minutes, with little or fast speech, or with copyrighted content [K216](../REPORT.md#k216) [K217](../REPORT.md#k217).
- **English → 20 languages:** Arabic, Bengali, Dutch, French, German, Hebrew, Hindi, Indonesian, Italian, Japanese, Korean, Malayalam, Polish, Portuguese, Punjabi, Russian, Spanish, Tamil, Telugu, Ukrainian.
- **Expressive speech:** English, French, German, Hindi, Indonesian, Italian, Portuguese, Spanish.
- **Not every language pair is supported.** Turkish, for example, can be dubbed *into* English but English cannot be dubbed into Turkish. If your second language is missing from the target list, your own uploaded track is the only way to offer it.
- Dubs can be previewed, published, unpublished or deleted per language, but not edited, and deleted dubs cannot be restored. If an auto-dub exists for a language, delete it before uploading your own track for that language.
- "Auto-dubbing applies to future uploads only" was true at launch; the docs now say older videos may be dubbed later [K218](../REPORT.md#k218).

**Translated title and description**
- Studio → Subtitles → Add language → Title & description ([answer/6289575](https://support.google.com/youtube/answer/6289575?hl=en)).
- Translated videos "can be found when viewers search using a translated video title and description" ([answer/4792576](https://support.google.com/youtube/answer/4792576?hl=en)). This is the documented search benefit of a second language.

**Does it pay?**
- YouTube reports "no negative impact on discovery" for auto-dubbing ([blog.youtube, 2026-05-15](https://blog.youtube/creator-and-artist-stories/youtube-auto-dubbing-explained/)).
- Practitioner evidence of extra views is small and single-channel (e.g. +87 views in one language in a month) [K115](../REPORT.md#k115) [K93](../REPORT.md#k93). "Double or triple reach" is one unsupported claim [K219](../REPORT.md#k219). Nothing measures whether main-language views fall.
- Views follow viewer location, so a track aimed at a lower-RPM market adds views and engagement but lowers the channel's average RPM.
- **Test it on your own data:** keep English the default language and metadata, then compare views by audio language and English views against comparable videos after 6–10 uploads.

---

## 5. Disclosures

- **AI voice clone of your own voice: no altered-content disclosure needed.** YouTube lists "Cloning one's own voice to create voice overs or dubs" among content creators don't have to disclose, as are animated or non-realistic visuals and AI help with scripts ([answer/14328491](https://support.google.com/youtube/answer/14328491?hl=en)). YouTube may still show a label on non-photorealistic AI content. The Data API field for this flag is `status.containsSyntheticMedia`.
- **Inauthentic content** (renamed from "repetitious content" on 2025-07-15): mass-produced, templated AI content that "lacks the creator's original insight" is not monetizable. AI used as a tool to visualise an original narrative is allowed. The test is originality, not AI use ([answer/1311392](https://support.google.com/youtube/answer/1311392?hl=en), [K24](../REPORT.md#k24)). The practical risk is near-identical template uploads, not your own cloned voice.
- **Promoting your own product.** "Endorsements" include content for "a creator's own brands" when the relationship is not clear ([answer/154235](https://support.google.com/youtube/answer/154235?hl=en)). Say "this is my own product" on screen and in the description, and tick the paid-promotion box if in doubt. Local advertising law may require more. Disclose every affiliate link and sponsorship.

---

## 6. Partner Program and payouts

| Tier | Today | From **2027-02-01** (new applicants) | Source |
|---|---|---|---|
| Ads and Premium revenue | 1,000 subscribers + **4,000** public long-form watch hours in 12 months, or 10M Shorts views in 90 days | 1,000 subscribers + **8,000** qualified watch hours in 365 days, or **20M** Shorts views in 90 days | [answer/72851](https://support.google.com/youtube/answer/72851?hl=en), [answer/12843009](https://support.google.com/youtube/answer/12843009?hl=en), [K3](../REPORT.md#k3) |
| Fan funding, Shopping (no ad revenue) | 500 subscribers + 3 uploads in 90 days + 3,000 hours or 3M Shorts views | Unchanged | [answer/13429240](https://support.google.com/youtube/answer/13429240?hl=en), [K177](../REPORT.md#k177) |
| Monthly Shorts Creator Pool earnings | Part of YPP | Needs **10M** qualified Shorts views in the last 90 days | [answer/12843009](https://support.google.com/youtube/answer/12843009?hl=en) |

- Shorts-feed watch hours **do not count** toward the long-form hours [K176](../REPORT.md#k176).
- Every tier also needs 2-step verification, one linked AdSense account, no active strikes, and Advanced features. Review takes about a month.
- **Mid-rolls:** videos of 8 minutes or more; placement automatic, manual or both; natural breaks serve better ([answer/6175006](https://support.google.com/youtube/answer/6175006?hl=en), [K30](../REPORT.md#k30), [K195](../REPORT.md#k195)). The retention cost of mid-rolls has no measurement in the evidence.
- **Payouts:** the threshold is about $100 or the local-currency equivalent [K181](../REPORT.md#k181). Your country's thresholds and methods are on [answer/14727140](https://support.google.com/youtube/answer/14727140?hl=en). The payment currency cannot be changed later. Balances settle on the 20th and pay out between the 21st and 26th.
- **US tax (creators outside the US)** ([answer/10391362](https://support.google.com/youtube/answer/10391362?hl=en)):
  - Submit a W-8BEN in AdSense (Payments → Payments info → Manage settings → United States tax info), **before monetization starts**.
  - With the form, only earnings from **US viewers** are withheld, at the treaty rate for your country. Without it, Google may withhold **24% of worldwide earnings**.
  - Forms expire after 3 full calendar years.
- **Link cards to external sites** are for Partner Program members only ([answer/6140493](https://support.google.com/youtube/answer/6140493?hl=en)). Before that, use description links (Advanced features) and pinned comments.
- **Speed.** Reports of joining the program range from 10 days to 6+ months, and the fast cases come mostly from course sellers [K1](../REPORT.md#k1). A new channel that cannot realistically reach 4,000 hours before 2027-02-01 should plan for 8,000.

---

## 7. Shorts

- Up to **3 minutes**, square or vertical, for uploads from 2024-10-15 ([answer/15424877](https://support.google.com/youtube/answer/15424877?hl=en)).
- Shorts reach new viewers; turning them into long-form viewers is often weak [K19](../REPORT.md#k19). One independent study found long-form views *fell* after a channel started Shorts ([arXiv 2402.18208](https://arxiv.org/html/2402.18208v1)).
- Set a **Related video** on every Short so viewers can tap to the long video; this needs Advanced features. URLs in Shorts descriptions are not clickable ([answer/14075157](https://support.google.com/youtube/answer/14075157?hl=en)).
- For animated content, render native 9:16 compositions from the same scenes rather than auto-cropping. The open-source "long video to Shorts" tools are built around face tracking.
- **Test it:** compare subscribers per Short vs per long video for 4 weeks. If Shorts bring subscribers but long-form views don't move, cut Shorts back to a minimal discovery role.

---

## 8. Upload specs

- **Video** ([answer/1722171](https://support.google.com/youtube/answer/1722171?hl=en)):
  - MP4, H.264 High Profile, closed GOP of half the frame rate, 4:2:0, BT.709
  - Upload at the frame rate the video was made at
  - SDR bitrates: 1080p30 = 8 Mbps, 1080p60 = 12 Mbps, 4K30 = 35–45 Mbps
- **Audio:** AAC-LC or Opus, **48 kHz** stereo at **384 kbps**. YouTube publishes no loudness target; −14 LUFS is widely quoted but unofficial.
- **Thumbnails:** 3840×2160 (16:9), JPG or PNG, up to **50 MB on desktop** and 2 MB on mobile ([answer/72431](https://support.google.com/youtube/answer/72431?hl=en)).
- **Tags:** 500 characters in total ([Data API videos](https://developers.google.com/youtube/v3/docs/videos)).

---

## 9. Open-source tools (surveyed, not installed)

**What the YouTube Data API v3 covers**
- **Through the API:** uploads (`videos.insert`), `defaultLanguage` / `defaultAudioLanguage`, `localizations` (translated titles and descriptions), captions, thumbnails, `publishAt` scheduling, playlists, `containsSyntheticMedia`.
- **Studio only:**
  - the extra audio track
  - per-language thumbnails
  - Test & Compare
  - views by audio language
  - end screens (assumed; not separately checked)

| Need | Recommended | Notes |
|---|---|---|
| Upload with full metadata | [googleapis/google-api-python-client](https://github.com/googleapis/google-api-python-client) (Apache-2.0) | Official client; a short script covers localizations, captions, scheduling and the disclosure flag |
| Ready-made upload CLI | [porjo/youtubeuploader](https://github.com/porjo/youtubeuploader) (Apache-2.0) | JSON metadata file with localizations, `publishAt`, captions, playlists. Stores its token in plain text |
| Claude Code / MCP access | [eat-pray-ai/yutu](https://github.com/eat-pray-ai/yutu) (Apache-2.0) | Covers most of the Data API and runs as an MCP server. Use it for reads, and for writes only with approval |
| Analytics | [parafoxia/analytix](https://github.com/parafoxia/analytix) (BSD-3) | Typed Python SDK for the Analytics API. Retention via `elapsedVideoTimeRatio` + `audienceWatchRatio` |
| Caption timing checks | [m-bain/whisperX](https://github.com/m-bain/whisperX) (BSD-2), [ggml-org/whisper.cpp](https://github.com/ggml-org/whisper.cpp) (MIT), [smacke/ffsubsync](https://github.com/smacke/ffsubsync) (MIT) | Word-level timestamps; drift fixes |

**Avoid**
- **View, subscriber and engagement bots, sub4sub tools.** The API policy bars automated engagement, and new repos with sudden stars are likely malware lures.
- **Autocomplete, search and transcript scrapers at volume, and several API projects to stretch quota.** The [developer policies](https://developers.google.com/youtube/terms/developer-policies) bar non-API retrieval and require one project per client.
- **Studio browser automation, and third-party upload relays that hold your YouTube access.**
- **One-line "pipe to shell" MCP installers.**
- **Unmaintained uploaders** such as tokland/youtube-upload.

**Google sign-in hygiene for your own uploader**
- One Cloud project.
- Only the `youtube.upload`, `youtube.force-ssl` and `yt-analytics.readonly` scopes.
- Move the OAuth consent screen out of "Testing", where refresh tokens expire after 7 days.
- Keep tokens in the OS keychain, and gitignore `client_secret*.json` and `*token*.json`.

**Growth tips repeated across GitHub knowledge-base repos** (title variants, a hook in the first 30 s, CTR benchmarks) cite third-party figures without a method. Test them on your own channel with Test & Compare rather than trusting the benchmarks.

---

## 10. Myths the evidence does not support

| Claim | Verdict | Cluster |
|---|---|---|
| Setting a US channel country raises RPM | Contradicted by docs. Viewer location decides RPM, and the country must be real | [K172](../REPORT.md#k172), [K4](../REPORT.md#k4) |
| Tags are a main ranking signal for new channels | Contradicted by docs | [K44](../REPORT.md#k44) |
| "Warm up" a new account with self-views or second accounts | Fake-engagement violation | [K16](../REPORT.md#k16) |
| New channels get a 90-day test period, or "the first video judges you" | Contradicted by the per-video framing in the docs | [K11](../REPORT.md#k11) |
| Holding uploads private for hours boosts reach | Unproven | [K20](../REPORT.md#k20) |
| Adding "AI" to titles doubles RPM | Unverifiable, likely misleading | [K46](../REPORT.md#k46) |

---

## 11. Measure on your own channel

1. **Partner Program pace (from video 1):** log subscribers and public long-form hours weekly and project the qualifying date against the 2027-02-01 change.
2. **RPM by country (28–90 days after monetization):** compare US/UK/CA/AU with everyone else, and topics with a similar country mix. Lean into the best RPM-weighted topics.
3. **Second-language tracks (after 6–10 videos):** views and watch time by audio language, and English views against comparable videos without the track.
4. **Shorts (4 weeks):** subscribers per Short vs per long video; long-form views from new subscribers.
5. **Off-platform income (90 days):** revenue by source and clicks per 1,000 views on one clear offer in your top videos.

Limits of the video evidence: 30 videos, with few from English educational channels and none in a faceless animated format with a cloned-voice track. Income figures are self-reported and survivorship-biased. No controlled data exists on dubbing cannibalisation, end screens, playlists or schedules.
