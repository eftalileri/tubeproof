# Sebastian Lague: slow cuts, fast talk, and a chain of bugs

## Short answer
The channel wins the click by showing the finished result in the thumbnail with no face: the glass dragon, the curling smoke plume, the boy and the fox. It mostly uses a fixed "CODING ADVENTURE / topic" text format. The videos never open on that result. 11 of 12 start with "Hello everyone" over a logo bumper or a recap, and the image from the thumbnail usually arrives in the last third of the video. What keeps viewers watching is a build log. Every 1–3 minutes something breaks, gets diagnosed and gets fixed, and each fix teaches one concept and ends in a visible result or a stats card. The editing is almost cut-free, and the narration runs at about 184 words per minute. The pattern is very consistent across the 11 narrated videos. The outlier is V7, a silent, music-only smoke render.

## Measured pattern
| Metric | Median | Range |
|---|---|---|
| Cuts per minute | 0.25 | 0.0 – 2.3 |
| Cuts in first 3 s | 0 | 0 – 0 |
| Cuts in first 10 s | 0 | 0 – 0 |
| Cuts in first 30 s | 0 | 0 – 1 (only V9) |
| Median shot length (s) | 116.3 | 2.6 – 1461 |
| Visual changes per minute | 5.8 | 3.2 – 18.8 |
| Median gap between visual changes (s) | 4.8 | 1.5 – 8.6 |
| Visual changes in first 30 s | 2.5 | 1 – 7 |
| Words per minute, overall (11 narrated videos) | 184.1 | 156.5 – 194.5 |
| Words per minute, first 10 s (11 narrated) | 156 | 144 – 192 |
| Words per minute, first 30 s (11 narrated) | 174 | 162 – 212 |
| First speech (s, 11 narrated) | 0.4 | 0.0 – 1.5 |
| Median sentence length (words, 11 narrated) | 27 | 21 – 32 |

V7 is silent apart from background music (1.3 wpm), so it is left out of the speech rows.

What the numbers mean:
- **The voice carries the pace, not the edit.** Two videos have no cuts at all ([V4], [V6]), and 10 of 12 have no cut in the first minute.
- **The picture still changes about every 5 seconds.** Animation, code panels and the simulation itself do that work.
- **Speech starts almost at once and speeds up.** It begins within 1.5 s in every narrated video, ramps from about 156 wpm in the first 10 s to about 174 wpm by 30 s, and settles around 184 wpm.
- **The two build-diary videos are faster.** [V1] and [V9] have 1.9–2.3 cuts per minute and 14–19 visual changes per minute, so hardware or jam footage is edited more tightly than screen-recorded coding.

## Packaging (title + thumbnail)
- **Series format, 8 of 12.** Seven titles start with "Coding Adventure:" followed by a plain topic name ([V3], [V4], [V5], [V6], [V8], [V10], [V11]). [V2] puts the same series label in its thumbnail text even though its title is first-person. The thumbnail layout is the same in all eight: white "CODING ADVENTURE" on top and the topic in coral or salmon at the bottom. [V12] uses the same two-line layout with different words ("RANDOM ACCESS MEMORY / EXPLORING HOW COMPUTERS WORK"), so 9 of 12 have this text template.
- **First-person challenge titles, 3 of 12.** "I Made…" or "I Tried…" ([V1], [V2], [V9]). Two of them ([V1], [V9]) are the only thumbnails with no text.
- **Result-as-image, 12 of 12.** Every thumbnail shows the finished output: contour maps, a crowd of 3D models, cubes moving from scrambled to solved, a spectrogram, a smoke plume, a glass dragon, the boy and fox, a grid of memory blocks. No thumbnail shows the presenter's face. [V5] is the only one with a human hand on screen.
- **The curiosity gap is always "can plain code really produce this?"** For example: can sine waves sound like a piano [V5], can a short program crack quintillions of cube states [V4], can you draw 3D with no GPU [V11]. Two thumbnails add an unexplained oddity: a cat [V1] and a whole family cast [V9].
- **Titles are plain, not hyped.** They read like project names, and the visual promise does the selling.

## The first 3, 10 and 30 seconds
- **0–3 s:**
  - "Hello everyone…" in 11 of 12 videos.
  - A low-poly sphere logo bumper in 8 ([V2], [V3], [V4], [V5], [V6], [V8], [V10], [V11]). Other openings are a jam card [V9], a zoom into the simulator [V12], an untextured moon sphere [V1], and smoke rising from black with no voice [V7].
  - No video shows any stakes in the first 3 seconds.
- **3–10 s:**
  - The series title card, then the goal in one plain sentence. "Today, I'd like to try and simulate some smoke." [V8 6s]; "Today I'd like to build a little tool for analyzing audio." [V6 5s]
  - [V3 10s] is the exception that opens with a concrete flaw: about 8 seconds and 40 moves per solve, and "occasionally gets stuck".
- **10–30 s:**
  - A callback to an earlier episode or project in 8 videos ([V2], [V3], [V5], [V6], [V8], [V10], [V11], [V12]).
  - Then the first concept starts straight away, for example the shader code in [V1 20s], CFOP in [V3 23s] and sound as pressure waves in [V6 15s].
- **When the goal is stated:** 9 of the 11 narrated videos state it within 30 s. [V12] states it at 77 s, after a recap. [V1] opens with "this is the moon", but the plotter plan only arrives at [V1 270s].
- **When the promise first appears (median 8 s):** this is almost always a spoken goal, not the thumbnail image. The opening frame matches the thumbnail in 0 of 12 videos.
- **When the promise is paid off (median about 1306 s, roughly 22 minutes):**
  - In 9 of 12 videos the recorded payoff lands at 56% or more of the runtime. Examples: the teapot at [V2 1570s], the first smoke at [V8 1626s], the boy and fox at [V11 2397s] and 256 bytes working at [V12 949s].
  - Only [V6] (the tool goal is met at 11 s) and [V7] (visual from 2 s) pay off early.
  - [V1]'s recorded payoff at 25 s is the plan statement. Its beats put the finished white-ink moon plot at [V1 1520s].
- **Self-introduction:** he never says his name. Five videos have a series greeting ("welcome to another episode of Coding Adventures") within 3 s ([V2], [V6], [V8], [V10], [V11]).

## Structure and re-hooks
**Common beat sequence (11 narrated videos):**
1. Greeting, then the goal.
2. Recap of earlier work.
3. The first build step.
4. A visible failure or bug, then diagnosis, then the fix plus the concept behind it.
5. A milestone payoff: a first image or a stats card.
6. A new, harder target, and the cycle repeats.
7. The final payoff that matches the thumbnail.
8. A list of what is still unsolved.
9. A request for suggestions.

**Re-hook cadence:** in 10 of the 11 narrated videos a new stake arrives every 1–3 minutes; [V12] runs on 30–60 s micro-hooks between bigger stakes. The re-hooks are spoken, not edited.
- Failure lines: "Alright well that wasn't a huge success." [V8 1100s]; "Oh, my computer died." [V10 318s]
- Reversals: the first greedy solve [V4 1040s] is followed by the reveal that it succeeds only 9.6% of the time [V4 1060s].
- Stats shortfalls: a 95% success rate [V3 860s]; "256 bits is not super helpful" [V12 868s].
- Comic stakes: a surprise inspection [V12 695s].
- In [V9] the day chapters act as structural re-hooks every 4–5 minutes.

**Open loops:** each video runs several short loops that close within 1–5 minutes, plus one long loop (the title promise) that closes near the end. The long loops are:
- the bunny bugs [V2 890s] → [V2 1030s]
- the hidden cat [V1 0s] → [V1 1160s]
- the deadline [V9 0s] → [V9 1205s]

Most videos end with one or two loops deliberately left open, which point to a sequel (synchronization in [V2 1625s], smoke conservation in [V8 1690s]).

**Sponsors and calls to action:**
- No sponsor read appears in any of the 12 videos.
- A closing request for suggestions or feedback appears in 8 ([V2], [V3], [V4], [V5], [V6], [V8], [V9], [V11]).
- Patreon thanks appear in [V1] and [V12].
- The only mid-video call to action is a joke offering free cake to subscribers [V11 2340s].
- [V7] and [V10] have no call to action.

## How it teaches
11 of 12 videos teach; [V7] teaches nothing. The median is 12 concepts per teaching video (range 5–15).

**Vehicles (121 concepts in total):**

| Vehicle | Concepts |
|---|---|
| Definition | 32 |
| Visual | 26 |
| Demo | 26 |
| Worked example | 23 |
| Analogy | 8 |
| Story | 4 |
| Misconception as the vehicle | 2 |

Analogies are rare but placed on the hardest physics or math, for example:
- the string fixed at both ends [V5 1130s]
- capacitors charged or empty [V12 430s]
- "little points just moving around a unit circle" [V11 621s]
- marching squares as "three-dimensional cousin" of marching cubes [V1 1200s]

**Usual order of moves:** problem or bug → demo or visual → plain-words explanation → technical name → code → test result. The name often comes after the picture: "This process is known as the short time Fourier transform by the way" [V6 235s]; "These are called caustics, which is just a fancy term for…" [V10 1375s].

**Jargon and prior knowledge:**
- Terms are named in passing with a one-line gloss, or deferred ("I'll talk more about this another time" [V10]).
- 5 videos assume earlier episodes ([V2], [V5], [V6], [V10], [V12]).
- Deeper theory is pointed to elsewhere: external course notes in [V8], research terms in [V4].

**Misconceptions:** explicitly corrected in 10 of 11 teaching videos. Examples:
- "You might think there should be 4096 entries" [V3 1135s]
- equal frequency steps do not sound even [V5 710s]
- phase does matter, which is heard before it is explained [V6 1025s]
- clamping depth does not fix triangles behind the camera [V11]

**"Think first" moments:** all 11 teaching videos ask for a prediction before the answer. Examples:
- "I know what you're thinking though, why are these bunnies not attracted to one another gravitationally?" [V2 1120s]
- guessing a random test phrase [V6 530s]
- counting moves aloud to 11 against a depth limit of 8 [V3 220s]

**The hardest part** is handled in one of four ways:
- **Shown failing first:** naive advection explodes [V8 1090s]; two shortcuts fail before near-plane clipping [V11 2510s].
- **Taken to extremes:** one sample per segment vs 48,000 [V6 470s].
- **Moved to 2D or a physical object:** a 2D ray tracer plus a glass globe [V10 1040s]; a real cube [V4 1270s].
- **Admitted openly:** "My understanding of all the synchronization stuff is a little questionable" [V2].

**Recaps** are weak:
- Spoken summaries of what was achieved appear in [V2], [V3], [V4] and [V12]. [V12 1477s] also does a visual zoom-out from chip to latch, and [V5] shows a zoomed-out view of all the widgets.
- [V1], [V6] and [V10] have none.
- [V8] and [V11] list the remaining work instead.

**Story:** no outside real-world case carries the teaching. The story is always the creator's own debug log, where each bug motivates the next concept ([V11], [V8], [V3]). [V9] is the most story-like: a four-day jam diary with a family cast. Recurring test objects act as anchors: the bunny [V2], "punctual thunderstorm" [V6], the dragon [V10].

## Script language
**Tone:** calm, conversational, self-deprecating, and openly unsure ("I have pretty much no idea how this works" [V8]). Excitement is kept small and saved for payoffs.

**Techniques:**
- "Okay," / "Alright," at the start of almost every new step.
- An inclusive "let's" and "we" that makes the viewer a co-builder.
- Concrete numbers as stakes (9.6%, 2 GB, 100,000 bunnies).
- Deadpan undercutting of expectations.
- Mistakes narrated live.

**Sentence shape:** long, chained explanations (median 27 words) closed by a short verdict line.

Example lines:
- "Wait, did that actually work? I was not expecting that." [V4 1040s]
- "The real trick is searching less." [V3 985s]
- "we have maximum precision about the frequencies, but have tragically lost our sense of time." [V6 470s]
- "let's test first and think later." [V8 1398s]
- "Okay, let's run it again, and this time we get... perfection." [V11]
- "Oh, my computer died." [V10 318s]

## Limits
- **Sample:** one channel and its latest 12 uploads, one of which (V7) is a silent art piece with no narration. These are not general rules for YouTube.
- **What is reliable:** cuts, visual changes, speech rates and timings were measured by code.
- **What is a model's reading:** beats, re-hooks, promise and payoff times, concept lists and vehicle labels were described by a model from transcripts, thumbnails and sampled frames. Some of these are approximate. For example, V1's recorded payoff time is the plan statement rather than the finished plot, and V12's frame timing drifts from the narration.
- **No retention data:** YouTube does not publish retention, so nothing here shows that these techniques actually hold viewers. They are only patterns in successful videos.
- **Date:** this reflects the channel as of 2026-11-03.