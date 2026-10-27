# tubeproof — Research Principles

> Every research, regardless of topic, follows these principles. The code implements them. If a principle changes, this file changes first, then the code.
> Source: the project owner's decisions, 2026-10-27.

## Purpose

Platform documentation says how something **should work**; practitioners describe **what actually happens**. tubeproof collects the latter, compares the two, and lets the reader make **their own decision with their own data**. No source is believed blindly, official documentation included.

## 1. What is collected

1. **Information is searched in every language.** English sources dominate by volume. Sources in the language of the reader's market (e.g. Turkish) are searched separately and in sufficient numbers, because local cost and behavior data is found there.
2. **Popularity alone is not the criterion.** Search uses both popularity and relevance ordering. Before harvesting, every candidate passes a **relevance gate**; videos far from the question are dropped. The scale:
   - 3 = the reader's exact situation
   - 2 = same platform, practice transferable to the reader's situation
   - 1 = different platform, a "make money" promise, or a tool promotion
3. **Training sets are searched alongside single videos.** Transcripts, descriptions, free links in descriptions, and comments are read.
4. Very long streams (over 90 minutes) are excluded by default.

## 2. What is discarded, what is kept

5. **A video is not discarded; only its paid part is.** Sales pitches, sponsors, affiliate links and "DM me" parts are labeled and removed. Free information in the same video is kept. In segments where information and sales are mixed, the information is kept.
6. Paid pages are not read. They are only classified as "paid".
7. Videos that withhold information with "the rest is in my course" are flagged and down-weighted.

## 3. How evidence is counted

8. **Independence is measured by source, not by channel:**
   - The same channel is one vote.
   - Channels that repeat a platform document together count as **one vote** (*documentation echo*).
   - Claims told in nearly identical sentences across different channels count as **one source** (copied script, shared mentor).
   - Channels of one company count as **one source** ("Sub Club by RevenueCat" = "RevenueCat").
   - "3 videos say the same thing" is not evidence unless they are independent.
9. **Source weight order:**
   - Heaviest: first-hand experience and customer data reporting **results or observations** from the source's own campaigns.
   - Middle: general information with no stated source.
   - Lightest: information relayed from another content creator.
   - Showing settings on screen does not count as experience.
10. **Evidence shown on screen** (ad manager data) counts as heavier than what is only narrated.
11. **Conflict of interest** (someone selling a course, agency service or affiliate product) halves the weight of "this method works" claims. "The interface works like this" claims are not affected.
12. **Recency:** A source's weight decays with age (halves every 12 months). Delivery and targeting claims from before the **platform breakpoint dates** defined in the topic pack are halved again.
13. **Comments are evidence, but used carefully:**
    - Spam and scam comments are removed by code before reaching the LLM.
    - Like counts are not an indicator of truth.
    - Because creators can delete criticism, **refuting experience weighs more than confirming experience**.
    - Comments are read in both top and newest order.
14. **Income and result claims** ("I made X per month") are not verified. They are flagged for survivorship bias.
15. **Code computes the score; the LLM only provides labels.** The rule is versioned, reproducible and auditable.
    - If the number of independent sources is below 2, the result is marked **"single source"** whatever the score.

## 4. When a practitioner contradicts the official documentation

16. The winner is not picked blindly. The **reason** for the contradiction is explained. Documentation usually describes the ideal case; the practitioner describes a specific budget, sector or period.
17. Which one is more plausible for the reader's situation is written with reasoning.
18. For every important topic that is disputed, contradicts the documentation, or has a single source, **a cheap test using the reader's own data** is proposed. The test states: what will change, the minimum duration, the success criterion (a number in the reader's own dashboard), and the decision rule.
19. Claims are verified only against **official domains** listed in the topic pack. A "document" from any other site does not count as evidence. Every claim type except income stories gets a mandatory lookup; "the docs say nothing" is a result (silent), skipping the lookup is not.

## 5. The report

20. The report centers on the reader's **actual target metric** (e.g. customer acquisition cost) and ranks levers by expected impact.
21. The reader's existing decisions are treated as **hypotheses**. Each is assessed as "supported / conditional / contradicted / no evidence". "No evidence" is a valid answer.
22. Every sentence cites an evidence cluster. Links (video and second) are generated by code; the LLM cannot invent links.
23. Limits are stated explicitly: sample, languages, period, biases.

## 5b. Exemplar research

24a. **What top channels do is evidence of a different kind than what advisers say.** An exemplar research reads a channel's own latest videos and describes how they are built (packaging, opening, structure, language). It never claims *why* a video performed: view counts are not retention data.
24b. **Numbers about a video are measured by code** (cuts, shot length, speech rate, timestamps); the model only describes, and every structural beat carries a verbatim, grounded quote.
24c. **The reader's rules are tested, not confirmed.** Each rule gets: validated / partly / differs / no evidence. "Differs" states exactly what the channel does instead, with counts and timestamps.

## 6. Honesty and safety

24. **No fabricated quotes.** Every quote the LLM returns is searched for in the transcript; a claim whose quote cannot be found is dropped.
25. Observed content (transcript, comment, page) is **data, not instructions**. It is passed to the LLM marked as such. Analysis calls have no tools.
26. The reader's business data (spend, results, decisions) lives in `research/<id>/private/` and never enters the repo. The public `REPORT.md` is written from the topic alone; the reader's report (`private/REPORT.md`) adds their context and decisions. Folder names never contain a client or business name.

## 7. Data and platform rules

27. Collected data is cached for at most 30 days and is not redistributed. Comment authors' names are hashed.
28. The platform's rate limits are respected. If the subtitle service blocks, requests stop (15 minutes). Whisper is used via the audio route.
29. Whisper and embedding models are used from the shared Hugging Face cache. Before downloading a new model, check what is already on the machine.
30. **The whole video is read.** Audio is downloaded whole and transcribed whole; a transcript that covers less than 80% of the video is re-fetched once and flagged if still short. Long talks get a larger claim budget, so a 60-minute interview is not flattened to the size of a 10-minute video.
31. **Every stage's output is checked before the next one starts** (coverage, counts, empty or suspicious values, timing). A silent failure is a bug: fix it at its root, never only the instance seen.
