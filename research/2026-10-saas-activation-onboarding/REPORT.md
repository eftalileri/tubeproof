# Getting mobile B2B SaaS and subscription app users to their first "aha" moment: what 30 videos support

## Short answer
The evidence supports a few directional rules. Define your activation event for your own product. Cut or defer every sign-up step that doesn't lead to that event. Use a short 2–4 question survey only if the answers change what the user sees. Never leave a new user on a blank screen. Frame onboarding around the outcome the user wants, not a list of features [K11](#k11) [K8](#k8) [K5](#k5) [K2](#k2) [K23](#k23) [K15](#k15) [K30](#k30). These points are "well supported" only in the sense that several independent creators and vendor guidance (Appcues, Userpilot, ProductLed) agree. Almost none of them show data, and most sell agency services, courses or tools.

The corpus leans heavily toward consumer mobile paywalls. Much of the "likely" material is about paywall placement, trial timelines and CTA copy, not B2B activation [K1](#k1) [K3](#k3) [K6](#k6) [K18](#k18). There is almost no usable evidence on activation emails, push or WhatsApp sequences, or day-one return. What exists is single-source and unverified [K216](#k216) [K217](#k217) [K219](#k219) [K73](#k73), and nothing at all covers WhatsApp. Treat this report as a list of hypotheses to test on your own funnel, not as proven results.

## What the platform says vs what practitioners report
No cluster has practitioners contradicting the docs (`practice_contradicts_docs`). Where the two diverge, it is because the docs are silent and only practitioners speak (`practice_only`).

| Topic | Platform / docs | Practitioners (first-hand) | When each one applies | Clusters |
|---|---|---|---|---|
| What activation means | Not checked against docs | It's the first real value, defined per product. Some describe a single key action, others a process that ends in a habit | Every product; how fine-grained depends on product type | [K11](#k11) |
| Trial timeline on the paywall | Silent | Show the reminder and charge dates and make the trial visible. Some creators hide the trial length instead, which commenters object to | Consumer apps with a paywall and a card-required trial | [K1](#k1) [K10](#k10) |
| Paywall placement | Silent | At the end of onboarding, not at install. Commenters prefer after the aha moment for new or sensitive apps | Consumer subscription apps; weaker fit for B2B | [K3](#k3) [K42](#k42) |
| CTA copy | Silent | Specific trial or benefit wording beats generic. One single-source item says "Continue" won on iOS | Paywalls with a real trial; "free" on a no-trial option risks App Store rejection | [K18](#k18) [K243](#k243) [K97](#k97) |
| When "more onboarding" isn't the fix | Silent | If activated users still churn, look at the product, price or fit | Products whose activation is already measured | [K40](#k40) |
| Onboarding length | Silent on length | Length only earns its place through personalisation or filtering buyers. Second-hand comments say long flows won A/B tests | Long quizzes in consumer paywall apps vs. B2B where time-to-value dominates | [K14](#k14) |
| Freemium vs trial for complex B2B | Silent | Freemium suits network-effect or simple apps; complex B2B often doesn't gain from it | B2B with delayed time-to-value | [K44](#k44) |
| Sample size for tests | No number given | Hundreds to thousands of users per variant; low-traffic apps should test bold changes | Any onboarding test | [K181](#k181) [K27](#k27) |

Where docs and practice **agree**: delaying non-essential fields and account creation until after value or trial start [K5](#k5). Vendor guidance also backs short tailoring surveys [K2](#k2), value before sign-up [K43](#k43), cutting fields [K8](#k8), outcome-led framing [K15](#k15), guided empty states [K23](#k23), fast time-to-value [K30](#k30) and role-based personalisation [K41](#k41). For those, practitioners contribute only general-knowledge opinion with no first-hand data (`docs_only`).

## Levers
Ranked by expected impact on "install/sign-up → first valuable action".

1. **Shorten the path to the first valuable action.** Map every step from the first touchpoint to the aha moment and remove anything that doesn't move the user toward it. Defer phone, company and account fields until after first value [K8](#k8) [K5](#k5) [K157](#k157) [K367](#k367).
   - Expected effect: higher sign-up completion and activation.
   - Evidence: well supported in direction; no shown effect sizes.
2. **Measure time-to-value and set your own target.** The direction (faster value, less early churn) is supported. The "7-minute limit" has no source. Userpilot cites about 1.5 days on average and under 5 minutes for top performers [K30](#k30).
   - Evidence: well supported in direction; the number is unsupported.
3. **Short goal/role survey that changes the path.** Ask 2–4 questions and route users to different templates or checklists based on the answers [K2](#k2) [K41](#k41).
   - Expected effect: plausible activation gains, but only if the answers actually change the experience.
   - Evidence: well supported as a practice. The only first-hand case is a consumer app using a survey to prime the paywall.
4. **Guided empty states.** Never leave a blank screen. The empty state should lead directly into the first action, through pre-filled sample data, a sandbox or a button placed where the copy points [K23](#k23) [K213](#k213) [K117](#k117).
   - Evidence: well supported in direction. The [K213](#k213) and [K117](#k117) details are single-source.
5. **Show value before sign-up or paywall** where the product can do so without the user's own data [K43](#k43). This is a weaker fit for B2B tools that need integrations or data.
   - Evidence: well supported, with conditions.
6. **Outcome-led framing** in welcome screens and checklists, not feature tours [K15](#k15).
   - Evidence: well supported consensus, no data.
7. **For apps with a paywall: place it after onboarding and value, and make the trial transparent** [K3](#k3) [K6](#k6) [K42](#k42) [K1](#k1) [K18](#k18).
   - Expected effect: mainly on trial starts, not on activation.
   - Evidence: likely or contested; consumer-app sources.
8. **Lifecycle messaging during the trial** (push/email triggered on trial events, reminders before the trial ends) [K217](#k217) [K216](#k216) [K219](#k219) [K73](#k73).
   - Evidence: single-source or unverifiable only. The reported lifts (about 7% trial-to-paid; a Duolingo lift) are not verified. No WhatsApp evidence exists in this corpus.

## Practical recipe
1. Define one activation event for your product, for example "first appointment created". Write down why it represents real value for the user [K11](#k11).
2. Measure your baseline: the share of sign-ups reaching that event, and the time to reach it, over the last 60–90 days. Segment by time-to-first-key-action (<5 min, 5–30 min, >30 min, >1 day) and compare day-30 retention or trial-to-paid. The point where retention drops is your time-to-value target. Don't adopt "7 minutes" [K30](#k30).
3. Strip sign-up to the fields needed for personalisation or for delivering first value. Move phone, company details and similar fields to after the first key action or trial start. Spread the remaining asks out over time [K8](#k8) [K5](#k5).
4. Add a 2–4 question welcome survey (role, goal, use case) only where each answer changes the checklist, templates or first screen [K2](#k2) [K41](#k41).
5. Replace every blank first screen with guidance: one clear next step that leads to the activation event [K23](#k23).
6. Write welcome screens and checklist items as outcomes ("get your first booking"), not features [K15](#k15).
7. If the core output can be shown without user data, let users see it before account creation [K43](#k43).
8. If you have a paywall, place it at the end of onboarding or after the first value moment, not right at install [K3](#k3) [K6](#k6). Show a clear trial timeline (reminder date, charge date) [K1](#k1). Use a CTA that states the actual offer, and never say "free" on an option with no trial [K18](#k18).
9. If your iOS paywall uses an "enable free trial" toggle, remove it. Vendors report App Review rejections since early 2026 [K21](#k21).
10. If traffic is low (around 10 users a day), test whole-screen or multi-element changes, not button colours [K27](#k27). Set up the base placements and record baseline stats before running many experiments [K17](#k17).

## How to proceed: validate with your own data
Run these in order. Each test uses your own funnel.

1. **Find your own time-to-value threshold** [K30 test](#k30). This is analysis only, no product change: about a day of work on 60–90 days of cohorts. Metric: day-30 retention or trial-to-paid by time-to-first-key-action bucket. Decision rule: the bucket where retention drops sharply becomes your target. Every later test aims to move users into faster buckets.
2. **Check whether your problem is activation or the product** [K40 test](#k40). Compare trial-to-paid and 30-day retention for activated vs. non-activated users over one full trial cycle. If activated users still churn heavily, fix the product, price or fit before you touch onboarding.
3. **Size your tests before running them** [K181 test](#k181). Enter your baseline step conversion and the smallest lift worth detecting (95% confidence, 80% power) into a sample-size calculator. If a test can't finish within 4–6 weeks at your sign-up volume, test a bigger change [K27](#k27) or use interviews instead. [K78](#k78) (single-source) suggests at least five user interviews before changing activation.
4. **Shorter vs. longer onboarding** [K14 test](#k14). Compare your current flow with a trimmed 3–5 step version for at least 2 weeks. Metrics: first valuable action rate, trial-to-paid and day-7 retention, not sign-up completion alone. Keep the longer flow only if it wins on activation or paid conversion.
5. **Welcome survey that changes the checklist** [K2 test](#k2). Random split for 2–4 weeks, or a few hundred sign-ups per arm. Metrics: percentage reaching the key action within 7 days, and trial-to-paid. Keep the survey only if activation rises; a higher sign-up rate alone isn't enough.
6. **Checklist vs. current onboarding** [K39 test](#k39). Mural's reported lift varies between sources (about 30% vs. 10% relative), so test it yourself. Randomise for 2–4 weeks. Metrics: days 1–7 return and activation rate.
7. **Paywall after aha vs. at end of onboarding** (only if you paywall) [K3 test](#k3) [K42 test](#k42). 2–4 weeks, or about 1,000 installs per arm. Metrics: trial start per install, trial-to-paid, day-1/day-7 retention. Choose the arm with higher revenue per install, not the one with more trial starts.
8. **Trial reminders by channel** [K219 test](#k219). Over at least 2 trial cycles, compare trial-to-paid for users who received a push reminder vs. email only. Remember that push reaches only users who opted in.

## Contested and conditional points
- **Onboarding length.** Creators say length must be earned by personalisation [K14](#k14). Second-hand comments cite long flows winning tests, and Cal AI (about 20 steps) is cited as a success [K22](#k22). The split likely comes from the metric: consumer paywall conversion vs. activation and user experience. It also depends on the sector: finance and health intake is longer [K8](#k8) [K187](#k187).
- **Survey purpose.** Consumer creators value the survey as commitment priming before the paywall. SaaS sources value it as routing users to value [K2](#k2).
- **Paywall timing.** "Most conversions happen on day zero" (RevenueCat consumer data repeated second-hand: about 50% of conversions, 82% of starts) [K4](#k4) argues for an early paywall. Comments and [K42](#k42) argue for after the aha moment. B2B products with setup time are not represented.
- **One change at a time vs. bold multi-element tests.** Single-variable tests give clean attribution [K20](#k20). Low traffic forces bolder tests [K27](#k27) [K13](#k13). Both hold; the choice depends on your volume.
- **Plan and trial structure** (trial only on yearly, weekly vs. annual, default plan) [K7](#k7) [K36](#k36) [K37](#k37) [K12](#k12). Results depend on category and app type, for example one-time-use AI apps. This is mostly off-topic for activation.
- **Hard paywall vs. freemium** [K19](#k19) [K32](#k32) [K44](#k44). The roughly 5x download-to-paid gap is correlational, and refunds are higher on the hard-paywall side.
- **Activation benchmarks.** The "20–30% typical, 40% world-class" claim [K245](#k245) is contradicted by Userpilot's B2B benchmark (average about 37.5%). Definitions vary too much to compare across companies.
- **Trial-to-paid "good" rates.** About 30% is good for card-required trials. For no-card B2B trials the median is roughly 8% [K264](#k264) [K148](#k148).

## Platform facts
- **Apple review of trial toggles:** paywalls with an "enable free trial" toggle have been rejected since around January 2026 under Guideline 3.1.2. The source is paywall vendors' reports, not an Apple announcement [K21](#k21). Comments add: show the billed price more prominently than any per-week breakdown, and re-check compliance on every release.
- **Push needs opt-in** on iOS and Android 13+, so push-only trial reminders miss part of your users [K219](#k219).
- **Day-0 cancellations:** about 55% of cancellations on 3-day trials happen on day 0. This is RevenueCat data via secondary coverage; longer trials show a lower share. It is not a figure for all cancellations [K26](#k26).
- **Day-zero skew:** trial starts in consumer subscription apps cluster heavily on install day: 82% per RevenueCat, about 89% per Adapty [K4](#k4). This is not established for B2B.
- **Superwall** lets you change and A/B test paywalls remotely without an app update (single-source, product feature) [K326](#k326). Its onboarding-flow testing [K327](#k327) and Bayesian reporting [K328](#k328) are unverified.
- **Contradicted by docs:** the activation benchmark range in [K245](#k245).

## Single-source but notable
All of these are unconfirmed and come from one source each.
- Mural (B2B): UI fixes to the invite flow added about 3% more invitations but didn't help when the account creator wasn't convinced by their first board [K149](#k149) [K74](#k74). Onboarding optimisation focused first on the account creator [K153](#k153). A Slack connection correlated with retention, but probably as an effect of engagement, not a cause [K147](#k147).
- Mural: a discount email and a no-discount benefits-reminder email both beat no email; the discount did not beat the reminder [K73](#k73).
- Mural: a cluster of onboarding and billing flow changes roughly doubled paid conversion in one quarter [K151](#k151). Letting trial owners pay for fewer seats than they had invited helped conversion [K150](#k150).
- Give new users a minimum viable setup, not the power-user setup [K367](#k367). Keep checklists visible after the user dismisses the tour [K341](#k341).
- Session recordings (PostHog) show where users get stuck; making whole table rows clickable was a major churn fix for one extension [K205](#k205) [K204](#k204).
- Measure drop-off at each onboarding screen and fix the worst ones [K344](#k344).
- OneSignal journeys on trial-started, trial-cancelled and trial-converted events; the reported lift of about 7% in trial-to-paid is unverified [K217](#k217) [K216](#k216).
- A founder-signed email after trial cancellation, asking for the reason, got a 51% open rate [K372](#k372).
- A custom screen before the OS notification prompt is said to raise opt-in [K354](#k354).
- Moving the paywall before sign-up in a fitness app raised paywall views from 40% to 94% [K272](#k272). Asking for an app review during onboarding can backfire with one-star reviews [K345](#k345).
- B2B services: charging an implementation fee filtered out customers unwilling to do the work [K47](#k47) [K62](#k62).
- Vertical examples (appointment software): GlossGenius asks about business type, team size and weekly appointments before the dashboard, then shows a 3-step checklist that starts with the booking page [K250](#k250) [K251](#k251). Vagaro's recommended first-day setup is profile → services → payments [K66](#k66) [K357](#k357). These are vendor descriptions, not evidence that they work.

## From the comments
These tips are unverified.
- Judge a walkthrough by whether users complete the first key action, not by whether they watched the tour.
- Ask personalisation questions in context, when the user reaches the feature that needs the answer, rather than in a long quiz up front.
- Offer a skip button. Show the interface before forcing sign-up or a paywall.
- Work backwards from the user's first win when designing the path.
- Only use "processing" screens if they do real setup work.
- Track failed-card charges at trial end and add billing retries and dunning emails.
- Measure day-35 cohorts, not only day-0 trial starts.
- Segment test results by traffic source, and check that the ad's promise matches what the onboarding delivers.
- Don't put "Free" on a button when payment follows; say "Start 7-day trial, then $X".

## Filtered out: sales, hype, unverifiable
- **Offers seen:** agency services (paywall and onboarding optimisation, UX design, done-for-you MRR growth, app audits), courses and academies, paid communities and accelerators, coaching, and affiliate or sponsored tools (paywall platforms, interactive-demo software, design libraries, booking software). Several of the strongest-sounding tactics come from these sellers. In one case, the full OneSignal push and email templates are sold in a paid community [K91](#k91), so the method can't be inspected.
- **Unverifiable outcome claims:** multi-fold lifts in install-to-paid conversion [K9](#k9); a reported jump from 8% to 15–20% in paywall conversion, which is a vendor claim [K60](#k60); churn falling from 16% to 6% [K87](#k87); MRR tripling [K142](#k142); doubled activation after a redesign [K85](#k85); 119% sign-up growth [K96](#k96); app revenue figures (Cal AI, Yazio, Lose It) [K64](#k64) [K350](#k350) [K246](#k246) [K247](#k247). Third-party revenue estimates are imprecise anyway [K38](#k38).
- **Vendor statistics:** the "18.7x revenue for apps running 50+ experiments" figure is correlational [K304](#k304). "Up to 80% leave due to bad onboarding" has no source [K346](#k346). The Blinkist +23% figure traces back to one second-hand story [K10](#k10).

## Limits
- The sample is 30 videos from 23 channels, mostly English-language, and dominated by consumer mobile paywall content. B2B mobile activation, in-product guides, activation email, push and especially WhatsApp sequences are barely covered or not covered at all.
- Almost no cluster shows measured data on screen. "Well supported" means agreement plus vendor guidance, not proven effect sizes.
- There is survivorship and incentive bias: creators showcase wins, and most sell services tied to the advice.
- Vendor "docs" (Appcues, Userpilot) are themselves marketing-adjacent.
- This reflects the videos available on 2026-11-03. App Store policy, such as the trial-toggle rejections, and tooling change quickly, so re-run this research in 3–6 months.


---

## Evidence appendix

Source videos and the moment each claim is made, for every cluster the report cites. Band and confidence are computed by code (rubric `r3`).


### <a id="k1"></a>K1 · likely · confidence 0.73

Showing a clear trial timeline (when the reminder comes and when the charge happens) and making the free trial visible on the paywall or a pre-paywall screen builds trust and improves trial starts.


*Assessment:* Five members recommend a transparent trial timeline, but they are mostly general knowledge or repeats of other creators, with no shown conversion data. Several have conflicts of interest (agency, sponsor). The Superwall member's tactic of hiding the trial length on the product card is a different, more manipulative move, and a commenter objects to it. The allowed official docs say nothing specific about paywall trial timelines, so the label is conditional and rests on practice.


*Test with your own data:* A/B test the paywall with and without a trial-timeline screen (reminder and charge dates stated). Run it for at least 2 weeks, or about 1,000 paywall views per arm. Compare trial-start rate, trial-to-paid rate and refund/cancellation complaints.


- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=2982) @49:42 · RevenueCat · 2026-09-09 · *supports* · basis: general knowledge
  > How your trial works, the full timeline will be better than this one.

- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=220) @3:40 · Tim Gabe · 2026-05-18 · *supports* · basis: other creator · conflict of interest: sells agency services
  > Cal AI told the user exactly when they would be charged and explicitly promised to send a reminder before the trial ended.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=297) @4:57 · Steven Cravotta · 2026-05-29 · *supports* · basis: other creator · conflict of interest: sells agency services, paid community
  > They would show users a timeline of exactly what happens during their trial

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=1692) @28:12 · notJust․dev · 2026-02-06 · *supports* · basis: general knowledge · conflict of interest: affiliate, sponsored
  > In two days, we will remind you before your trial ends so you're safe.

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=812) @13:32 · Superwall · 2025-11-16 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > Just removing the time constraint from here and be like, don't worry about the time, just focus on the fact this is free.

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=1563) @26:03 · RevenueCat · 2026-09-09 · *supports* · basis: own experience
  > Please do the big, really visible seven days free pages, like free trial communication pages on the products.

### <a id="k2"></a>K2 · well supported · confidence 0.95

Asking new users a few questions about their goal, role, use case or experience during sign-up, and tailoring onboarding to the answers, improves activation or conversion.


*Assessment:* Most members agree that onboarding questions plus tailoring is a standard practice, and Appcues describes welcome surveys as the most common personalization mechanism. However, none show data. The only first-hand member (Cravotta) is a consumer app that used a long survey before a paywall. Two consumer-app members and a comment say the survey mainly primes commitment and raises trial conversion, not activation. So the benefit depends on whether the answers actually change the experience.


*Test with your own data:* A/B test, with random split, a 2–3 question welcome survey that changes the first-run checklist against a generic flow. Run it for at least 2–4 weeks, or until each arm has a few hundred sign-ups. Compare the percent reaching the first key action within 7 days and the trial-to-paid rate.


- Official source: [https://appcues.com/blog/personalizing-user-onboarding](https://appcues.com/blog/personalizing-user-onboarding) — “Welcome surveys and role-selection screens are the most common mechanism.”

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=594) @9:54 · Steven Cravotta · 2026-05-29 · *qualifies* · basis: own experience · conflict of interest: sells agency services, paid community
  > we customized their experience using a long survey, we targeted the pain that the users were feeling in the survey

- [I made a Claude Skill that builds app onboarding](https://youtu.be/at94PruxNdo?t=0) @0:00 · Adam Lyttle · 2026-04-08 · *qualifies* · basis: general knowledge
  > The new way is questionnaires. But not any type of questions, ones that are designed to make you feel something.

- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=296) @4:56 · Adam Lyttle · 2025-08-08 · *qualifies* · basis: general knowledge
  > Then the user asks how often they work out.

- [The Product-Led Growth Playbook for SaaS Startups (Navattic Case Study](https://youtu.be/sO2x9Nbggg4?t=307) @5:07 · Andrew Capland · 2026-10-06 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > what we have learned in marketing and in sales is that segmentation tends to lead to higher conversion rates.

- [Onboarding Best Practices from 200+ Top Apps!](https://youtu.be/vAN7kmpTdy4?t=149) @2:29 · Elizabeth Alli - DesignerUp · 2025-02-26 · *supports* · basis: general knowledge · conflict of interest: sells a course, affiliate
  > use or for school so you're self-identifying with the type of use case

- [SaaS Onboarding Best Practices: 6 UX Tips](https://youtu.be/meQvQesO-zE?t=79) @1:19 · Eleken · 2026-09-23 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Ask a few useful questions at signup. What's their role? What are they trying to accomplish? How experienced are they?

### <a id="k3"></a>K3 · likely · confidence 0.71

In a mobile subscription app, the paywall should be shown at the end of onboarding (after the user has spent some time and built trust) rather than instantly after install or much later.


*Assessment:* Most members converge on putting the paywall after onboarding rather than instantly at install, but no member has verified data. They are verbal estimates, repeated claims from creators who sell agency services or courses, or general knowledge. Mobbin's 22% figure shows that many apps do something different, and comments describe a trial-first flow, a very long quiz funnel, and sensitive or new apps where a hard paywall hurts. Official docs from the allowed domains say nothing on paywall placement, so the claim is best treated as a conditional heuristic.


*Test with your own data:* A/B test the paywall at the end of onboarding against the paywall after the first value action (the aha moment). Run it for at least 2 to 4 weeks, with enough installs per arm. Measure trial start rate per install, trial-to-paid conversion, and day-1 retention.


- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=538) @8:58 · RevenueCat · 2026-09-09 · *supports* · basis: own experience
  > And after onboarding flow, you can add your paywall.

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=538) @8:58 · RevenueCat · 2026-09-09 · *qualifies* · basis: general knowledge
  > average sum will be like around 80% of people from onboarding flow will see your paywall.

- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=71) @1:11 · App Masters · 2026-08-18 · *supports* · basis: other creator · conflict of interest: sells agency services, sells a course, sponsored
  > Across all categories, users who do not try immediately rarely try at all.

- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=220) @3:40 · Mobbin · 2026-04-16 · *qualifies* · basis: own experience
  > out of 900-plus apps and websites, 22%

- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=465) @7:45 · Steven Cravotta · 2026-03-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > They're going to pay at a much lower rate than they would if they already spent time in your app.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=594) @9:54 · Steven Cravotta · 2026-05-29 · *supports* · basis: other creator · conflict of interest: sells agency services, paid community
  > If you show the hard paywall instantly before building any trust with the users, it will feel like a demand, not a simple next step.

### <a id="k4"></a>K4 · likely · confidence 0.65

Most subscription app trial starts and paid conversions happen on day zero (install day), so the paywall or upgrade offer should be shown in the first session during onboarding.


*Assessment:* All members repeat RevenueCat's State of Subscription App data second-hand, so they are not independent. The percentages differ (50% of conversions, 82% of starts, "nearly all"). The 82% figure for trial starts matches what the search surfaced from RevenueCat, and Adapty reports about 89%, so a strong day-zero skew is plausible for consumer subscription apps. The 50% and 82% figures measure different things (conversions versus starts). None of the allowed docs address it, and no member is first-hand. The data comes from consumer apps and doesn't establish that a B2B SaaS app should paywall at install, where activation and the aha moment often come first.


*Test with your own data:* A/B test showing the paywall or trial offer at the end of onboarding against showing it after the first aha action. Run it for 2–4 weeks on new installs. Compare trial starts, paid conversion at day 30, and day-7 retention.


- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=223) @3:43 · Steven Cravotta · 2026-05-29 · *qualifies* · basis: other creator · conflict of interest: sells agency services, paid community
  > 50% of all app conversions happen on day zero, the first day that someone has your app downloaded.

- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=76) @1:16 · Nik Zechner · 2026-03-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > How they do it is they trigger this screen already in the onboarding.

- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=76) @1:16 · Nik Zechner · 2026-03-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > there is some data that some of the people actually upgrade on day one without even trying.

- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=146) @2:26 · Tim Gabe · 2026-05-18 · *qualifies* · basis: other creator · conflict of interest: sells agency services
  > 82% of all starts happen on the day a user installs the app, according to RevenueCat.

- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=71) @1:11 · App Masters · 2026-08-18 · *supports* · basis: other creator · conflict of interest: sells agency services, sells a course, sponsored
  > Nearly all trial starts happen on day zero, literally the day they open the app.

### <a id="k5"></a>K5 · well supported · confidence 0.93

In onboarding, defer requests for non-essential information (phone, email, company details, account sign-up) until after users have reached value or started the trial, and spread out the remaining asks instead of requesting everything at signup.


*Assessment:* All four members point the same way, and Appcues material on gradual engagement agrees that registration should be postponed until users have seen value. However, the evidence is verbal and generic, and the creators have conflicts of interest (sponsorship, affiliates, agency). C26 is narrower: it asks for sign-up right after the paywall, which suits paywalled mobile subscription apps and not every product. C15 is first-hand but concerns B2B services and gives no data on the 2–3 day spacing.


*Test with your own data:* A/B test moving the phone/company fields (or account creation) from signup to after the first key action or trial start. Run it for at least 2–4 weeks and compare signup completion, activation rate (first valuable action) and day-7 retention.


- Official source: [https://www.appcues.com/blog/gradual-engagement-mobile-app-first-screen](https://www.appcues.com/blog/gradual-engagement-mobile-app-first-screen) — “Gradual engagement involves postponing registration for as long as possible”

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=4214) @1:10:14 · notJust․dev · 2026-02-06 · *qualifies* · basis: general knowledge · conflict of interest: affiliate, sponsored
  > but not in the onboarding flow, right after, when the paywall, when the trial is activated.

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=1159) @19:19 · notJust․dev · 2026-02-06 · *supports* · basis: general knowledge · conflict of interest: affiliate, sponsored
  > if you simply ask for the mobile phone in order to have the mobile phone in case they drop off, people are going to be pissed off.

- [SaaS Onboarding Best Practices: 6 UX Tips](https://youtu.be/meQvQesO-zE?t=0) @0:00 · Eleken · 2026-09-23 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > If a step doesn't help users experience value, consider moving it later.

- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3203) @53:23 · Practical Founders - with Greg Head · 2026-04-23 · *supports* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > after they complete this task and give us this information, let's give them two or three days.

### <a id="k6"></a>K6 · likely · confidence 0.70

For mobile subscription apps, onboarding and the paywall work as one conversion system: most paid conversions come at the onboarding paywall, and the earlier product experience shapes whether users pay. So optimising the paywall alone gives only minor gains.


*Assessment:* All four members point the same way, but they are general opinion or experience with no data shown. Two creators sell agency, community or sponsored services, and one of the claims is only repeated founder advice (the 80% figure). The Mobbin comments add some independent experiential support, such as people who never subscribed when the paywall came before the product. Others note that demand and price can matter more than design. The Userpilot FTUE page only illustrates value-before-paywall with Headspace and says nothing quantitative about paywall conversion share.


*Test with your own data:* Run an A/B test with a baseline versus a change to one onboarding step before the paywall, such as a personalised result screen or a first-value moment, with the paywall unchanged. Run it for about 2 weeks or 1,000+ users per arm. Compare trial-start rate per install. Also check what share of your trial starts come from the onboarding paywall versus later paywalls.


- Official source: [https://userpilot.com/blog/first-time-user-experience-saas/](https://userpilot.com/blog/first-time-user-experience-saas/) — “Headspace delivers a complete introductory meditation session to every new user before presenting a subscription option.”

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=445) @7:25 · Superwall · 2025-11-16 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > First you optimize your onboarding payroll where you get like probably most of your conversions

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=148) @2:28 · Superwall · 2025-11-16 · *qualifies* · basis: other creator · conflict of interest: sells agency services, paid community
  > 80% of the effort that you put into building your app should go to onboarding and payw wall

- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=0) @0:00 · Mobbin · 2026-07-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > users sometimes decide to pay before they even see the paywall.

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=77) @1:17 · notJust․dev · 2026-02-06 · *supports* · basis: own experience · conflict of interest: affiliate, sponsored
  > in my opinion, onboarding flow and paywall are the same thing together. And only focusing on the paywall will only lead to minor results.

### <a id="k7"></a>K7 · contested · confidence 0.56

Offering a free trial only on the yearly plan (not on the cheaper monthly/weekly plan) pushes users to the yearly plan and may improve sales or revenue.


*Assessment:* The two members that support it only offer a hypothesis and a pattern seen in other apps' paywalls, with no measured result. The two App Masters members report the opposite: moving the trial off the yearly plan and onto a weekly plan tripled sales. That test changed the paywall design at the same time, so it isn't a clean comparison. The App Masters claims come from sellers of courses and agency services and are verbal or screenshot-only. The allowed official docs don't address this.


*Test with your own data:* Run an A/B test with the same paywall design and prices. Arm A gives the trial only on the yearly plan. Arm B gives a short trial on the weekly or monthly plan instead. Run it for at least 3–4 weeks, or until each arm has enough trial starts. Compare revenue per install and 60-day retained revenue, not only gross sales.


- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=1964) @32:44 · RevenueCat · 2026-09-09 · *supports* · basis: general knowledge
  > decrease free trial from the less expensive product and stay with free trial only on yearly product.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=667) @11:07 · Steven Cravotta · 2026-05-29 · *supports* · basis: other creator · conflict of interest: sells agency services, paid community
  > most of these apps are offering a yearly plan and a monthly plan. And only on the yearly plan are they ever offering a free trial.

- [How One Simple Paywall Test 3x’d Revenue for Our AI App (Case Study) 🚀](https://youtu.be/7kcieUp39iM?t=75) @1:15 · App Masters · 2025-05-13 · *contradicts* · basis: own experience · conflict of interest: sells agency services, sells a course
  > We got three X more sales from our B paywall than our A paywall.

- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=732) @12:12 · App Masters · 2026-08-18 · *contradicts* · basis: own experience · conflict of interest: sells agency services, sells a course, sponsored
  > We moved the trial from a 7-day yearly to a 3-day weekly and then sales 3x with similar amounts of downloads.

### <a id="k8"></a>K8 · well supported · confidence 0.93

Sign-up and onboarding questions or fields that don't help the user reach the first valuable action should be removed or deferred, because they add friction before activation.


*Assessment:* Three creators and ProductLed's guidance agree that fields not needed for the first value action should be cut or delayed. But all three members rest on general knowledge with no data shown, and two of the creators sell courses or agency services. The first video's own comments and the creator's reply note that long survey or quiz onboarding can work, for example in financial apps, so the rule depends on the product. The ProductLed page also warns against cutting too deep.


*Test with your own data:* A/B test your current sign-up against a version with only the essential fields, deferring the rest until after the first key action. Run it for 2–4 weeks, or until each arm has at least a few hundred sign-ups. Compare sign-up completion and the percentage who complete the first valuable action (activation within 7 days).


- Official source: [https://productled.com/time-to-value/](https://productled.com/time-to-value/) — “Any steps that add more friction for users to achieve the First Strike should be removed or delayed.”

- [Onboarding Best Practices from 200+ Top Apps!](https://youtu.be/vAN7kmpTdy4?t=811) @13:31 · Elizabeth Alli - DesignerUp · 2025-02-26 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, affiliate
  > if you're asking for their full name job title favorite color grandma's maen name before you even let them see the product they're not going to like that

- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=230) @3:50 · Henry SaaS · 2026-10-21 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > They even have it where they're asking, you know, their team size, the industry that they're in.

- [Suno Music AI: Making a Complex UX Easy to Use | App Breakdown #83](https://youtu.be/a_wJTPNOk_4?t=75) @1:15 · App Breakdown · 2026-09-22 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services
  > which a music creation tool doesn't need

### <a id="k9"></a>K9 · unverifiable · confidence 0.63

Iteratively A/B testing paywalls and onboarding can raise an app's install-to-trial or install-to-paid conversion several-fold, with no extra traffic.


*Assessment:* Three independent creators report large lifts from paywall and onboarding testing, which is directionally consistent. But all the numbers are stated verbally with no screenshots, and each speaker sells an agency, community, or sponsored product, so they have an incentive to show big wins. The official Userpilot docs describe A/B test setups but make no claim about the size of the lift. The different baselines, verticals, and metrics (install-to-paid vs. open-to-trial) also make the figures hard to compare or reproduce.


*Test with your own data:* Pick one change, such as the paywall variant or one onboarding step. Run a 50/50 A/B test (RevenueCat, Superwall, or an in-app tool) for at least 2 weeks, or until each arm has about 1,000 installs. Compare install-to-trial and trial-to-paid rates.


- Official source: [https://docs.userpilot.com/in-app-engagement/flows/use-cases/AB-testing.md](https://docs.userpilot.com/in-app-engagement/flows/use-cases/AB-testing.md) — “”

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=370) @6:10 · Superwall · 2025-11-16 · *supports* · basis: own experience · conflict of interest: sells agency services, paid community
  > They had like a 1.1% install to paid rate. We got it up to 4% in September.

- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=0) @0:00 · Steven Cravotta · 2026-03-04 · *supports* · basis: own experience · conflict of interest: sells agency services
  > We started at 8.5% initial conversion rate.

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=390) @6:30 · notJust․dev · 2026-02-06 · *supports* · basis: own experience · conflict of interest: affiliate, sponsored
  > we managed to have an open up to start trial. We started maybe at 15, 20, and we managed to drive that until 33%.

### <a id="k10"></a>K10 · contested · confidence 0.59

Showing a transparent trial timeline on the paywall (when the trial ends and when and what you will be charged) improved Blinkist's trial sign-ups/conversion (reported +23%) and cut complaints.


*Assessment:* All three members repeat the same Blinkist case study (23% lift, 55% fewer complaints) second-hand, with no first-hand data and agency/course conflicts of interest, so they are not independent. The figures trace back to a single secondhand story, and I found no primary Blinkist data. The allowed official docs (Appcues, Userpilot, ProductLed, Reforge, Intercom) are silent on it. The tactic is plausible, but the numbers are unverified, and the case concerns consumer apps with a hard paywall and a free trial, not B2B SaaS activation.


*Test with your own data:* A/B test your paywall or trial-start screen with and without an explicit timeline (day 0 start, day 5 reminder, day 7 charge and price) for at least 2 weeks. Measure trial start rate, trial-to-paid conversion, refund/complaint tickets and 30-day churn.


- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=148) @2:28 · Mobbin · 2026-07-09 · *supports* · basis: other creator · conflict of interest: sells agency services
  > The result was more trial sign-ups, fewer complaints.

- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=291) @4:51 · App Masters · 2026-08-18 · *supports* · basis: other creator · conflict of interest: sells agency services, sells a course, sponsored
  > How solving our biggest customer complaint at Blinkist led to a 23% increase in conversions.

- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=443) @7:23 · Tim Gabe · 2026-05-18 · *supports* · basis: other creator · conflict of interest: sells agency services
  > The result was a 23% increase in conversion rate, a 55% drop in complaints, and zero change in churn.

### <a id="k11"></a>K11 · likely · confidence 0.68

Activation is the point or process at which a user first gets real value from the product, and it must be defined specifically for each product (for example, running a browser session, installing an extension, or building a habit).


*Assessment:* All three members define activation as the user getting value, but they differ in form. One sees it as a process ending in a habit, and two see it as a single key action. The sources are definitions and opinions, not tested findings. Only Browserbase's is first-hand, and it is a single company's example. They agree on the principle, and the exact definition depends on the product.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=3441) @57:21 · GROWTH ROCKSTAR · 2025-04-03 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > Para mí activación es un proceso en el que usuario va de hacerse una cuenta a generar un hábito.

- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=464) @7:44 · Henry SaaS · 2026-10-21 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > The activation point is the thing that someone would have to hit in order to activate in your products and receive value.

- [How We Grew Our Self-Serve Revenue by 119% in Three Months](https://youtu.be/iLrbuDNbask?t=152) @2:32 · Upside - AI Intelligence Layer for GTM · 2026-07-16 · *supports* · basis: own experience
  > For us, activation is, does someone use a browser?

### <a id="k12"></a>K12 · likely · confidence 0.63

Choose the paywall's default-selected plan based on measured LTV per product (often yearly) rather than defaulting to the cheapest or smallest option; a yearly default is not right for every business.


*Assessment:* The members agree that the default plan matters and should be picked using LTV, but they differ on which plan. Mobbin says yearly, RevenueCat says to test and switch to yearly only if its LTV and retention are better, and one RevenueCat claim says to use the middle option. All four rest on general knowledge or an unshown "we see" statement, and none shows data. Mobbin also sells agency services. The allowed docs (Appcues, Userpilot, Intercom, Reforge, ProductLed) say nothing on paywall defaults. Outside sources point both ways: yearly is the most common preselection, but Adapty's 2026 analysis ranks a weekly plan with a trial highest on one-year LTV. A viewer comment about not being able to afford a yearly plan shows the cost of defaulting to yearly.


*Test with your own data:* A/B test the default plan (yearly vs your current default) for at least 2–4 weeks, or until there are enough conversions per arm. Compare 30-day revenue per paywall viewer and, later, retention and refund rates. Don't judge it on conversion rate alone.


- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=437) @7:17 · Mobbin · 2026-07-09 · *qualifies* · basis: client data · conflict of interest: sells agency services
  > Ideally, you want to default to a yearly product because we see that that has the highest LTV

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=1019) @16:59 · RevenueCat · 2026-09-09 · *supports* · basis: general knowledge
  > please check your analytic data and try to figure out what's the best LTV will be for each product.

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=1019) @16:59 · RevenueCat · 2026-09-09 · *qualifies* · basis: general knowledge
  > you have to try to change default plan from monthly to yearly.

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=2515) @41:55 · RevenueCat · 2026-09-09 · *qualifies* · basis: general knowledge
  > change, um, uh, the default one from the smallest one to the average

### <a id="k13"></a>K13 · likely · confidence 0.62

Paywall optimization works best by running bold tests (radically different designs, headers, and pricing tested in isolation) rather than small wording tweaks.


*Assessment:* The members agree that big, structurally different tests beat small tweaks, and the one screen-shown data point (Puff Count, $1.15 vs $0.39 ARPU from header changes) fits that. But all of this comes from consumer-app paywall creators who sell agency or community services, and the other members repeat general knowledge with no data. Pricing-first and design-first are different priorities, and the allowed official docs (Appcues, Userpilot, Reforge, Intercom, ProductLed) say nothing about paywall testing. The claim also concerns consumer subscription paywalls rather than B2B activation.


*Test with your own data:* Run two radically different paywall designs (e.g. bullet list vs trial timeline) against your current one, with a 3-way even split for at least 2–4 weeks. Change nothing else, and compare revenue per paywall view (ARPU) and trial start rate.


- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=659) @10:59 · Mobbin · 2026-07-09 · *supports* · basis: other creator · conflict of interest: sells agency services
  > design tests move the needle the most.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=891) @14:51 · Steven Cravotta · 2026-05-29 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > First, I recommend that you test your pricing, and that should be the only thing that you're changing on your paywall.

- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=773) @12:53 · Steven Cravotta · 2026-03-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > You want to test vastly different headers to kind of get yourself closer to the most optimized header wording possible.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=742) @12:22 · Steven Cravotta · 2026-05-29 · *supports* · basis: own experience · conflict of interest: sells agency services, paid community
  > It was $1.15 compared to the lowest one at 39 cents.

### <a id="k14"></a>K14 · contested · confidence 0.58

Longer onboarding is justified only when the extra questions or steps produce a personalized first experience or filter for likely buyers; otherwise a short flow of about 3–5 steps is preferable.


*Assessment:* All four members are opinion or general knowledge with no data shown. The Tim Gabe and Adam Lyttle videos broadly agree: length should be earned by personalization or buyer filtering, and shorter flows are easier to build. A comment citing a ~$1M/month app whose A/B tests favored longer onboarding is second-hand, but it points to real contention in paywall-driven consumer apps. The Appcues docs say personalization helps and doesn't need complexity. They say nothing on optimal length or on B2B SaaS activation.


*Test with your own data:* A/B test your current flow against a trimmed version (about 3–5 steps) for at least 2 weeks, or until each arm has enough users. Compare activation rate (first valuable action), trial-to-paid conversion and day-7 retention, not just sign-up completion.


- Official source: [https://www.appcues.com/customer-stories/how-hotjar-increased-installations-by-26-with-a-personalized-approach-to-onboarding](https://www.appcues.com/customer-stories/how-hotjar-increased-installations-by-26-with-a-personalized-approach-to-onboarding) — “Personalization doesn’t demand complexity”

- [How To Solve The App Onboarding Paradox](https://youtu.be/Aa89MC8jX2c?t=220) @3:40 · Tim Gabe · 2026-06-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Either a personalized first experience that wouldn't be possible without the data or a filter that gets you actual buyers.

- [How To Solve The App Onboarding Paradox](https://youtu.be/Aa89MC8jX2c?t=147) @2:27 · Tim Gabe · 2026-06-03 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > You give up speed, but you get a first experience built specifically for you.

- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=518) @8:38 · Adam Lyttle · 2025-08-08 · *supports* · basis: own experience
  > Do you need that many? Probably not. A more sensible approach might actually be the way to go.

- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=518) @8:38 · Adam Lyttle · 2025-08-08 · *qualifies* · basis: general knowledge
  > It's a really straightforward process that strips down the Cal AI onboarding questionnaire format into something a little more digestible.

### <a id="k15"></a>K15 · well supported · confidence 0.93

Mobile app onboarding should sell the benefit or outcome the user wants, not present a feature list or feature-tour screens.


*Assessment:* All four members say the same thing, but they are general-knowledge opinions with no data. Two come from the same creator (Adam Lyttle), so they are not independent. Appcues' own guidance, which comes from a vendor with a stake in onboarding, independently says to frame steps around what the user gets, not around features. No credible source argues the opposite. The weak point is the missing quantified evidence, not any disagreement.


- Official source: [https://www.appcues.com/blog/user-onboarding](https://www.appcues.com/blog/user-onboarding) — “Every step should be framed in terms of what the user gets, not what the product does.”

- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=148) @2:28 · Adam Lyttle · 2025-08-08 · *supports* · basis: general knowledge
  > But the key across the entire onboarding flow is to focus on the benefits.

- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=72) @1:12 · Mobbin · 2026-04-16 · *supports* · basis: general knowledge
  > features, they're selling the outcome.

- [I made a Claude Skill that builds app onboarding](https://youtu.be/at94PruxNdo?t=72) @1:12 · Adam Lyttle · 2026-04-08 · *supports* · basis: general knowledge
  > The onboarding flow doesn't sell the feature, it sells that transformation.

- [I made a Claude Skill that builds app onboarding](https://youtu.be/at94PruxNdo?t=0) @0:00 · Adam Lyttle · 2026-04-08 · *supports* · basis: general knowledge
  > The old way of doing onboarding was a few screens showing off your features.

### <a id="k17"></a>K17 · likely · confidence 0.64

Before running many paywall experiments, first put the basic paywall placements in place (e.g. a simple base paywall, session start, transaction abandonment) and gather baseline stats from a sample of users.


*Assessment:* All three members say the same thing: set a simple baseline with core placements first, then experiment. They come from two channels. Both sell services: one is an agency, the other a paywall-tool vendor with a paid community. Neither shows data, and one is general knowledge. The advice is sensible but it is not independently verified. It is also about consumer app paywalls, and only loosely related to B2B onboarding and activation. The searches of the allowed official domains (Appcues, Userpilot, Intercom) returned nothing relevant, so the docs are silent.


*Test with your own data:* Launch only a simple base paywall plus a transaction-abandonment placement. Run it for 2-4 weeks, or until each variant has about 1,000+ paywall views. Record view-to-trial and trial-to-paid rates as your baseline. Then A/B test one change at a time against that baseline.


- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=437) @7:17 · Mobbin · 2026-07-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > You want to keep the base paywall simple, get a bunch of users in there to see how your base stats perform

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=518) @8:38 · Superwall · 2025-11-16 · *supports* · basis: client data · conflict of interest: sells agency services, paid community
  > most of kind of the apps that come to us they lack a lot of like fundamental stuff that is concerned to placements

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=2515) @41:55 · Superwall · 2025-11-16 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > If you don't have transaction abandonment payable in place, put it there.

### <a id="k18"></a>K18 · likely · confidence 0.64

Paywall and CTA copy that is specific and focused on the trial or on a benefit ("Try it free", "Start my 3-day trial", a feature-related CTA) converts better than generic copy such as "annual plan" or "Start now for $3.99/month".


*Assessment:* Three creators broadly agree that specific, trial- or benefit-led CTA copy beats generic copy. However, none shows data on screen, and two of them have commercial ties (Superwall sells paywall tooling). One member rests on general knowledge only. A commenter on the first video flags a compliance risk: a "try for free" button on a no-trial option may violate Apple's rules. So the tactic is plausible but depends on the CTA matching the actual offer. The official docs searched (Appcues, Userpilot, Intercom, etc.) said nothing on paywall CTA copy.


*Test with your own data:* A/B test the generic CTA against the specific trial or feature CTA on the same paywall. Run it for at least 2 weeks, or until each variant has roughly 1,000 paywall views. Compare trial-start rate, then trial-to-paid conversion.


- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=739) @12:19 · Superwall · 2025-11-16 · *qualifies* · basis: own experience · conflict of interest: sells agency services, paid community
  > We say try it free because it's free and on a CTA again we say try for free

- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=663) @11:03 · Superwall · 2026-02-08 · *supports* · basis: own experience · conflict of interest: sponsored, paid community
  > And so you're increasing that free trial conversion rate and you're showing that yeah, the weekly has no plan.

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=3443) @57:23 · RevenueCat · 2026-09-09 · *supports* · basis: general knowledge
  > having a call to action that is, uh, is a feature related call to action for the customer.

### <a id="k19"></a>K19 · contested · confidence 0.56

Hard paywalls, and onboarding walls that end in a paywall, convert downloads to paid much better than freemium models in subscription apps, at the cost of more friction.


*Assessment:* The "about 5x" figure matches RevenueCat's State of Subscription Apps data (median download-to-paid about 10–12% vs about 2%), which is the original source for C1. But the gap is correlational, since apps that choose hard paywalls differ from freemium apps, and the hard-paywall side also shows higher refund rates. C2 and C3 contradict each other on which design converts best (hard paywall vs onboarding wall) and neither gives data. All three members rest on repetition or general knowledge by agency-selling creators. The allowed official domains (Appcues, Userpilot, Productled, Reforge, Intercom) say nothing on paywall design.


*Test with your own data:* A/B test, split by install cohort, your current paywall against a hard paywall placed after onboarding with a trial. Run it for at least 2–4 weeks, or until there are enough installs per arm. Compare install-to-paid conversion, trial-to-paid rate, refund rate and day-35 revenue per install.


- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=74) @1:14 · Steven Cravotta · 2026-05-29 · *supports* · basis: other creator · conflict of interest: sells agency services, paid community
  > They convert five times better than freemium

- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=157) @2:37 · Nik Zechner · 2026-03-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > This method has the highest conversion rate of all apps.

- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=472) @7:52 · Nik Zechner · 2026-03-27 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > And then the onboarding wall that converts the best.

### <a id="k20"></a>K20 · contested · confidence 0.60

When A/B testing a paywall or onboarding, change only one element at a time so any change in conversion can be attributed to that element.


*Assessment:* All three creators repeat the standard attribution principle, and none shows data. The Appcues and Userpilot docs I checked don't require a single change. Userpilot's experiment types explicitly allow multivariate tests and tests with several variables. Many third-party sources do state the one-change rule. It is sound for attributing cause, but it's a trade-off, because it slows learning when traffic is low or when you are comparing whole redesigned flows.


- Official source: [https://appcues.com/blog/flow-variation-a-b-testing](https://appcues.com/blog/flow-variation-a-b-testing) — “”

- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=620) @10:20 · Steven Cravotta · 2026-03-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > So you can only change one thing at a time.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=891) @14:51 · Steven Cravotta · 2026-05-29 · *supports* · basis: own experience · conflict of interest: sells agency services, paid community
  > Only test one thing at a time.

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=543) @9:03 · notJust․dev · 2026-02-06 · *supports* · basis: own experience · conflict of interest: affiliate, sponsored
  > we change only one onboarding step for a couple of days, let's say.

### <a id="k21"></a>K21 · likely · confidence 0.64

Since early 2026, Apple App Review has been rejecting subscription paywalls that use an "enable free trial" toggle, because it considers them confusing or misleading.


*Assessment:* Both videos say the same thing, though neither shows evidence and both rest on general knowledge. Third-party paywall vendors (RevenueCat, Adapty, Superwall) independently report rejections under Guideline 3.1.2 starting around January 2026. The allowed official-doc domains (Appcues, Userpilot, Productled, Reforge, Intercom) say nothing about it. Nothing credible contradicts the claim. Those vendor reports are secondary sources, not Apple documentation, and Apple apparently made no formal announcement.


- [We Studied 2,995 Paywalls. Here’s What Actually Converts.](https://youtu.be/9ypqs_2fAl8?t=584) @9:44 · Mobbin · 2026-07-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > And in early 2026, Apple also started rejecting paywall patterns that relied on free trial toggles

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=1768) @29:28 · notJust․dev · 2026-02-06 · *supports* · basis: general knowledge · conflict of interest: affiliate, sponsored
  > By the way, do you know that the enable free trial toggle is already banned?

### <a id="k22"></a>K22 · likely · confidence 0.62

Cal AI's onboarding is a long quiz of about 20 or more steps that users complete before seeing the product.


*Assessment:* Two independent creators describe Cal AI's onboarding as about 20 steps. This is an observable fact about a public app, and there's no opposing view. Both are general knowledge without screen-shown data, and one creator sells agency services. The exact count may vary by app version. The official docs (Appcues, Userpilot, ProductLed, Reforge, Intercom) say nothing about Cal AI. My restricted search returned no relevant pages from those domains. A third-party benchmark found health and fitness apps have long onboarding flows (median about 20 steps), which is consistent with this claim but isn't an official doc.


- [How To Solve The App Onboarding Paradox](https://youtu.be/Aa89MC8jX2c?t=147) @2:27 · Tim Gabe · 2026-06-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Their onboarding is a 20-plus step quiz.

- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=296) @4:56 · Adam Lyttle · 2025-08-08 · *supports* · basis: general knowledge
  > Cal AI follows the same process, but instead of four steps, they've got 20.

### <a id="k23"></a>K23 · well supported · confidence 0.91

Dropping new users onto blank or empty screens, or into complex setup, without guidance on the next step causes them to leave before reaching value. Empty states should tell users what to do next.


*Assessment:* Both members make the same general point, and Appcues' guidance matches it. Both come from creators who sell agency services (one also a course), and neither shows data, so the evidence is weak. Even so, nothing credible argues against it. The "10-step form" detail and the "never" wording are rhetorical and have no numeric backing.


- Official source: [https://www.appcues.com/blog/user-onboarding-best-practices](https://www.appcues.com/blog/user-onboarding-best-practices) — “An empty dashboard that says "No data yet" leaves users stranded.”

- [How We Boosted SaaS Activation by 40%: A UX Case Study](https://youtu.be/DiKC6sMe_q0?t=0) @0:00 · Eleken · 2025-12-23 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > If they open your app and get hit with a blank screen, a complicated setup, or a 10-step form, they re gone.

- [Suno Music AI: Making a Complex UX Easy to Use | App Breakdown #83](https://youtu.be/a_wJTPNOk_4?t=379) @6:19 · App Breakdown · 2026-09-22 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services
  > never or almost never lead users into empty views, into dead ends

### <a id="k26"></a>K26 · contested · confidence 0.54

About 55% of cancellations on 3-day free trials happen on day zero, the day of install. This comes from RevenueCat's State of Subscription Apps data.


*Assessment:* Secondary coverage of RevenueCat's report gives 55.4% of 3-day trial cancellations on day 0, which matches the first member. The second member drops the "3-day trial" qualifier and says "all app cancellations", which overstates the figure. Longer trials show lower day-0 shares; one source puts 30-day trials at about 31%. Both members repeat RevenueCat and have no first-hand data, and both creators sell agency services. The allowed vendor domains (Appcues, Userpilot, Intercom) returned nothing on this statistic.


- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=146) @2:26 · Tim Gabe · 2026-05-18 · *supports* · basis: other creator · conflict of interest: sells agency services
  > 55% of three-day trial cancellations also happen on day zero.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=74) @1:14 · Steven Cravotta · 2026-05-29 · *qualifies* · basis: other creator · conflict of interest: sells agency services, paid community
  > 55% of all cancellations happen on day zero, the first day that someone has your app installed.

### <a id="k27"></a>K27 · likely · confidence 0.62

Apps with low traffic can't detect small effects, so they should test bold, large changes (whole screens or multi-element changes) rather than small cosmetic tweaks like button colour or font.


*Assessment:* Both members make the same statistical point: small effects need large samples, so low-traffic apps should go bigger. Neither gives data (both are general_knowledge), and the notJust.dev video carries affiliate and sponsorship conflicts. The point matches standard A/B-testing logic, and the official pages I fetched don't address it directly. It holds only when the goal is statistically detecting effects. "Skip step-by-step tests" also means you give up attribution of which change worked, and at around 10 users a day even bold tests may need weeks.


- Official source: [https://userpilot.com/blog/ab-testing-mistakes/](https://userpilot.com/blog/ab-testing-mistakes/) — “”

- [The 3 layers of paywall conversion: offer, value, and design [Shipaton](https://youtu.be/wr0a_ZTpnU8?t=2121) @35:21 · RevenueCat · 2026-09-09 · *supports* · basis: general knowledge
  > you can go like with more bold ideas and with blocks.

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=775) @12:55 · notJust․dev · 2026-02-06 · *supports* · basis: general knowledge · conflict of interest: affiliate, sponsored
  > unless you're a huge app like Duolingo or something like that, you don't have enough users who come through your app

### <a id="k30"></a>K30 · well supported · confidence 0.91

Users should reach their aha moment as fast as possible after sign-up, since slow time-to-value drives churn (one member claims a hard 7-minute limit).


*Assessment:* The general direction (faster time-to-value reduces early churn) is supported by Userpilot's guidance, though the page is a vendor blog and not hard evidence. The specific 7-minute cutoff has no source and isn't in the docs; Userpilot cites a ~1.5-day average and under 5 minutes for top performers, so the right target varies by product complexity. Both members are general knowledge from agency sellers, with no data shown. "Most decisions happen on day zero" is also unsourced.


*Test with your own data:* Segment last 60–90 days of sign-ups by time-to-first-key-action (e.g. <5 min, 5–30 min, >30 min, >1 day) and compare day-30 retention or trial-to-paid conversion. The threshold where retention drops sharply is your own number.


- Official source: [https://userpilot.com/blog/aha-moment/](https://userpilot.com/blog/aha-moment/) — “Friction between signup and the Aha moment is the most common reason users churn before they reach it.”

- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=230) @3:50 · Henry SaaS · 2026-10-21 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > And you want this to be below seven minutes, because if it's over seven minutes, that person is going to very likely churn.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=74) @1:14 · Steven Cravotta · 2026-05-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > it is imperative that you deliver the users the aha moment, the key value inside of your app as quick as possible.

### <a id="k32"></a>K32 · contested · confidence 0.58

A hard paywall (no dismiss option, shown before app use) is most appropriate when each non-paying user is costly, as with AI apps or paid-traffic installs, so non-payers cannot consume resources or acquisition spend.


*Assessment:* Both members give a plausible cost-based rationale, but each is general-knowledge opinion with no data. Both creators also sell services or courses. The two rationales are different (serving cost versus acquisition cost) and don't conflict. The allowed official docs (Appcues, Userpilot, Productled, Reforge, Intercom) say nothing about hard paywalls. Outside sources suggest hard paywalls raise install-to-paid conversion but also raise uninstalls, so the claim holds only in certain situations. It also sits at the edge of a B2B SaaS activation topic, since it is mainly a consumer-app tactic.


*Test with your own data:* A/B test the hard paywall against a soft paywall (dismissible, or a trial that needs no card) on paid-traffic installs for at least 2 weeks. Compare cost per paying subscriber (spend ÷ paid conversions) and day-7 retention, not just cost per trial.


- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=549) @9:09 · Nik Zechner · 2026-03-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > the hard paywall makes sense because you don't want to have users in the app that use it, that cost you money

- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=143) @2:23 · App Masters · 2026-08-18 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored
  > You're paying for this traffic, you might as well force them to either pay or get out.

### <a id="k36"></a>K36 · contested · confidence 0.57

Weekly subscription plans convert better than annual plans in subscription apps, particularly for low-long-term-value apps like AI photo/video tools, though this says nothing about long-term retention or revenue.


*Assessment:* The creator of 7kcieUp39iM (own experience, ads manager screenshots) reports weekly beating yearly for one-time-use AI apps, and says it worked less well for long-term-use apps on a small sample. Tim Gabe's "1.7 to 7.4x across every price tier" figure is verbal general knowledge. It matches Adapty benchmark wording found in search, so it is vendor data and not independent practitioner evidence. Commenters on both videos note churn and the decoy or entry-point effect, so higher conversion does not mean better revenue or retention. The allowed official docs (Appcues, Userpilot, ProductLed, Reforge, Intercom) say nothing on this.


*Test with your own data:* Run an A/B paywall test with weekly versus annual, each with the same trial, for at least 2–4 weeks or until each arm has about 100 conversions. Compare trial-to-paid conversion and also revenue per install at 30 and 90 days, including refunds and churn.


- [How One Simple Paywall Test 3x’d Revenue for Our AI App (Case Study) 🚀](https://youtu.be/7kcieUp39iM?t=151) @2:31 · App Masters · 2025-05-13 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course
  > Weekly actually does perform better than yearly.

- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=73) @1:13 · Tim Gabe · 2026-05-18 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > So, weekly plans convert 1.7 to 7.4 times better than annual plans across every price tier.

### <a id="k37"></a>K37 · contested · confidence 0.56

Plan length (weekly vs. annual) materially changes subscription-app monetization: weekly-plan subscribers can end up paying more than annual ones, while apps selling yearly plans are reported to monetize about 2x better early on.


*Assessment:* The two members point in different directions: Superwall says weekly plans out-earn annual for AI apps, while Cravotta, repeating RevenueCat data, says yearly-focused apps monetize better in the first 14 days and at day 60. Superwall sells paywall tooling and gave no numbers. Cravotta relays someone else's data verbally and sells agency services. Neither makes the case for onboarding or activation. Third-party search results (Adapty, RevenueCat) suggest weekly plans take a growing share of revenue in utilities and entertainment, and annual plans dominate in health and fitness. So the outcome depends on category and on retention.


*Test with your own data:* Run a paywall A/B test of weekly-led against annual-led pricing on new installs for at least 8–12 weeks. Compare cumulative revenue per install at days 14, 60 and 180, and refunds and churn, not only first-payment conversion.


- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=738) @12:18 · Superwall · 2026-02-08 · *supports* · basis: client data · conflict of interest: sponsored, paid community
  > a lot of the time weekly, you know, our users will pay more in the weekly plan than if they would have just paid for the annual plan.

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=149) @2:29 · Steven Cravotta · 2026-05-29 · *qualifies* · basis: other creator · conflict of interest: sells agency services, paid community
  > Apps that sell yearly subscriptions primarily monetize two times better than other groups in the first 14 days

### <a id="k38"></a>K38 · likely · confidence 0.62

Third-party app revenue estimates (Sensor Tower, Paywall Screens, etc.) are imprecise: tools disagree with each other and show revenue, not profit, so they are unreliable as absolute benchmarks.


*Assessment:* Both members agree that competitor-tracking estimates are imprecise: one shows a 20% gap between two tools ($800k vs $1M), the other notes that revenue is not profit. Both are from different channels, but neither shows data on the true figures. Official docs from the allowed domains are silent on this, as they cover SaaS onboarding rather than app-store estimation. Vendor blogs outside the allowed list also say estimates can be off by 30-50% and that trend direction is more reliable than absolute figures. This is also off-topic for activation and onboarding.


- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=155) @2:35 · Steven Cravotta · 2026-03-04 · *supports* · basis: own experience · conflict of interest: sells agency services
  > Sensor Tower says $800,000. Paywall screen says a million dollars a month

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=1692) @28:12 · notJust․dev · 2026-02-06 · *supports* · basis: own experience · conflict of interest: affiliate, sponsored
  > revenue is one metric, but then profits, there is no way to know

### <a id="k39"></a>K39 · unverifiable · confidence 0.55

Mural replaced its earlier onboarding (pop-ups and banners) with a gamified, step-by-step checklist, and one-week retention increased. The size of the lift is disputed: about 30% in one account, 10% relative in another.


*Assessment:* Both members agree on the direction (a checklist raised one-week retention at Mural), but the magnitude differs: about 30% versus 10% relative. The first is a verbal recollection from a course seller, and the second is a second-hand case-study summary with no method shown. A commenter asked how the numbers were obtained and got no answer. The official docs searched (Appcues, Userpilot) contain no Mural data, only vendor claims for other companies.


*Test with your own data:* A/B test your current onboarding against a checklist variant. Randomize new sign-ups for at least 2-4 weeks, until each arm has enough users to detect your expected lift. Compare the share of users returning in days 1-7, and the activation rate.


- Official source: [https://www.appcues.com/ui-patterns/checklists](https://www.appcues.com/ui-patterns/checklists) — “”

- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=2828) @47:08 · GROWTH ROCKSTAR · 2025-04-03 · *qualifies* · basis: own experience · conflict of interest: sells a course
  > había subido como si te dijera, tipo, 30% del one week retention, que hicimos un gamified onboarding

- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=442) @7:22 · Mobbin · 2026-04-16 · *qualifies* · basis: other creator
  > it drove a 10% relative increase in one-week retention.

### <a id="k40"></a>K40 · likely · confidence 0.60

If onboarding is already good, adding more onboarding is not the fix; remaining post-trial churn points to the product itself, or to onboarding that should do the work for the user.


*Assessment:* Both members are opinions with no data, and both come from creators with a conflict of interest (an agency seller and a sponsored channel). They agree in direction: more onboarding is not always the answer. They differ in scope, though. One is about low-personalization consumer and AI apps. The other is about heavy post-trial churn when onboarding is already good. The "good onboarding" premise is hard to verify, because onboarding quality is usually judged by activation, which is itself affected by the product. The official docs I checked say nothing on this.


*Test with your own data:* Segment trial users by whether they reached the aha action. Compare trial-to-paid conversion and 30-day retention for activated and non-activated users, over at least one full trial cycle. If activated users still churn heavily, the cause is the product, pricing or fit, not onboarding. If activation is low, simplify the onboarding steps before adding more.


- Official source: [https://userpilot.com/solutions/customer-retention-software](https://userpilot.com/solutions/customer-retention-software) — “”

- [How To Solve The App Onboarding Paradox](https://youtu.be/Aa89MC8jX2c?t=74) @1:14 · Tim Gabe · 2026-06-03 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > the fix usually isn't more onboarding. It's onboarding that does the work for the user, not work for you.

- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=1767) @29:27 · Superwall · 2026-02-08 · *qualifies* · basis: general knowledge · conflict of interest: sponsored, paid community
  > then you know it's a product issue

### <a id="k41"></a>K41 · well supported · confidence 0.90

Onboarding should not be one-size-fits-all; personalising it by user type, customer size, use case or behaviour improves activation.


*Assessment:* Both members make the same general point, but each is an unevidenced opinion from a creator with a conflict of interest (a course seller and an agency/sponsored channel). Vendor material (Appcues) backs role-based personalisation, though that is also a vendor with a commercial interest, and its customer results are self-reported. Personalisation is plausible and widely recommended, but it has a cost, and the gain depends on how different your segments really are.


*Test with your own data:* Split new sign-ups into a generic flow and a flow tailored to your biggest segment (for example by role chosen at sign-up). Run both for 2–4 weeks, or until each arm has about 200 sign-ups. Compare the share who reach the first key action (such as the first appointment) within 7 days.


- Official source: [https://appcues.com/blog/personalizing-user-onboarding](https://appcues.com/blog/personalizing-user-onboarding) — “The product might be the same, but the path to value is different, and the onboarding should reflect that.”

- [Onboarding Best Practices from 200+ Top Apps!](https://youtu.be/vAN7kmpTdy4?t=886) @14:46 · Elizabeth Alli - DesignerUp · 2025-02-26 · *supports* · basis: general knowledge · conflict of interest: sells a course, affiliate
  > if your onboarding flow is one size fits all right now it can probably be improved

- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=2578) @42:58 · Practical Founders - with Greg Head · 2026-04-23 · *supports* · basis: general knowledge · conflict of interest: sponsored, paid community, sells agency services
  > you can't treat all of your customers the same, regardless of size, complexity, or use case

### <a id="k42"></a>K42 · contested · confidence 0.56

Onboarding should demonstrate the product's value before pushing monetization: pushing payment too aggressively makes users bounce, and failing to show value clearly can lead users to pick short plans or not convert.


*Assessment:* Both members make the same broad point: value should be shown before or alongside the ask. The first rests on general knowledge from a course seller. The second is a hedged ("maybe") interpretation from a sponsored Superwall channel, with client data that was not shown. The Appcues page only says unnecessary steps are exit points, so it does not address monetization timing. The claim is plausible, but how aggressive the ask can be without hurting conversion depends on the app and its paywall.


*Test with your own data:* A/B test the paywall placement: show it after the first valuable action versus at the end of onboarding. Run it for at least 2 weeks, or about 1,000 installs per arm. Compare trial start rate, day-7 retention and the share of users on annual plans.


- Official source: [https://www.appcues.com/onboarding](https://www.appcues.com/onboarding) — “Every unnecessary step in your onboarding flow is a potential exit point.”

- [Onboarding Best Practices from 200+ Top Apps!](https://youtu.be/vAN7kmpTdy4?t=371) @6:11 · Elizabeth Alli - DesignerUp · 2025-02-26 · *supports* · basis: general knowledge · conflict of interest: sells a course, affiliate
  > if onboarding is too aggressive in pushing monetization users will bounce before they even understand the value

- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=1031) @17:11 · Superwall · 2026-02-08 · *supports* · basis: client data · conflict of interest: sponsored, paid community
  > maybe we didn't do a good good enough job in onboarding really showing off the product

### <a id="k43"></a>K43 · well supported · confidence 0.94

Letting users experience the app's core value (e.g., a teaser or AI feature) before sign-up or paywall is a worthwhile onboarding pattern that delivers the aha moment earlier.


*Assessment:* Both members recommend the pattern from general knowledge, with no data shown. Userpilot's guide gives Loom and Zoom as examples where value arrives before sign-up, which supports the idea. One commenter says they uninstalled when asked to sign up first, but that is a single anecdote. It is mostly consumer and AI app advice. For B2B SaaS with a trial, the fit depends on whether the product can show value without the user's own data.


*Test with your own data:* A/B test: show half of new installs a pre-signup teaser or demo and the other half sign-up first. Run it for 2 to 4 weeks. Compare the sign-up completion rate, the share who reach the first valuable action, and day-1 retention.


- Official source: [https://userpilot.com/blog/?p=2212](https://userpilot.com/blog/?p=2212) — “the Aha moment arrives before onboarding is required”

- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=72) @1:12 · Mobbin · 2026-04-16 · *supports* · basis: general knowledge
  > lets you try the core experience before you sign up.

- [I made a Claude Skill that builds app onboarding](https://youtu.be/at94PruxNdo?t=147) @2:27 · Adam Lyttle · 2026-04-08 · *supports* · basis: general knowledge
  > It's a curated way to show the best part of your app, the instant aha moment, right in your onboarding flow.

### <a id="k44"></a>K44 · contested · confidence 0.59

Freemium works best for simple, network-effect or marketplace apps. For complex B2B SaaS, freemium or a free trial usually doesn't bring in more users.


*Assessment:* The two members are complementary rather than conflicting. Freemium fits network-effect and marketplace apps, and complex B2B products often don't benefit from it. Both rest on opinion or on one person's experience, and both creators sell services, so the evidence is weak. The ProductLed page doesn't address product complexity, and third-party blogs found in search give a similar rule of thumb, but they aren't official docs.


*Test with your own data:* Run a 4–6 week split on your signup flow: one arm offers a free trial or freemium plan, the other requires a demo or guided onboarding. Compare the cost per activated account (users who complete the first key action) and the trial-to-paid rate.


- Official source: [https://productled.com/?p=15178](https://productled.com/?p=15178) — “Design the right free experience instead of giving away random free stuff.”

- [I’ve Analyzed the Top 100 iOS Apps. They All Use the Same Paywalls.](https://youtu.be/qVRQIKFpkdQ?t=549) @9:09 · Nik Zechner · 2026-03-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > especially if you need to bring more people into the app to create network effects or to have a proper marketplace.

- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3516) @58:36 · Practical Founders - with Greg Head · 2026-04-23 · *supports* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > And it usually doesn't work that way if your product is complex enough.

### <a id="k47"></a>K47 · single source · confidence 0.55

Charging for implementation improves completion rates because it creates accountability (skin in the game) on the customer side.


- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3433) @57:13 · Practical Founders - with Greg Head · 2026-04-23 · *—* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > Like charging for implementation improves competition rates. We call that skin in the game.

- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3433) @57:13 · Practical Founders - with Greg Head · 2026-04-23 · *—* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > we find that people who pay for implementation are going to stick around.

### <a id="k60"></a>K60 · unverifiable · confidence 0.55

Paywall experimentation yields the biggest conversion gains for apps with little prior testing: about $100k/month apps benefit most, and newer $10k–50k/month apps can lift paywall conversion from roughly 8% to 15–20% after a couple of test iterations.


*Assessment:* Both members come from the same speaker at Superwall, a paywall-testing vendor, in a sponsored or community-paid video. The numbers are verbal, unaudited and have no evidence on screen. The official docs checked (Appcues) say nothing about paywall conversion by revenue stage, so nothing corroborates or refutes them. The direction is plausible, since low-testing apps have more room to improve, but the 8% to 15–20% figure is a vendor sales claim about selected customers.


*Test with your own data:* Run one A/B test on your paywall's biggest lever (price, trial length or layout), splitting traffic 50/50. Run it for at least 2–4 weeks, or until you have a few hundred conversions per arm. Success metric: paywall view to trial or paid conversion, plus revenue per user. Compare it with your baseline.


- Official source: [https://www.appcues.com/blog/mobile-app-onboarding](https://www.appcues.com/blog/mobile-app-onboarding) — “A/B test different flows to see what works”

- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=3310) @55:10 · Superwall · 2026-02-08 · *supports* · basis: client data · conflict of interest: sponsored, paid community
  > apps that are making I would say 100,000 a month and they haven't done a ton of payw wall experimentation

- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=3310) @55:10 · Superwall · 2026-02-08 · *supports* · basis: client data · conflict of interest: sponsored, paid community
  > to 15 to 20% after a couple iterations working with us

### <a id="k62"></a>K62 · single source · confidence 0.55

At a previous company that onboarded 30,000+ customers, a $1,500 onboarding fee filtered out customers unwilling to do the work, and those customers would not have stuck around anyway.


- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3594) @59:54 · Practical Founders - with Greg Head · 2026-04-23 · *—* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > if somebody wasn't willing to pay $1,500 to have somebody do real work to help them get this set up

- [The Real Bottom of the Funnel: SaaS Onboarding That Works](https://youtu.be/z7tqfuk8hrQ?t=3358) @55:58 · Practical Founders - with Greg Head · 2026-04-23 · *—* · basis: own experience · conflict of interest: sponsored, paid community, sells agency services
  > if you didn't pay, if you offered free onboarding, which we think was a nice gift, people wouldn't show up to the meetings.

### <a id="k64"></a>K64 · unverifiable · confidence 0.57

Cal AI earns about $1 million per month in revenue.


- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=0) @0:00 · Adam Lyttle · 2025-08-08 · *—* · basis: other creator
  > generating around $2.50 per download last month

- [I made a Claude Skill that builds app onboarding](https://youtu.be/at94PruxNdo?t=0) @0:00 · Adam Lyttle · 2026-04-08 · *—* · basis: general knowledge
  > Cal AI, a million dollars a month.

### <a id="k66"></a>K66 · single source · confidence 0.60

In the vendor's recommended first-day setup, the business should fill in its business profile and list itself on the Vagaro.com marketplace so customers can find it.


- [Welcome to Vagaro - Getting Started](https://youtu.be/NoyKf0yzZWs?t=235) @3:55 · Vagaro University | Support · 2026-03-19 · *—* · basis: platform docs · conflict of interest: sells agency services, sells a course
  > Remember to fill out your business profile and list your business on Vegaro.com so customers can find you through the Vegaro Marketplace.

- [Welcome to Vagaro - Getting Started](https://youtu.be/NoyKf0yzZWs?t=159) @2:39 · Vagaro University | Support · 2026-03-19 · *—* · basis: platform docs · conflict of interest: sells agency services, sells a course
  > Fill these out to get basic details about your business added to your Vegaro listing page.

### <a id="k73"></a>K73 · single source · confidence 0.53

In an A/B/C test at Mural, a discount email and a non-discount benefits-reminder email both outperformed no email, and the discount did not beat the reminder.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=2523) @42:03 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > tanto el 1 y el 2, performaban mejor que el 3

### <a id="k74"></a>K74 · single source · confidence 0.53

Interface changes to the invitation flow do not fix invitations if the account creator does not understand or like the product, because they will not invite anyone.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=3901) @1:05:01 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > no importa lo que vos hagas a nivel UI, si alguien, el creador de cuenta, no estaba convencido con tu aplicación, no iba a invitar a nadie

### <a id="k78"></a>K78 · single source · confidence 0.55

Complement the metrics analysis with at least five user interviews before deciding on activation changes, since metrics alone are not enough.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=1369) @22:49 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > al menos, tipo, al menos, cinco entrevistas a usuarios

### <a id="k85"></a>K85 · unverifiable · confidence 0.54

Zaplify, a SaaS client, doubled its activation rate after a UX overhaul by Eleken.


- [How We Boosted SaaS Activation by 40%: A UX Case Study](https://youtu.be/DiKC6sMe_q0?t=0) @0:00 · Eleken · 2025-12-23 · *—* · basis: client data · conflict of interest: sells agency services
  > Zaplify doubled their activation rate with a UX overhaul

### <a id="k87"></a>K87 · unverifiable · confidence 0.57

Using onboarding changes, the speaker says his SaaS reduced monthly churn from about 16% at its peak to about 6%.


- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=0) @0:00 · Henry SaaS · 2026-10-21 · *—* · basis: own experience · conflict of interest: sells agency services
  > using the exact process that I use to go from around 16% to 6% in churn

### <a id="k91"></a>K91 · single source · confidence 0.53

The full OneSignal journey templates, copy and sequences are withheld and sold inside the creator's paid community.


- [increase FREE TRIAL TO PAID conversion rate in 18 minutes (mobile apps](https://youtu.be/UnZ2RM2k7FM?t=156) @2:36 · Alim Charaniya · 2025-08-14 · *—* · basis: own experience · conflict of interest: paid community, sells agency services, affiliate
  > I provide all the templates and all the copy and strategy and sequences inside my paid community

### <a id="k96"></a>K96 · unverifiable · confidence 0.62

Browserbase reports that in three months signups grew 119% and activation rose 10%, with the 119% growth attributed to AI-agent referrals from Claude.


- [How We Grew Our Self-Serve Revenue by 119% in Three Months](https://youtu.be/iLrbuDNbask?t=0) @0:00 · Upside - AI Intelligence Layer for GTM · 2026-07-16 · *—* · basis: own experience
  > we grew our signups in three months by 119% and increased our activation by 10%

### <a id="k97"></a>K97 · single source · confidence 0.55

A generic 'Continue' CTA often converts better than a descriptive CTA such as 'Put AI into action', because it moves the user gently through the funnel.


- [I made 4,000 app paywalls and learned this](https://youtu.be/lkwX_kc0NS8?t=514) @8:34 · Superwall · 2026-02-08 · *—* · basis: own experience · conflict of interest: sponsored, paid community
  > we like to just have continue because it it kind of like lets the user gently go down that funnel to the conversion stage.

### <a id="k117"></a>K117 · single source · confidence 0.57

Instead of dropping new signups into an empty dashboard, drop them into an interactive sandbox that guides them to the first key action (for example, connecting an account) so they get value quickly.


- [I studied 200+ AI SaaS Onboardings, Here's What Actually Works](https://youtu.be/-SqrOQ_vT0k?t=152) @2:32 · Supademo · 2026-04-22 · *—* · basis: general knowledge
  > Now instead of dropping new users into some empty dashboard, you're dropping them into an interactive sandbox environment where they're guided to the exact action you needed to complete

### <a id="k142"></a>K142 · unverifiable · confidence 0.57

A client's MRR rose from about $2,500–3,000 to about $10,000 per month in roughly four months after onboarding was changed to push users toward the MCP.


- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=541) @9:01 · Henry SaaS · 2026-10-21 · *—* · basis: client data · conflict of interest: sells agency services
  > we recently got him to $10,000 a month, which when we started working together, he was around $2,500, $3,000

### <a id="k147"></a>K147 · single source · confidence 0.53

Connecting Slack to Mural correlated with very high retention, but the speaker thinks this is more likely an effect of already-engaged users than a cause, so it should not be used as an activation step by itself.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=3743) @1:02:23 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > si conectabas Slack con Mural, tipo, la retención era altísima

### <a id="k148"></a>K148 · unverifiable · confidence 0.53

Mural's free-trial-to-paid conversion was about 1.5% before the growth work began.


*Assessment:* This is a single verbal figure from one creator who sells a course, with no on-screen data. The official docs say nothing about Mural. They only give general benchmarks: Userpilot says the median free-trial conversion is 8%, and 20% of products convert below 2.5%. A 1.5% rate is therefore plausible, but it can't be checked. The "interested but not convinced" reading is the speaker's interpretation, not data.


*Test with your own data:* Measure your own trial-to-paid rate by signup cohort over 30–60 days. Compare it with the 8% median and the 2.5% low-end benchmark to see where you stand. Do not rely on the Mural figure.


- Official source: [https://userpilot.com/blog/saas-average-conversion-rate/](https://userpilot.com/blog/saas-average-conversion-rate/) — “Twenty percent of free trial products convert below 2.5%.”

- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=1990) @33:10 · GROWTH ROCKSTAR · 2025-04-03 · *supports* · basis: own experience · conflict of interest: sells a course
  > el conversion to pay era tipo un 1.5%

### <a id="k149"></a>K149 · single source · confidence 0.53

Simplifying Mural's invitation modal increased invitations by about 3%, but the speaker found that UI fixes did not help if the account creator was not convinced by their first board.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=3901) @1:05:01 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > con ese cambio sí aumentamos, creo que fue un 3% de las invitaciones

### <a id="k150"></a>K150 · single source · confidence 0.53

Letting a trial account owner pay for fewer seats than they have invited, with 30 days to remove the extra people, made a large difference to conversion to paid at Mural.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=2599) @43:19 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > permitirte pagar menos personas, aunque tengas más en tu workspace, y darte 30 días para borrarlos

### <a id="k151"></a>K151 · single source · confidence 0.53

At Mural, a series of mostly transactional onboarding and billing flow changes in one quarter roughly doubled conversion to paid.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=759) @12:39 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > en segundo cuarto de mural duplicamos el conversion a paid

### <a id="k153"></a>K153 · single source · confidence 0.53

Onboarding optimisation at Mural focused first on the account creator, because that person decided whether the team would adopt the product.


- [La evolución de un equipo de growth | Victoria Colombato (ex-Growth PM](https://youtu.be/4czPnSN0PTU?t=2447) @40:47 · GROWTH ROCKSTAR · 2025-04-03 · *—* · basis: own experience · conflict of interest: sells a course
  > Entonces, siempre por mucho tiempo nos enfocamos en ese primer usuario

### <a id="k157"></a>K157 · single source · confidence 0.64

To find activation problems, map every step a user takes from the marketing touchpoint to the aha moment, and remove steps that do not move them toward it.


- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=230) @3:50 · Henry SaaS · 2026-10-21 · *—* · basis: own experience · conflict of interest: sells agency services
  > map out every single step in your software that someone has to go through in order to get to the aha moment

### <a id="k181"></a>K181 · single source · confidence 0.55

Onboarding A/B tests need hundreds to thousands of users per variant to reach statistical significance.


*Assessment:* The claim matches general statistics: required sample size depends on baseline conversion and minimum detectable effect, and "hundreds to thousands" is a plausible range for typical onboarding step conversions. It comes from one creator's verbal experience with no data shown, and the creator has affiliate and sponsored ties. The official docs I checked (Userpilot) give no specific sample-size number, only advice to fix the sample size in advance and to aim for about 95% confidence. The range is a rule of thumb. The real number can be far higher for small effects.


*Test with your own data:* Before testing, plug your current onboarding step conversion rate and the smallest lift worth detecting into a sample-size calculator (95% confidence, 80% power). Compare the per-variant n with your weekly sign-ups to see whether the test can finish in under 4 to 6 weeks. If it can't, use a bigger change or a qualitative method instead.


- Official source: [https://userpilot.com/blog/ab-testing-mistakes/](https://userpilot.com/blog/ab-testing-mistakes/) — “”

- [Mobile app Onboarding secrets that convert](https://youtu.be/zCtwBQYD18U?t=543) @9:03 · notJust․dev · 2026-02-06 · *supports* · basis: own experience · conflict of interest: affiliate, sponsored
  > once we did have enough statistical significance, so hundreds or thousands of users who saw the same onboarding step

### <a id="k187"></a>K187 · unverifiable · confidence 0.60

Finance, health & fitness and education apps have the longest mobile onboarding flows, with finance apps making up about 7 of the 10 longest.


*Assessment:* There is only one source, Mobbin, which is a design-pattern library and plausibly has a large dataset. The figure is stated verbally, and the dataset and the way "longest" is measured aren't shown. The allowed official docs (Userpilot and others) have no category-level onboarding length data. An outside search suggests health & fitness and education are the longest categories, which only partly agrees with the finance claim. Finance may be over-represented because of KYC steps, but that isn't established.


*Test with your own data:* Count the onboarding steps in 10 competitor apps in your own vertical (use Mobbin or screen recordings). Compare them with your own flow and check whether your step-by-step drop-off and activation rate stay in line with that benchmark.


- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=0) @0:00 · Mobbin · 2026-04-16 · *supports* · basis: own experience
  > Seven out of 10 of these longest apps are actually finance apps as

### <a id="k204"></a>K204 · single source · confidence 0.57

Watching session recordings can reveal dead clicks; making a whole table row clickable (instead of only a small button) was one of the biggest churn reducers for one SEO extension.


- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=306) @5:06 · Henry SaaS · 2026-10-21 · *—* · basis: own experience · conflict of interest: sells agency services
  > if someone selected the whole row, this was one of the biggest things that helped me reduce the churn

### <a id="k205"></a>K205 · single source · confidence 0.64

Session-recording tools such as PostHog (previously Microsoft Clarity) are the way to find where users get stuck before the aha moment.


- [If You Don't Understand Onboarding, You Don't Understand SaaS](https://youtu.be/Pn-5F2JoyA0?t=306) @5:06 · Henry SaaS · 2026-10-21 · *—* · basis: own experience · conflict of interest: sells agency services
  > watched session recordings at the time I used Microsoft Clarity, but now I'd recommend PostHog

### <a id="k213"></a>K213 · single source · confidence 0.60

In empty states, the call-to-action should sit where the text points; an empty library reading 'Get started below' with no button below it is confusing, so the empty state should lead directly into the intended action.


- [Suno Music AI: Making a Complex UX Easy to Use | App Breakdown #83](https://youtu.be/a_wJTPNOk_4?t=1145) @19:05 · App Breakdown · 2026-09-22 · *—* · basis: general knowledge · conflict of interest: sells a course, sells agency services
  > the empty state could be clear and just lead me into the thing that they really want me to do

### <a id="k216"></a>K216 · unverifiable · confidence 0.55

Adding OneSignal journeys for trial-started, trial-cancelled and trial-converted events raised the free trial to paid conversion rate by about 7%, measured June to July.


- [increase FREE TRIAL TO PAID conversion rate in 18 minutes (mobile apps](https://youtu.be/UnZ2RM2k7FM?t=156) @2:36 · Alim Charaniya · 2025-08-14 · *—* · basis: own experience · conflict of interest: paid community, sells agency services, affiliate
  > that did give it a nice 7% increase in conversion rate.

### <a id="k217"></a>K217 · single source · confidence 0.61

Setting up OneSignal journeys that trigger on trial-started, trial-cancelled and trial-converted events is a way to send push and email messages during a trial.


- [increase FREE TRIAL TO PAID conversion rate in 18 minutes (mobile apps](https://youtu.be/UnZ2RM2k7FM?t=156) @2:36 · Alim Charaniya · 2025-08-14 · *—* · basis: own experience · conflict of interest: paid community, sells agency services, affiliate
  > we actually have three different journeys running for trial started, trial cancellations, and trial converted.

### <a id="k219"></a>K219 · single source · confidence 0.58

Trial-end push reminders only reach users who have enabled push notifications, which adds friction, but Duolingo reportedly still lifted conversions with them.


*Assessment:* The mechanic that push needs opt-in is structurally true on iOS and Android 13+ and is widely documented by non-allowed vendors. The Duolingo conversion lift is a verbal claim from a creator who sells agency services and a paid community, with no data shown. The allowed official docs searched (Intercom, Appcues) said nothing on this point.


*Test with your own data:* Split trial users by push opt-in status and compare trial-to-paid conversion for those who got the push reminder versus those who got only an email reminder. Run it for at least 2 trial cycles (about 2–4 weeks). The success metric is the conversion rate difference.


- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=371) @6:11 · Steven Cravotta · 2026-05-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > the users actually have to turn on push notifications to be reminded

### <a id="k243"></a>K243 · single source · confidence 0.56

For clients, 'Continue' outperformed 'Start free trial' on iOS, while 'Start free trial' did better on Android.


- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=880) @14:40 · App Masters · 2026-08-18 · *—* · basis: client data · conflict of interest: sells agency services, sells a course, sponsored
  > continue for iOS, start free trial on Android.

### <a id="k245"></a>K245 · doubtful · confidence 0.05

Typical SaaS activation rates are about 20–30%, with world-class around 40%.


*Assessment:* The claim comes from one creator who sells agency services. He gives no data and no definition of "activation". Userpilot's benchmark of 62 B2B SaaS companies puts the average at 37.5% and the median at 37.04%. That is roughly the "world-class" level in the claim. Other sources put the median nearer 30%. The numbers depend heavily on how activation is defined and on the vertical, so the range is only a rough guide.


*Test with your own data:* Define your activation event, for example the first appointment created. Measure the share of sign-ups reaching it within 7 days, using the last 30–60 days of cohorts. Compare that with your own prior baseline instead of an outside benchmark, and track whether changes to onboarding lift it.


- Official source: [https://userpilot.com/saas-product-metrics/](https://userpilot.com/saas-product-metrics/) — “”

- [The Product-Led Growth Playbook for SaaS Startups (Navattic Case Study](https://youtu.be/sO2x9Nbggg4?t=76) @1:16 · Andrew Capland · 2026-10-06 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > World-class activation rates for SaaS companies tend to be around 40%, and most are really between 20% and 30%.

### <a id="k246"></a>K246 · unverifiable · confidence 0.53

Calorie tracker Yazio reportedly made around $3 million per month at 700,000 installs, with its paywall built around structure first and price last.


- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=368) @6:08 · Tim Gabe · 2026-05-18 · *—* · basis: other creator · conflict of interest: sells agency services
  > The calorie tracker did around $3 million in monthly revenue at 700,000 installs.

### <a id="k247"></a>K247 · unverifiable · confidence 0.53

Lose It reportedly made $3.3 million in monthly revenue at 350k installs after adding a paywall section that explained the free trial timeline.


- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=294) @4:54 · Tim Gabe · 2026-05-18 · *—* · basis: other creator · conflict of interest: sells agency services
  > The result, $3.3 million in monthly revenue at 350k installs.

### <a id="k250"></a>K250 · single source · confidence 0.57

GlossGenius onboarding asks for business type, team size, average weekly appointment count, referral source, current software and specialty before showing the dashboard.


- [Glossgenius Tutorial For Beginners: From Setup to First Client Booking](https://youtu.be/subY_kCGZuU?t=76) @1:16 · Software Scope · 2026-04-26 · *—* · basis: general knowledge · conflict of interest: affiliate
  > How many appointments does your business average per week?

### <a id="k251"></a>K251 · single source · confidence 0.57

The GlossGenius getting-started checklist has three steps, the first being 'Get discovered and booked online', which means claiming a business name and booking-page URL and choosing a template.


- [Glossgenius Tutorial For Beginners: From Setup to First Client Booking](https://youtu.be/subY_kCGZuU?t=156) @2:36 · Software Scope · 2026-04-26 · *—* · basis: general knowledge · conflict of interest: affiliate
  > There are three steps they recommend. Get discovered and booked online.

### <a id="k264"></a>K264 · single source · confidence 0.52

For free-trial subscription apps, a trial-to-paid conversion rate above about 30% is considered good.


*Assessment:* The ~30% threshold matches third-party benchmarks only for card-required (opt-out) trials, where 25-35% is "good". For no-card opt-in trials, "good" is about 4-6%, and the median across B2B SaaS is about 8%. The single speaker sells agency services, shows no data, and likely has consumer subscription apps with a paywall and card in mind. The official docs allowed here are blog summaries of benchmarks, not product documentation, so I treat them as silent.


- Official source: [https://userpilot.com/blog/saas-average-conversion-rate/](https://userpilot.com/blog/saas-average-conversion-rate/) — “Free trial (credit card required) | 25-35% | 50-60%”

- [Our No-Code Apps Made $50M Using THIS Paywall](https://youtu.be/24QMRDXck70?t=296) @4:56 · Superwall · 2025-11-16 · *qualifies* · basis: own experience · conflict of interest: sells agency services, paid community
  > Trial to paid conversion rate, everything above like a 30% is good.

### <a id="k272"></a>K272 · single source · confidence 0.56

Moving the paywall before the sign-up screen in a fitness app raised paywall views from 40% to 94%, and the speaker reports a 190% increase in trial activation and a 52% increase in sales.


- [We’ve Tested 100s of Paywalls. Here’s What Actually Converts.](https://youtu.be/vZXn_BSi5AE?t=880) @14:40 · App Masters · 2026-08-18 · *—* · basis: client data · conflict of interest: sells agency services, sells a course, sponsored
  > the paywall views went up from 40 to 94%

### <a id="k304"></a>K304 · unverifiable · confidence 0.53

Subscription apps running 50+ paywall experiments a year earn about 18.7 times more revenue than apps running just one; this is a correlation, not a tested causal effect.


*Assessment:* The only source is one creator who sells agency services and repeats a figure that appears to come from a paywall-tool vendor's report (Adapty). I found this through search snippets only, so I haven't confirmed the original. The data is vendor-produced and correlational. Apps with more revenue can afford more experiments, so reverse causation and survivorship bias are likely. The allowed official docs (Appcues, Userpilot, ProductLed, Reforge, Intercom) say nothing about this statistic.


*Test with your own data:* Run one paywall or onboarding A/B test at a time on your own traffic for at least 2 weeks (or until about 95% significance). Success metric: trial-start rate and revenue per install versus control. Then judge whether testing cadence pays off for you, rather than relying on the 18.7x figure.


- Official source: [https://appcues.com/blog/from-trial-to-paid-how-we-accelerated-sales-by-68-percent-with-our-very-own-paywall](https://appcues.com/blog/from-trial-to-paid-how-we-accelerated-sales-by-68-percent-with-our-very-own-paywall) — “”

- [I Studied 10,000 Paywall Screens (THIS Makes People Pay)](https://youtu.be/sYRhXB_ZcLI?t=590) @9:50 · Tim Gabe · 2026-05-18 · *supports* · basis: other creator · conflict of interest: sells agency services
  > This crazy gap is between apps that ran 50 plus paywall experiments a year versus apps that ran one.

### <a id="k326"></a>K326 · single source · confidence 0.59

Superwall lets you change a paywall remotely and run A/B tests on it without shipping an app update.


*Assessment:* This is a basic, well-known mechanic of Superwall: the SDK fetches paywalls remotely, so you can edit them and run experiments without a new build. The only member is a single creator who sells agency services, but the claim is a product feature and not an efficacy claim, so that conflict matters little. The allowed official domains (Appcues, Userpilot, ProductLed, Reforge, Intercom) say nothing on it. Superwall's own pages, which are not in the allowed list, describe the same behavior.


- [How I Build Paywalls That PRINT ($44k/Month App)](https://youtu.be/aPug2RqXV-A?t=312) @5:12 · Steven Cravotta · 2026-03-04 · *supports* · basis: own experience · conflict of interest: sells agency services
  > you can remotely change your paywall without shipping an app update

### <a id="k327"></a>K327 · unverifiable · confidence 0.58

Superwall recently launched A/B testing of entire user onboarding flows, so onboarding screens can be tested in the same tool as paywalls.


*Assessment:* This is a single, verbal, general-knowledge statement from one creator who sells agency services and runs a paid community. The allowed official domains (Appcues, Userpilot, Intercom, and so on) say nothing about Superwall. Superwall's own pages, which are outside the allowed list, appear to describe Flows with onboarding A/B testing, so the claim is plausible. I could not confirm the launch date or the details from the allowed sources.


*Test with your own data:* Open your Superwall dashboard and check whether Flows/onboarding experiments are available on your plan. If they are, run one 2-variant onboarding test (for example short vs long) for at least 2 weeks. Measure trial start rate and day-1 return.


- Official source: [https://appcues.com/blog/flow-variation-a-b-testing](https://appcues.com/blog/flow-variation-a-b-testing) — “Unfortunately, user onboarding is still one of the most neglected areas of testing.”

- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=816) @13:36 · Steven Cravotta · 2026-05-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > Superwall just launched AB testing user onboarding flows

### <a id="k328"></a>K328 · unverifiable · confidence 0.68

Superwall reports A/B test results for paywall experiments using Bayesian analysis.


*Assessment:* There is a single source: one creator who sells agency services and runs a paid community, and he states the claim verbally. The allowed official domains (Appcues, Userpilot, ProductLed, Reforge, Intercom) say nothing about Superwall or Bayesian testing. The claim is plausible and low-stakes, but I could not confirm it independently. Superwall's own docs would be the right place to check it, and they are outside the allowed list.


*Test with your own data:* Open the Superwall dashboard or its experiments documentation and check how the experiment results are described. Look for terms such as "probability to be best" or "credible interval". This takes about 5 minutes.


- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=742) @12:22 · Steven Cravotta · 2026-05-29 · *supports* · basis: platform docs · conflict of interest: sells agency services, paid community
  > Superwall will use the testing method, the AB testing method called Bayesian analysis.

### <a id="k341"></a>K341 · single source · confidence 0.57

Onboarding checklists should persist after the user dismisses the initial onboarding flow.


- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=442) @7:22 · Mobbin · 2026-04-16 · *—* · basis: general knowledge
  > Checklists stick around even after the user dismisses the initial flow.

### <a id="k344"></a>K344 · single source · confidence 0.61

Measure drop-off between each onboarding screen, and change or remove any screen with a high drop-off before it reaches the paywall.


- [I Studied 100 Paywalls, Here's What I Found](https://youtu.be/y0f8-CSOJ58?t=816) @13:36 · Steven Cravotta · 2026-05-29 · *—* · basis: own experience · conflict of interest: sells agency services, paid community
  > if one of these screens produced a high drop-off rate, we would either change it or completely remove it.

### <a id="k345"></a>K345 · single source · confidence 0.56

Asking for an app review during onboarding can backfire: some users leave one-star reviews, so the prompt should be used with caution.


- [The app onboarding secrets that convert (proven strategies)](https://youtu.be/QMo2T5apdYw?t=222) @3:42 · Adam Lyttle · 2025-08-08 · *—* · basis: own experience
  > sometimes you'll get a few one-star reviews, so just be cautious.

### <a id="k346"></a>K346 · unverifiable · confidence 0.52

A bad onboarding experience can cause up to 80% of users to leave an app before they even try it.


*Assessment:* The claim comes from a single creator who sells courses and has an affiliate interest. The video gives no source or data for it. The Appcues mobile onboarding statistics page gives no figure for abandonment caused by poor onboarding. Public figures I found are about 21–25% abandoning after one use, which is a different metric. "Up to 80%" is so loose that it can't be checked.


*Test with your own data:* Measure your own install-to-first-key-action rate. Take cohorts over 2–4 weeks, split by whether users saw the new or old onboarding flow, and compare the share who complete the first valuable action within 24 hours.


- Official source: [https://appcues.com/blog/mobile-app-user-onboarding-statistics](https://appcues.com/blog/mobile-app-user-onboarding-statistics) — “”

- [Onboarding Best Practices from 200+ Top Apps!](https://youtu.be/vAN7kmpTdy4?t=737) @12:17 · Elizabeth Alli - DesignerUp · 2025-02-26 · *supports* · basis: general knowledge · conflict of interest: sells a course, affiliate
  > a bad onboarding experience can cause up to 80% of people to leave the app before they even try it

### <a id="k350"></a>K350 · unverifiable · confidence 0.54

Cal AI, a calorie tracking app, reportedly made $35 million in revenue in its first year.


- [How To Solve The App Onboarding Paradox](https://youtu.be/Aa89MC8jX2c?t=147) @2:27 · Tim Gabe · 2026-06-03 · *—* · basis: general knowledge · conflict of interest: sells agency services
  > Cal AI is the calorie tracking app that did $35 million in revenue in its first year.

### <a id="k354"></a>K354 · single source · confidence 0.57

Showing a custom screen before the system notification permission prompt (explaining the benefit) is said to significantly improve notification accept rates.


- [I Studied 1,460 Onboarding Flows. Here's What I Found.](https://youtu.be/Qsq-Sj_rojU?t=442) @7:22 · Mobbin · 2026-04-16 · *—* · basis: general knowledge
  > it improves accept rates significantly.

### <a id="k357"></a>K357 · single source · confidence 0.60

The vendor recommends adding services and activating credit card processing right after the profile setup so the business can be booked and paid.


- [Welcome to Vagaro - Getting Started](https://youtu.be/NoyKf0yzZWs?t=235) @3:55 · Vagaro University | Support · 2026-03-19 · *—* · basis: platform docs · conflict of interest: sells agency services, sells a course
  > Then add your services, classes, and activate credit card processing so you can get booked and paid.

### <a id="k367"></a>K367 · single source · confidence 0.57

New users should be given a minimum viable setup (the smallest set of steps to reach first value) rather than being asked to do everything a power user would do.


- [The Product-Led Growth Playbook for SaaS Startups (Navattic Case Study](https://youtu.be/sO2x9Nbggg4?t=154) @2:34 · Andrew Capland · 2026-10-06 · *—* · basis: own experience · conflict of interest: sells agency services
  > they'll try to have you do everything like a power user would. But new users don't need to behave in the same way as power users.

### <a id="k372"></a>K372 · single source · confidence 0.53

A founder-signed email sent after trial cancellation, asking the user to reply with the reason for cancelling, got a 51% open rate.


- [increase FREE TRIAL TO PAID conversion rate in 18 minutes (mobile apps](https://youtu.be/UnZ2RM2k7FM?t=233) @3:53 · Alim Charaniya · 2025-08-14 · *—* · basis: own experience · conflict of interest: paid community, sells agency services, affiliate
  > I've gotten a 51% open rate on this email.