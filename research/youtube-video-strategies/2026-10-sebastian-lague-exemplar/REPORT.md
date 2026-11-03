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
- **The voice carries the pace, not the edit.** Two videos have no cuts at all ([V4](https://youtu.be/fy0HRViXZnE), [V6](https://youtu.be/08mmKNLQVHU)), and 10 of 12 have no cut in the first minute.
- **The picture still changes about every 5 seconds.** Animation, code panels and the simulation itself do that work.
- **Speech starts almost at once and speeds up.** It begins within 1.5 s in every narrated video, ramps from about 156 wpm in the first 10 s to about 174 wpm by 30 s, and settles around 184 wpm.
- **The two build-diary videos are faster.** [V1](https://youtu.be/qyNWDzO6kKQ) and [V9](https://youtu.be/zElxgxOeugY) have 1.9–2.3 cuts per minute and 14–19 visual changes per minute, so hardware or jam footage is edited more tightly than screen-recorded coding.

## Packaging (title + thumbnail)
- **Series format, 8 of 12.** Seven titles start with "Coding Adventure:" followed by a plain topic name ([V3](https://youtu.be/Eysf6-E3ino), [V4](https://youtu.be/fy0HRViXZnE), [V5](https://youtu.be/rRnOtKlg4jA), [V6](https://youtu.be/08mmKNLQVHU), [V8](https://youtu.be/Q78wvrQ9xsU), [V10](https://youtu.be/wA1KVZ1eOuA), [V11](https://youtu.be/yyJ-hdISgnw)). [V2](https://youtu.be/_JGMgpyCTsY) puts the same series label in its thumbnail text even though its title is first-person. The thumbnail layout is the same in all eight: white "CODING ADVENTURE" on top and the topic in coral or salmon at the bottom. [V12](https://youtu.be/HGkuRp5HfH8) uses the same two-line layout with different words ("RANDOM ACCESS MEMORY / EXPLORING HOW COMPUTERS WORK"), so 9 of 12 have this text template.
- **First-person challenge titles, 3 of 12.** "I Made…" or "I Tried…" ([V1](https://youtu.be/qyNWDzO6kKQ), [V2](https://youtu.be/_JGMgpyCTsY), [V9](https://youtu.be/zElxgxOeugY)). Two of them ([V1](https://youtu.be/qyNWDzO6kKQ), [V9](https://youtu.be/zElxgxOeugY)) are the only thumbnails with no text.
- **Result-as-image, 12 of 12.** Every thumbnail shows the finished output: contour maps, a crowd of 3D models, cubes moving from scrambled to solved, a spectrogram, a smoke plume, a glass dragon, the boy and fox, a grid of memory blocks. No thumbnail shows the presenter's face. [V5](https://youtu.be/rRnOtKlg4jA) is the only one with a human hand on screen.
- **The curiosity gap is always "can plain code really produce this?"** For example: can sine waves sound like a piano [V5](https://youtu.be/rRnOtKlg4jA), can a short program crack quintillions of cube states [V4](https://youtu.be/fy0HRViXZnE), can you draw 3D with no GPU [V11](https://youtu.be/yyJ-hdISgnw). Two thumbnails add an unexplained oddity: a cat [V1](https://youtu.be/qyNWDzO6kKQ) and a whole family cast [V9](https://youtu.be/zElxgxOeugY).
- **Titles are plain, not hyped.** They read like project names, and the visual promise does the selling.

## The first 3, 10 and 30 seconds
- **0–3 s:**
  - "Hello everyone…" in 11 of 12 videos.
  - A low-poly sphere logo bumper in 8 ([V2](https://youtu.be/_JGMgpyCTsY), [V3](https://youtu.be/Eysf6-E3ino), [V4](https://youtu.be/fy0HRViXZnE), [V5](https://youtu.be/rRnOtKlg4jA), [V6](https://youtu.be/08mmKNLQVHU), [V8](https://youtu.be/Q78wvrQ9xsU), [V10](https://youtu.be/wA1KVZ1eOuA), [V11](https://youtu.be/yyJ-hdISgnw)). Other openings are a jam card [V9](https://youtu.be/zElxgxOeugY), a zoom into the simulator [V12](https://youtu.be/HGkuRp5HfH8), an untextured moon sphere [V1](https://youtu.be/qyNWDzO6kKQ), and smoke rising from black with no voice [V7](https://youtu.be/8BCdKJ4ObZ4).
  - No video shows any stakes in the first 3 seconds.
- **3–10 s:**
  - The series title card, then the goal in one plain sentence. "Today, I'd like to try and simulate some smoke." [V8 0:06](https://youtu.be/Q78wvrQ9xsU?t=6); "Today I'd like to build a little tool for analyzing audio." [V6 0:05](https://youtu.be/08mmKNLQVHU?t=5)
  - [V3 0:10](https://youtu.be/Eysf6-E3ino?t=10) is the exception that opens with a concrete flaw: about 8 seconds and 40 moves per solve, and "occasionally gets stuck".
- **10–30 s:**
  - A callback to an earlier episode or project in 8 videos ([V2](https://youtu.be/_JGMgpyCTsY), [V3](https://youtu.be/Eysf6-E3ino), [V5](https://youtu.be/rRnOtKlg4jA), [V6](https://youtu.be/08mmKNLQVHU), [V8](https://youtu.be/Q78wvrQ9xsU), [V10](https://youtu.be/wA1KVZ1eOuA), [V11](https://youtu.be/yyJ-hdISgnw), [V12](https://youtu.be/HGkuRp5HfH8)).
  - Then the first concept starts straight away, for example the shader code in [V1 0:20](https://youtu.be/qyNWDzO6kKQ?t=20), CFOP in [V3 0:23](https://youtu.be/Eysf6-E3ino?t=23) and sound as pressure waves in [V6 0:15](https://youtu.be/08mmKNLQVHU?t=15).
- **When the goal is stated:** 9 of the 11 narrated videos state it within 30 s. [V12](https://youtu.be/HGkuRp5HfH8) states it at 77 s, after a recap. [V1](https://youtu.be/qyNWDzO6kKQ) opens with "this is the moon", but the plotter plan only arrives at [V1 4:30](https://youtu.be/qyNWDzO6kKQ?t=270).
- **When the promise first appears (median 8 s):** this is almost always a spoken goal, not the thumbnail image. The opening frame matches the thumbnail in 0 of 12 videos.
- **When the promise is paid off (median about 1306 s, roughly 22 minutes):**
  - In 9 of 12 videos the recorded payoff lands at 56% or more of the runtime. Examples: the teapot at [V2 26:10](https://youtu.be/_JGMgpyCTsY?t=1570), the first smoke at [V8 27:06](https://youtu.be/Q78wvrQ9xsU?t=1626), the boy and fox at [V11 39:57](https://youtu.be/yyJ-hdISgnw?t=2397) and 256 bytes working at [V12 15:49](https://youtu.be/HGkuRp5HfH8?t=949).
  - Only [V6](https://youtu.be/08mmKNLQVHU) (the tool goal is met at 11 s) and [V7](https://youtu.be/8BCdKJ4ObZ4) (visual from 2 s) pay off early.
  - [V1](https://youtu.be/qyNWDzO6kKQ)'s recorded payoff at 25 s is the plan statement. Its beats put the finished white-ink moon plot at [V1 25:20](https://youtu.be/qyNWDzO6kKQ?t=1520).
- **Self-introduction:** he never says his name. Five videos have a series greeting ("welcome to another episode of Coding Adventures") within 3 s ([V2](https://youtu.be/_JGMgpyCTsY), [V6](https://youtu.be/08mmKNLQVHU), [V8](https://youtu.be/Q78wvrQ9xsU), [V10](https://youtu.be/wA1KVZ1eOuA), [V11](https://youtu.be/yyJ-hdISgnw)).

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

**Re-hook cadence:** in 10 of the 11 narrated videos a new stake arrives every 1–3 minutes; [V12](https://youtu.be/HGkuRp5HfH8) runs on 30–60 s micro-hooks between bigger stakes. The re-hooks are spoken, not edited.
- Failure lines: "Alright well that wasn't a huge success." [V8 18:20](https://youtu.be/Q78wvrQ9xsU?t=1100); "Oh, my computer died." [V10 5:18](https://youtu.be/wA1KVZ1eOuA?t=318)
- Reversals: the first greedy solve [V4 17:20](https://youtu.be/fy0HRViXZnE?t=1040) is followed by the reveal that it succeeds only 9.6% of the time [V4 17:40](https://youtu.be/fy0HRViXZnE?t=1060).
- Stats shortfalls: a 95% success rate [V3 14:20](https://youtu.be/Eysf6-E3ino?t=860); "256 bits is not super helpful" [V12 14:28](https://youtu.be/HGkuRp5HfH8?t=868).
- Comic stakes: a surprise inspection [V12 11:35](https://youtu.be/HGkuRp5HfH8?t=695).
- In [V9](https://youtu.be/zElxgxOeugY) the day chapters act as structural re-hooks every 4–5 minutes.

**Open loops:** each video runs several short loops that close within 1–5 minutes, plus one long loop (the title promise) that closes near the end. The long loops are:
- the bunny bugs [V2 14:50](https://youtu.be/_JGMgpyCTsY?t=890) → [V2 17:10](https://youtu.be/_JGMgpyCTsY?t=1030)
- the hidden cat [V1 0:00](https://youtu.be/qyNWDzO6kKQ?t=0) → [V1 19:20](https://youtu.be/qyNWDzO6kKQ?t=1160)
- the deadline [V9 0:00](https://youtu.be/zElxgxOeugY?t=0) → [V9 20:05](https://youtu.be/zElxgxOeugY?t=1205)

Most videos end with one or two loops deliberately left open, which point to a sequel (synchronization in [V2 27:05](https://youtu.be/_JGMgpyCTsY?t=1625), smoke conservation in [V8 28:10](https://youtu.be/Q78wvrQ9xsU?t=1690)).

**Sponsors and calls to action:**
- No sponsor read appears in any of the 12 videos.
- A closing request for suggestions or feedback appears in 8 ([V2](https://youtu.be/_JGMgpyCTsY), [V3](https://youtu.be/Eysf6-E3ino), [V4](https://youtu.be/fy0HRViXZnE), [V5](https://youtu.be/rRnOtKlg4jA), [V6](https://youtu.be/08mmKNLQVHU), [V8](https://youtu.be/Q78wvrQ9xsU), [V9](https://youtu.be/zElxgxOeugY), [V11](https://youtu.be/yyJ-hdISgnw)).
- Patreon thanks appear in [V1](https://youtu.be/qyNWDzO6kKQ) and [V12](https://youtu.be/HGkuRp5HfH8).
- The only mid-video call to action is a joke offering free cake to subscribers [V11 39:00](https://youtu.be/yyJ-hdISgnw?t=2340).
- [V7](https://youtu.be/8BCdKJ4ObZ4) and [V10](https://youtu.be/wA1KVZ1eOuA) have no call to action.

## How it teaches
11 of 12 videos teach; [V7](https://youtu.be/8BCdKJ4ObZ4) teaches nothing. The median is 12 concepts per teaching video (range 5–15).

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
- the string fixed at both ends [V5 18:50](https://youtu.be/rRnOtKlg4jA?t=1130)
- capacitors charged or empty [V12 7:10](https://youtu.be/HGkuRp5HfH8?t=430)
- "little points just moving around a unit circle" [V11 10:21](https://youtu.be/yyJ-hdISgnw?t=621)
- marching squares as "three-dimensional cousin" of marching cubes [V1 20:00](https://youtu.be/qyNWDzO6kKQ?t=1200)

**Usual order of moves:** problem or bug → demo or visual → plain-words explanation → technical name → code → test result. The name often comes after the picture: "This process is known as the short time Fourier transform by the way" [V6 3:55](https://youtu.be/08mmKNLQVHU?t=235); "These are called caustics, which is just a fancy term for…" [V10 22:55](https://youtu.be/wA1KVZ1eOuA?t=1375).

**Jargon and prior knowledge:**
- Terms are named in passing with a one-line gloss, or deferred ("I'll talk more about this another time" [V10](https://youtu.be/wA1KVZ1eOuA)).
- 5 videos assume earlier episodes ([V2](https://youtu.be/_JGMgpyCTsY), [V5](https://youtu.be/rRnOtKlg4jA), [V6](https://youtu.be/08mmKNLQVHU), [V10](https://youtu.be/wA1KVZ1eOuA), [V12](https://youtu.be/HGkuRp5HfH8)).
- Deeper theory is pointed to elsewhere: external course notes in [V8](https://youtu.be/Q78wvrQ9xsU), research terms in [V4](https://youtu.be/fy0HRViXZnE).

**Misconceptions:** explicitly corrected in 10 of 11 teaching videos. Examples:
- "You might think there should be 4096 entries" [V3 18:55](https://youtu.be/Eysf6-E3ino?t=1135)
- equal frequency steps do not sound even [V5 11:50](https://youtu.be/rRnOtKlg4jA?t=710)
- phase does matter, which is heard before it is explained [V6 17:05](https://youtu.be/08mmKNLQVHU?t=1025)
- clamping depth does not fix triangles behind the camera [V11](https://youtu.be/yyJ-hdISgnw)

**"Think first" moments:** all 11 teaching videos ask for a prediction before the answer. Examples:
- "I know what you're thinking though, why are these bunnies not attracted to one another gravitationally?" [V2 18:40](https://youtu.be/_JGMgpyCTsY?t=1120)
- guessing a random test phrase [V6 8:50](https://youtu.be/08mmKNLQVHU?t=530)
- counting moves aloud to 11 against a depth limit of 8 [V3 3:40](https://youtu.be/Eysf6-E3ino?t=220)

**The hardest part** is handled in one of four ways:
- **Shown failing first:** naive advection explodes [V8 18:10](https://youtu.be/Q78wvrQ9xsU?t=1090); two shortcuts fail before near-plane clipping [V11 41:50](https://youtu.be/yyJ-hdISgnw?t=2510).
- **Taken to extremes:** one sample per segment vs 48,000 [V6 7:50](https://youtu.be/08mmKNLQVHU?t=470).
- **Moved to 2D or a physical object:** a 2D ray tracer plus a glass globe [V10 17:20](https://youtu.be/wA1KVZ1eOuA?t=1040); a real cube [V4 21:10](https://youtu.be/fy0HRViXZnE?t=1270).
- **Admitted openly:** "My understanding of all the synchronization stuff is a little questionable" [V2](https://youtu.be/_JGMgpyCTsY).

**Recaps** are weak:
- Spoken summaries of what was achieved appear in [V2](https://youtu.be/_JGMgpyCTsY), [V3](https://youtu.be/Eysf6-E3ino), [V4](https://youtu.be/fy0HRViXZnE) and [V12](https://youtu.be/HGkuRp5HfH8). [V12 24:37](https://youtu.be/HGkuRp5HfH8?t=1477) also does a visual zoom-out from chip to latch, and [V5](https://youtu.be/rRnOtKlg4jA) shows a zoomed-out view of all the widgets.
- [V1](https://youtu.be/qyNWDzO6kKQ), [V6](https://youtu.be/08mmKNLQVHU) and [V10](https://youtu.be/wA1KVZ1eOuA) have none.
- [V8](https://youtu.be/Q78wvrQ9xsU) and [V11](https://youtu.be/yyJ-hdISgnw) list the remaining work instead.

**Story:** no outside real-world case carries the teaching. The story is always the creator's own debug log, where each bug motivates the next concept ([V11](https://youtu.be/yyJ-hdISgnw), [V8](https://youtu.be/Q78wvrQ9xsU), [V3](https://youtu.be/Eysf6-E3ino)). [V9](https://youtu.be/zElxgxOeugY) is the most story-like: a four-day jam diary with a family cast. Recurring test objects act as anchors: the bunny [V2](https://youtu.be/_JGMgpyCTsY), "punctual thunderstorm" [V6](https://youtu.be/08mmKNLQVHU), the dragon [V10](https://youtu.be/wA1KVZ1eOuA).

## Script language
**Tone:** calm, conversational, self-deprecating, and openly unsure ("I have pretty much no idea how this works" [V8](https://youtu.be/Q78wvrQ9xsU)). Excitement is kept small and saved for payoffs.

**Techniques:**
- "Okay," / "Alright," at the start of almost every new step.
- An inclusive "let's" and "we" that makes the viewer a co-builder.
- Concrete numbers as stakes (9.6%, 2 GB, 100,000 bunnies).
- Deadpan undercutting of expectations.
- Mistakes narrated live.

**Sentence shape:** long, chained explanations (median 27 words) closed by a short verdict line.

Example lines:
- "Wait, did that actually work? I was not expecting that." [V4 17:20](https://youtu.be/fy0HRViXZnE?t=1040)
- "The real trick is searching less." [V3 16:25](https://youtu.be/Eysf6-E3ino?t=985)
- "we have maximum precision about the frequencies, but have tragically lost our sense of time." [V6 7:50](https://youtu.be/08mmKNLQVHU?t=470)
- "let's test first and think later." [V8 23:18](https://youtu.be/Q78wvrQ9xsU?t=1398)
- "Okay, let's run it again, and this time we get... perfection." [V11](https://youtu.be/yyJ-hdISgnw)
- "Oh, my computer died." [V10 5:18](https://youtu.be/wA1KVZ1eOuA?t=318)

## Limits
- **Sample:** one channel and its latest 12 uploads, one of which (V7) is a silent art piece with no narration. These are not general rules for YouTube.
- **What is reliable:** cuts, visual changes, speech rates and timings were measured by code.
- **What is a model's reading:** beats, re-hooks, promise and payoff times, concept lists and vehicle labels were described by a model from transcripts, thumbnails and sampled frames. Some of these are approximate. For example, V1's recorded payoff time is the plan statement rather than the finished plot, and V12's frame timing drifts from the narration.
- **No retention data:** YouTube does not publish retention, so nothing here shows that these techniques actually hold viewers. They are only patterns in successful videos.
- **Date:** this reflects the channel as of 2026-11-03.

---

## Measurements per video

Computed by code from the 360p picture and the transcript: cuts = ffmpeg scene changes, wpm = words per minute. Speech rate is approximate for auto-transcribed audio.

| # | Video | Views | Cuts/min | Cuts 0-3 s | Cuts 0-10 s | Cuts 0-30 s | Median shot (s) | Changes/min | Changes 0-30 s | Median change gap (s) | WPM | WPM 0-10 s | WPM 0-30 s | First word (s) |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V1 | [I Made a Pen Plotter to Draw Maps of the Moon](https://youtu.be/qyNWDzO6kKQ) | 637740 | 1.9 | 0 | 0 | 0 | 8.8 | 13.8 | 4 | 2.07 | 173.9 | 192.0 | 212.0 | 0.0 |
| V2 | [I Tried Coding my own Graphics Library](https://youtu.be/_JGMgpyCTsY) | 466209 | 0.1 | 0 | 0 | 0 | 117.67 | 5.8 | 5 | 6.37 | 194.1 | 156.0 | 190.0 | 0.0 |
| V3 | [Coding Adventure: Improving my Rubik's Cube Solver](https://youtu.be/Eysf6-E3ino) | 190411 | 0.2 | 0 | 0 | 0 | 212.08 | 6.7 | 2 | 4.4 | 187.7 | 168.0 | 174.0 | 0.5 |
| V4 | [Coding Adventure: Rubik's Cube](https://youtu.be/fy0HRViXZnE) | 355871 | 0.0 | 0 | 0 | 0 | 1461.0 | 5.2 | 5 | 3.53 | 182.6 | 156.0 | 174.0 | 0.4 |
| V5 | [Coding Adventure: Additive Synthesis](https://youtu.be/rRnOtKlg4jA) | 363797 | 0.1 | 0 | 0 | 0 | 165.7 | 4.2 | 2 | 6.13 | 156.5 | 150.0 | 172.0 | 0.7 |
| V6 | [Coding Adventure: Analyzing Audio](https://youtu.be/08mmKNLQVHU) | 360182 | 0.0 | 0 | 0 | 0 | 1287.0 | 3.2 | 2 | 8.57 | 176.1 | 156.0 | 162.0 | 0.1 |
| V7 | [Bad Apple!! but it's a smoke simulation](https://youtu.be/8BCdKJ4ObZ4) | 164996 | 0.3 | 0 | 0 | 0 | 115.0 | 7.0 | 4 | 6.37 | 1.3 | 0.0 | 2.0 | 0.0 |
| V8 | [Coding Adventure: Simulating Smoke](https://youtu.be/Q78wvrQ9xsU) | 675470 | 0.1 | 0 | 0 | 0 | 488.7 | 4.4 | 1 | 5.7 | 193.0 | 144.0 | 186.0 | 0.0 |
| V9 | [I Made a Game in 4 Days (for the GMTK jam)](https://youtu.be/zElxgxOeugY) | 199449 | 2.3 | 0 | 0 | 1 | 12.9 | 18.8 | 7 | 1.5 | 194.5 | 192.0 | 208.0 | 0.0 |
| V10 | [Coding Adventure: Ray-Tracing Glass](https://youtu.be/wA1KVZ1eOuA) | 327754 | 0.4 | 0 | 0 | 0 | 2.63 | 5.8 | 3 | 5.23 | 192.6 | 144.0 | 172.0 | 1.5 |
| V11 | [Coding Adventure: Software Rasterizer](https://youtu.be/yyJ-hdISgnw) | 639227 | 0.4 | 0 | 0 | 0 | 5.73 | 6.7 | 1 | 1.5 | 184.1 | 156.0 | 170.0 | 1.3 |
| V12 | [Simulating 256 Bytes of RAM](https://youtu.be/HGkuRp5HfH8) | 490572 | 0.5 | 0 | 0 | 0 | 11.37 | 5.6 | 2 | 3.57 | 170.4 | 162.0 | 164.0 | 1.2 |
| | **Median** | | 0.2 | 0.0 | 0.0 | 0.0 | 116.3 | 5.8 | 2.5 | 4.8 | 183.3 | 156.0 | 173.0 | 0.2 |
