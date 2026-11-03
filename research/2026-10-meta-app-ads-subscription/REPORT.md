# Meta Advantage+ app campaigns for B2B subscription trials on a small budget

## Short answer
The best-supported advice is to optimize the campaign for StartTrial rather than installs [K2](#k2). Feed it from one consolidated campaign with a broad ad set and a handful of clearly different creatives [K1](#k1) [K3](#k3) [K6](#k6). Keep automatic "highest volume" bidding [K24](#k24), and judge results by cost per trial and then by cost per paying customer, not by cost per install [K11](#k11) [K36](#k36). The main constraint on a small budget is event volume. Meta needs roughly 50 optimization events per ad set per week to leave learning, so the weekly budget should be about 50 × your cost per trial [K10](#k10) [K23](#k23). If you can't afford that, a purchase or paid-subscription event is usually out of reach, and StartTrial is the realistic target [K2](#k2) [K58](#k58).

Most of this is backed by Meta's docs or broad agreement. However, nearly all sources sell courses, agency services or tools, and very little first-hand data comes from B2B subscription apps running app campaigns. Most practitioner evidence comes from consumer apps, ecommerce (often Turkey) and B2B lead generation. Treat the mechanics as solid. Treat the numbers and the efficacy claims as hypotheses to check against your own data.

## What the platform says vs what practitioners report
No cluster has first-hand practice directly contradicting the docs. The gaps below are where practitioners add advice the docs don't cover (practice_only). One creator claim is contradicted by the docs: see [K405](#k405) under Platform facts.

| Topic | Platform / docs | Practitioners (first-hand) | When each one applies | Clusters |
|---|---|---|---|---|
| Account structure | Docs: Advantage+ app campaigns use one ad set with several ads. Docs give no recommendation on consolidating | One campaign, one broad ad set, many creatives. "Let the creative do the targeting" | Consolidation matters most when weekly events are scarce. With more budget, several ad sets can work | [K3](#k3) [K65](#k65) [K1](#k1) |
| Higher-intent trial signal | Docs say nothing on "qualified trials". They require about 50 events per week | Send a "qualified trial" (not cancelled within 1–3 h) or a custom value event instead of raw trials | Only if the filtered event still reaches about 50 events per week | [K7](#k7) [K36](#k36) |
| Creative testing structure | Docs say nothing on how spend is split between ads | Test each creative in its own fixed-budget ad set (ABO), then move winners to Advantage+ or CBO | ABO testing splits a small budget. The ecommerce examples may not carry over to app campaigns | [K42](#k42) [K30](#k30) |
| Budget scaling | No official % threshold | Raise 10–20% every 2–4 days. With low volume, wait 7–10 days between changes | Slower cadence when there are few conversions | [K16](#k16) |
| Metric for judging creatives | Docs separate install optimization from event optimization but say nothing on CPI as a KPI | CPI is a poor yardstick. Use cost per trial or purchase | Always, once trial data exists | [K11](#k11) |
| Tracking cross-check | Docs say nothing on App Store Connect comparison | Compare Meta installs and trials with App Store Connect. A gap of about 5–15% is normal | iOS apps | [K74](#k74) |
| Targeting | Advantage+ app allows only limited targeting (geo, language, minimum age, exclusions) | Broad targeting matches or beats interest stacking | Large addressable market, no ABM, not local | [K9](#k9) [K370](#k370) |
| Vertical 9:16 creatives | Docs pages unavailable | Square assets in Stories/Reels get cropped or underperform, so make 9:16 versions | When Stories/Reels placements are on | [K81](#k81) |
| Onboarding/paywall | Docs say nothing | The funnel often matters more than tweaks in Ads Manager | Self-serve paywall in the app. Evidence comes from consumer apps | [K28](#k28) [K40](#k40) [K39](#k39) |
| Adding tier-1 countries | Docs say nothing on cost by country | Adding CA/UK/AU/NZ to the US lowers CPI | Weak if your paying B2B buyers sit in specific markets | [K29](#k29) |

**Where docs and practitioners agree:** deep-funnel event optimization brings more payers than install optimization [K2](#k2). Test one variable at a time [K77](#k77). Cross-check Ads Manager against Events Manager [K458](#k458). Keep a steady supply of new creatives [K18](#k18). Mix creative formats [K41](#k41). Use about 50 events per week as the learning benchmark [K10](#k10). Use default automatic bidding while learning [K24](#k24).

## Levers
Ranked by expected impact on trials and paying customers on a small budget.

1. **Choose the right optimization event.** Optimize for StartTrial, not installs. Move to Purchase or Subscribe only when volume allows [K2](#k2) [K58](#k58). Expected effect: installs cost more, but more of those users become trials and payers. Raw trials can still include people who cancel right away [K36](#k36). Evidence: well_supported for StartTrial over installs. The qualified-trial step is only likely [K7](#k7), and the purchase threshold is contested [K58](#k58).
2. **Match budget to event volume and leave learning alone.** Set the weekly budget at about 50 × cost per trial [K10](#k10) [K23](#k23) [K83](#k83) [K64](#k64). Avoid significant edits while the campaign learns [K63](#k63) [K378](#k378). Expected effect: the campaign leaves "Learning limited" and delivery stabilizes. Evidence: well_supported in the docs. The exact thresholds are rules of thumb.
3. **Get the conversion signal right.** Fire StartTrial through the SDK or an MMP [K8](#k8) [K428](#k428). Send events within an hour [K356](#k356). Reconcile the counts across sources [K458](#k458) [K74](#k74). Expected effect: without a clean signal, optimization can't work [K27](#k27). Evidence: well_supported for the mechanics. One viewer comment reported a large iOS undercount (55 actual trials vs 27 shown by Meta) [K8](#k8).
4. **Creative diversity and steady supply.** Use a few clearly different concepts (hook, angle, format, pain point) rather than near-duplicates [K6](#k6) [K45](#k45) [K71](#k71) [K41](#k41). Refresh in small weekly batches [K18](#k18) [K19](#k19). Expected effect: post-Andromeda, this is the main lever you control directly. Evidence: well_supported in direction. Volume figures such as 50/month or 25+/week come from large-budget accounts [K18](#k18) [K76](#k76).
5. **Consolidated structure.** One campaign, one broad ad set, roughly 3–10 creatives, with the lower end on small budgets [K1](#k1) [K3](#k3) [K65](#k65). Expect spend to concentrate on one or two ads [K4](#k4) [K72](#k72). Evidence: well_supported or likely. How many creatives is best is not settled.
6. **Paywall and onboarding.** These cap how many installs can become trials and payers [K28](#k28) [K40](#k40) [K39](#k39). Evidence: likely, but from consumer apps, and the size of the effect is unverified.
7. **Unit-economics judgment.** Judge by cost per paying customer against gross-margin LTV, with about 3:1 LTV:CAC as a convention [K11](#k11) [K13](#k13) [K60](#k60). This doesn't change delivery, but it decides when to scale or stop.
8. **Scaling cadence.** Increase gradually [K16](#k16). Exactly how big a jump resets learning is contested [K26](#k26).

## Practical recipe
1. Confirm the setup. The App promotion objective needs an app [K79](#k79). Events must be sent through the SDK and/or an MMP [K8](#k8), because app campaigns optimize on in-app events [K428](#k428) [K364](#k364). On iOS you may need to start with an app-installs setup. The event optimization option appears once Meta has received StartTrial events [K37](#k37). Send events in real time, or at least within 1 hour [K356](#k356).
2. Validate tracking before spending seriously. Compare Ads Manager with Events Manager [K458](#k458). On iOS, compare against App Store Connect and expect a gap of about 5–15% [K74](#k74). A gap above roughly 30% between backend trials and Meta's StartTrial count means you should fix the SDK or event setup first [K8](#k8).
3. Size the budget: weekly budget ≈ 50 × your expected cost per trial [K10](#k10) [K23](#k23) [K83](#k83). If you can't afford that, keep StartTrial as the event rather than Purchase [K2](#k2) [K36](#k36), and expect a longer learning phase [K64](#k64).
4. Build one campaign with one broad ad set, a daily budget and no end date [K3](#k3) [K65](#k65) [K32](#k32). Use default "highest volume" bidding with no bid or cost caps [K24](#k24).
5. Load 3–10 clearly different creative concepts, toward the lower end on a small budget [K1](#k1) [K6](#k6) [K45](#k45). Mix formats such as talking head, static and podcast/B-roll [K41](#k41). Add 9:16 versions [K81](#k81). Try rough or native-looking ads [K56](#k56) [K54](#k54) with a strong hook in the first ~3 seconds [K15](#k15). Supply several primary texts and headlines, up to 5 each [K22](#k22). Source ideas from the Meta Ad Library [K5](#k5) and from your best organic posts [K21](#k21).
6. Launch and leave it for about 7 days with no significant edits [K63](#k63) [K378](#k378). Check the Delivery status (Learning / Learning limited) [K23](#k23). Don't kill low-spend creatives immediately [K68](#k68). Base any kill rule on your cost per trial (e.g. 10–20× target CPT), not a flat $100 [K75](#k75).
7. Judge on cost per StartTrial first, then on cost per paying customer and trial-to-paid rate. Don't use CPI [K11](#k11) [K36](#k36). Compare against gross-margin LTV, using about 3:1 LTV:CAC as a reference [K13](#k13).
8. Add a small batch of new distinct concepts each week and retire clear losers [K18](#k18) [K71](#k71) [K19](#k19).
9. Scale in steps of about 10–20% every 2–4 days. On low volume, wait 7–10 days between steps [K16](#k16).
10. In parallel, work on the paywall and onboarding [K28](#k28) [K40](#k40) [K39](#k39).
11. Once raw trial volume comfortably exceeds about 50 per week, test a qualified-trial event [K7](#k7).

## How to proceed: validate with your own data
Run these in order. Each test should change one thing only [K77](#k77).

1. **Tracking baseline (week 0–4).** Record Meta StartTrial alongside backend and App Store Connect counts each week [K74 test](#k74) [K8 test](#k8). Decision: if the gap is under about 15% and stable, proceed. If it's above about 30% or erratic, fix the SDK or MMP before running any other test.
2. **Event choice (2 weeks, equal budgets).** Run installs against StartTrial optimization [K2 test](#k2). If 50 × CPT is unaffordable, compare StartTrial against a cheaper upstream event [K10 test](#k10) [K64 test](#k64). Metric: cost per paying subscriber. Decision: keep the event with the lower cost per payer, even if its CPI is higher.
3. **Creative count and diversity (≥7 days, same budget).** Run 4–5 concepts against 10 [K1 test](#k1). Separately, run distinct angles against visual variants of a single angle [K45 test](#k45). Metric: cost per StartTrial and spend share per creative. Decision: if most creatives get almost no spend, use fewer.
4. **Testing structure (7 days).** Run 3 creatives in separate fixed-budget ad sets against the same 3 in one Advantage+ campaign [K42 test](#k42) [K4 test](#k4). Decision: keep ABO for testing only if Advantage+ spend is heavily skewed and its cost per trial is no better.
5. **Qualified trial (2–3 weeks), only once volume allows.** Run raw StartTrial against the qualified-trial event [K7 test](#k7) [K36 test](#k36). Metric: cost per paid subscriber. Decision: switch only if the qualified event still reaches about 50 events per week.
6. **Paywall/onboarding (2 weeks, ad spend held constant).** Make one change, such as placement or flow length [K28 test](#k28) or the trial presentation [K39 test](#k39). Metric: paywall-to-trial rate and cost per StartTrial.
7. **Secondary settings (7–14 days each).** Test Advantage+ placements against Instagram-only [K12 test](#k12), creative enhancements on against off [K67 test](#k67), and copy length [K73 test](#k73). Keep a setting only if cost per trial and trial-to-paid both hold up.
8. **Scaling cadence (2 + 2 weeks).** Compare +15% every 3 days with a 7-day cadence [K16 test](#k16), and a 20% step with a 50% step [K26 test](#k26). Metric: learning status and cost per trial.

At small volumes, call a result inconclusive below roughly 30–50 events per arm. Several tests above use this threshold.

## Contested and conditional points
- **Narrow vs broad** [K17](#k17). Ben Heath says niche down. The Turkish agencies say keep targeting broad. They probably mean different things: a narrow niche in the *message* versus narrow *audience settings*. In Advantage+ app campaigns, audience control is limited anyway [K370](#k370).
- **Placements** [K12](#k12). Instagram-only comes from local-service message campaigns in Turkey. For app objectives, the default all-placements setting is the more plausible starting point.
- **Creative enhancements** [K67](#k67). One view keeps them on and disables only text and translation. The other disables everything for control. For a B2B app where wording must be accurate, at least check the text enhancements.
- **When to move to Purchase optimization** [K58](#k58). One creator says 50 events in 2 weeks; the usual figure is about 50 per week. Thresholds are rules of thumb.
- **Budget jump that resets learning** [K26](#k26). Somewhere between 20% and 50%, with no official figure.
- **Learning duration** [K84](#k84). "24–48 hours" holds only with enough volume. Commenters on small budgets report being stuck for over a week.
- **Creative vs signal as the main lever** [K27](#k27). Signal quality is a precondition. Creative is what you iterate on once the signal works.
- **SDK-only vs SDK + CAPI** [K38](#k38). SDK-only is enough for in-app StartTrial. Paid conversions and renewals happen off-device and need server-side events.
- **Copy length** [K73](#k73). Short vs long copy. Neither side shows data.
- **Separate test and scale campaigns** [K61](#k61). On small budgets, false winners are likely.
- **Weekly creative volume** [K76](#k76). "25+ per week" applies to high-spend accounts only.
- **CAC ceiling** [K44](#k44) [K13](#k13). The offer price is only a break-even on the first sale. The 3–4x LTV:CAC figure depends on margin, churn and cash.
- **Meta as the best platform for subscription apps** [K85](#k85). This comes from agency client bases in consumer apps.
- **B2B demo benchmark of $150–200** [K78](#k78). This is for lead-gen or booked calls. It doesn't apply to StartTrial.

## Platform facts
- Advantage+ app campaigns use one ad set with several ads. App campaigns optimize for installs or in-app events, including custom events [K1](#k1) [K428](#k428) [K364](#k364).
- On iOS the app-installs setup is required, and app-event optimization needs the events set up first. No volume threshold is documented [K37](#k37).
- The learning phase needs about 50 optimization events per ad set per week [K10](#k10) [K83](#k83) [K23](#k23). Significant edits restart it [K378](#k378).
- Lowest-cost bidding spends the full budget. Bid caps need more management and may underspend [K24](#k24).
- Campaign budget (Advantage campaign budget) shifts spend in real time across ad sets [K374](#k374) [K445](#k445) [K263](#k263). The concentration effect inside a single ad set is reported by practitioners but not documented [K4](#k4).
- Advantage+ audience controls (location, minimum age, language, exclusions) are hard limits. Suggestions are only signals [K370](#k370).
- Default placements include Audience Network [K53](#k53).
- Ads Manager counts only attributed, deduplicated events. Events Manager counts all events received [K458](#k458).
- Send events in real time, or within 1 hour. Delays of 24 hours or more hurt [K356](#k356).
- Value optimization needs a value sent with each event [K170](#k170). AEM and SKAdNetwork are separate attribution choices [K159](#k159).
- **pLTV:** requires about 100 conversions per week, allows one event per dataset, and per current docs runs on web CAPI only, with no app events [K295](#k295). **Contradicted by docs:** the claim that pLTV works for app subscription campaigns via CAPI "surviving ATT" [K405](#k405).
- Other supported mechanics: Andromeda's self-reported figures (about 3x throughput, +6% recall) [K192](#k192). Using an existing Instagram post as the creative [K57](#k57). Image-to-video enhancement (9:16 output not confirmed) [K353](#k353). The AI recommendations assistant in Ads Manager [K272](#k272). Special ad categories, relevant only to fintech or recruiting apps [K49](#k49). A payment failure pauses ads [K273](#k273).
- "Automated App Ads" was renamed Advantage+ app campaigns, not removed. Hook and hold rate are custom metrics you build from video-play columns [K215](#k215) [K416](#k416).

## Single-source but notable
Unconfirmed. Each item comes from one source, mostly stated verbally.
- Sending trial starts as a Trial event instead of Purchase lowered one audited app's cost per trial by about 35% without changing ads [K187](#k187).
- A review of 100 accounts found that a single CBO campaign with one ad group and many creatives succeeded 21% of the time at small budgets, 16% at mid and 14% at high [K87](#k87). In the same review, accounts with high creative diversity did better [K341](#k341), and fully AI-generated ads failed [K342](#k342).
- Clickbait ads that get cheap trials can sharply cut trial-to-paid, so check trial-to-paid per ad [K391](#k391).
- Measure a trial-to-paid baseline for cold paid traffic (about one month) before scaling [K269](#k269). In one B2C fitness app, trial-to-paid was about 25% from Meta vs 35–40% from organic [K107](#k107).
- Sending traffic to a web quiz converted better than going straight to the App Store, on iOS only [K468](#k468) [K282](#k282). Another speaker says a quiz never worked for their app [K396](#k396).
- An annual-first paywall moved the mix from about 60/40 monthly/annual to 75–80% annual [K286](#k286). A no-trial option did worse than the free trial [K166](#k166).
- Skit-style UGC halved cost per trial ($60 → $30) for a consumer app [K207](#k207). Founder-recorded content performed well across one agency's clients [K212](#k212).
- App Store Connect path for trial starts: Analytics > Metrics > Subscriptions > Events > Offer starts, filtered to free trials [K408](#k408).
- After Andromeda, one creator gets better results with ad-set-level budgets [K375](#k375). Another says pLTV signals didn't help when the model behind them was poor [K146](#k146).
- Warm up a new ad account with engagement campaigns before running conversion campaigns [K274](#k274).

## From the comments
Not verified.
- Check Meta's trial count against store data regularly to see how much attribution you're losing. Reconcile before spending on any other channel.
- Treat CAC as valid only when it's cost per *paying* user. The 3:1 rule fails when CAC is measured per install.
- Calculate cost per subscriber from your real CPI. At $3 CPI and 21 subscribers per 1,000 installs, that's about $143, not about $95.
- Scale only after checking trial-to-paid and month 2–3 retention, because early LTV is an estimate.
- Optimize on StartTrial or a qualified trial rather than purchase, because SKAN postbacks arrive 1–2 days late.
- Advantage+ creative enhancements can silently switch back on when you edit an ad, so recheck them after each edit.
- Advantage+ often puts nearly all spend on 1–2 creatives.
- Rule of thumb: about 2–3 conversions per creative per week, so the number of creatives should follow your weekly conversion count.
- In GDPR markets, check consent requirements before adding an SDK.

## Filtered out: sales, hype, unverifiable
- **Offers in the corpus:** agency done-for-you services and paid audits, coaching or "advisory" calls, paid Skool and Telegram communities, courses and academies, creators' own SaaS tools (attribution, ad-creation, AI creative generators with discount codes), a UGC sourcing platform, DM lead magnets, and sponsor reads. Many "levers" come from these sellers, which is why they were scored down.
- **Income and outcome claims** were treated as marketing, not benchmarks: small-budget campaigns producing large MRR [K20](#k20), agency ROAS or pipeline figures [K154](#k154) [K257](#k257) [K258](#k258) [K421](#k421), subscriber testimonials [K132](#k132) [K133](#k133), an app's sales vs ad spend [K390](#k390), and CPI figures from single accounts [K66](#k66) [K435](#k435) [K437](#k437).
- **Unverifiable benchmarks** to be careful with: "$10–15 per trial" [K389](#k389), install-to-trial of 5–10% [K104](#k104), paid intro offers reaching 60–70% trial-to-paid [K105](#k105), an "LTV ≥ $3 per install" rule [K386](#k386), an "LTV ≥ $100" rule [K418](#k418), frequency cutoffs [K111](#k111), IPM ranges [K473](#k473) [K86](#k86), and the claim that "Meta favors statics" [K402](#k402), which commenters contradict.

## Limits
- The sample is 35 videos from 26 channels. Almost all speakers sell something, and on-screen data is rare.
- Very little evidence comes from actual B2B subscription apps on Advantage+ app campaigns. Much of it is from consumer apps, Turkish ecommerce, message campaigns, or B2B lead-gen and booked-call funnels.
- Languages are mainly English and Turkish, with some Spanish and Hungarian. Currency figures (TRY, HUF) don't transfer.
- Survivorship bias: creators show what worked and rarely show failed accounts.
- The Meta UI, Andromeda behavior and pLTV availability change often. Several docs pages could only be read as titles or search summaries.
- This report reflects the videos available on 2026-11-03. Re-run it in 3–6 months.


---

## Evidence appendix

Source videos and the moment each claim is made, for every cluster the report cites. Band and confidence are computed by code (rubric `r3`).


### <a id="k1"></a>K1 · well supported · confidence 0.85

In a Meta app promotion (Advantage+ app) campaign, put several creatives (roughly 3–10 or more) in one ad set instead of splitting them one ad per ad set.


*Assessment:* Most creators agree on several creatives in one ad set, but recommendations range from 3 to 20+ and rest on opinion or general knowledge, mostly from people selling agency services or courses. The docs say Advantage+ app campaigns use one ad set with multiple ads, with a limit of 50 creative combinations, but give no recommended count, so they are silent on the number. Two members recommend one ad per ad set. One is an ABO isolated-testing structure and the other is a messages campaign where the creator is sure of the creative. Those are different setups from Advantage+ app, so they contradict only partly. The only first-hand evidence comes from ecommerce in Turkey and B2B leads in Hungary, and neither is app install or trial data. A small budget probably favors the lower end, because budget concentrates on one or two creatives anyway.


*Test with your own data:* Run one campaign with 4–5 distinct creative concepts and another with 10 for at least 7 days at the same budget. Compare cost per StartTrial and the share of spend that goes to each creative. If most creatives get almost no spend, use fewer.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “Manually test up to 50 creative combinations.”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1403) @23:23 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > I recommend testing at least 10 in a campaign.

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=1747) @29:07 · Aprendamos Marketing · 2026-01-13 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > yo aquí igual te digo mínimo, te recomiendo que agregues cinco anuncios

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=79) @1:19 · Burak Mermi · 2026-02-16 · *supports* · basis: platform docs · conflict of interest: sells a course
  > More than 20 creatives, for example.

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=1154) @19:14 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > I've now come up with three to five different ad concepts that I can just put into one ad set in meta and let the algorithm do its thing

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=544) @9:04 · Menaf Avcı · 2025-12-28 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Her reklam setinin altına 3-7 arası kreatif ekleyebiliriz.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1097) @18:17 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Adset'in içerisinde de en az 5 tane 5 tane'den fazla da olabilir bu arada.

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=544) @9:04 · Menaf Avcı · 2025-12-28 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Eğer ki reklam bütçeniz çok yüksek değilse bu kitleleri aynı reklam setinin içerisinde de kullanabilirsiniz.

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=1297) @21:37 · Gürkanzone · 2026-08-15 · *qualifies* · basis: own experience · conflict of interest: sells a course
  > Bak tek bir set içerisinde 10 tane kreatif var.

- [1500+ B2B lead Meta Ads-ből ~620 Ft/lead kampánnyal [ESETTANULMÁNY]](https://youtu.be/OW74dQjjOBo?t=242) @4:02 · Fluid Digital · 2025-12-16 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > 21 különböző kreatívot használtunk híret és sorozatonként, amelyek mindegyike, három különböző méretben volt létrehozva

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=696) @11:36 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > don't put one ad per ad set. Please maybe bundle them three to five per ad set because it's easier to manage.

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1166) @19:26 · Nida Yıldırım · 2026-04-29 · *contradicts* · basis: own experience · conflict of interest: sells agency services
  > Eğer ki kreatifiniz yani reklam videonuz kuvvetliyse ve eminseniz tek bir reklam seti ve tek bir reklam olarak devam etmelisiniz.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=467) @7:47 · Burak Mermi · 2026-07-06 · *contradicts* · basis: other creator
  > Her reklam grubunda tek bir reklam test ediliyor

### <a id="k2"></a>K2 · well supported · confidence 0.97

For subscription apps on Meta, optimize for a deeper-funnel event (trial start or purchase) rather than installs, because installs are cheaper but bring fewer payers.


*Assessment:* Several channels agree, and the Meta docs describe event optimization as reaching people likely to take the chosen action. Only one member (Cravotta) shows first-hand data, and he sells a course. The others are general knowledge or repetition of other creators. The claim holds only when there is enough event volume (roughly 50 events per week per ad set), so a small budget may need a shallower event such as trial start rather than purchase. The Adapty client-data member also says to avoid cost caps and use value optimization, which goes beyond the core claim.


*Test with your own data:* Run two campaigns for 2 weeks with equal budget: one optimized for installs, one for trial start. Compare cost per trial and cost per paid subscriber, not cost per install.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “The difference is that your ads reach people most likely to take the action you specify”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1015) @16:55 · Steven Cravotta · 2026-07-30 · *supports* · basis: own experience · conflict of interest: sells a course
  > the cost per install was double on this free trial optimized campaign, but ultimately it ended up being more profitable for us

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=459) @7:39 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > if you optimize for installs, you might get a cheap install, maybe a dollar to $2, but nobody pays

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1259) @20:59 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > it could end up 10, 20% install to paid ratio on a purchase campaign on Meta.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=389) @6:29 · Sub Club by RevenueCat · 2026-09-15 · *supports* · basis: other creator
  > I haven't seen a case where an install optimized campaigns got anywhere near the performance of a deeper funnel event

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=238) @3:58 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > Most likely if you're running a hard paywall consumer app, you want to optimize for purchase.

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1093) @18:13 · Steven Cravotta · 2026-07-30 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > One thing you absolutely never want to do is optimize only for clicks or landing page views.

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1177) @19:37 · App Leaders by Adapty · 2025-12-26 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > I would definitely optimize for purchase and trial.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1431) @23:51 · App Leaders by Adapty · 2026-09-11 · *qualifies* · basis: client data · conflict of interest: sells agency services
  > Please do not use cost gaps. Do not use cost per purchase optimizations.

### <a id="k3"></a>K3 · likely · confidence 0.79

For an app-install/event campaign on a small budget, consolidate into one campaign with one broad ad set and many creatives, letting the creative do the targeting, rather than splitting into many campaigns, ad sets or narrow audiences.


*Assessment:* Most members, including Cravotta, Heath, Menaf Avcı, Adapty and Gui Costa, repeat the same consolidation and broad-targeting advice. All are general knowledge or one's own experience, with no data shown, and most sell courses or agency services. Meta's "About learning limited" page appears, from a search summary, to suggest consolidating ad sets and broadening audiences to reach about 50 optimization events a week. My fetch of that page returned only its title, so I could not quote it and I rate the docs as silent. The advice is plausible on a small budget, where a trial or purchase event is rare. After Andromeda, creative diversity matters more. Kamil's two claims are descriptive: C16 only describes the campaign and ad set structure, and C5 notes that Advantage+ audience can be turned off, which is a different route from broad targeting.


*Test with your own data:* Run one campaign with one broad Advantage+ ad set and 6-10 distinct creatives. Run it for 2 weeks at your current total budget and compare it with your existing split setup. Success is a lower cost per StartTrial, and more than 50 optimization events a week in the ad set.


- Official source: [https://en-gb.facebook.com/business/help/269269737396981](https://en-gb.facebook.com/business/help/269269737396981) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=310) @5:10 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > You need one campaign, one ad set, and a lot of creatives in that ad set.

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=388) @6:28 · Menaf Avcı · 2025-12-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Burada amacımız hedef kitleye oynamak değil, kreatifi daha fazla konuşturmak.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=865) @14:25 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Çok fazla kampanya açmak içeride çok fazla etset açmak.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1525) @25:25 · Ben Heath · 2026-02-20 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > Don't have lots of different campaigns. Don't have lots of different ad sets.

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=233) @3:53 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > Broad targeting wins, which is great for you and me.

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=75) @1:15 · Gui Costa · 2026-07-25 · *supports* · basis: own experience · conflict of interest: sells agency services
  > you need to call out your audience and you need to use your creative as the target

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1565) @26:05 · Kamil YILDIRIM · 2026-05-31 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Fakat biz burada dilersek bu özelliği kapatabiliyoruz.

### <a id="k4"></a>K4 · well supported · confidence 0.91

With campaign-level budget (CBO / Advantage+ campaign budget), Meta automatically concentrates spend on the ad sets or ads it predicts will convert most easily or cheaply. This can starve other ad sets or creatives, and that choice does not always match what the advertiser sees as better performance.


*Assessment:* Several members agree on the basic mechanic: CBO concentrates budget where Meta predicts the easiest results. Two of them (Ben Heath, Kamil Yıldırım) only describe the neutral mechanic of distribution. Only Gui Costa shows first-hand screen evidence of Meta favouring a worse ad, and he sells agency services. The Burak Mermi comments add experiential confirmation (one creative taking all spend, one ad set dominating). The claim that Meta's choice is wrong, as opposed to just uneven, rests on thin evidence, and the fetched help page returned no usable text. The "split high prices into separate campaigns" advice and the "existing customers get the budget" claim are heuristics from general knowledge, not tested.


*Test with your own data:* Run the same creatives in two setups for at least 7 days with an equal total budget: one campaign with all creatives in a single ad set (CBO), and one with each creative in its own ad set on a fixed budget (ABO). Compare cost per trial start and the share of spend each creative gets.


- Official source: [https://www.facebook.com/business/help/153514848493595](https://www.facebook.com/business/help/153514848493595) — “”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=304) @5:04 · Gui Costa · 2026-07-25 · *supports* · basis: own experience · conflict of interest: sells agency services
  > And here G's one, 25 cents per click and G's one is doing pretty bad, right?

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=890) @14:50 · Ben Heath · 2026-01-06 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > budget will be distributed to those ad sets according to performance.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1251) @20:51 · Kamil YILDIRIM · 2026-05-31 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Bütçenizin aslında otomatik olarak reklam setlerine dağıtılmasını istiyorsanız bu seçenek üzerinden ilerleyebilirsiniz.

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=698) @11:38 · Menaf Avcı · 2025-12-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > meta bütçenin çoğunu bu kampanya yapısı olmadan en kolay dönüşümlere, yani eski müşterilere yönlendirir.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=543) @9:03 · Burak Mermi · 2026-07-06 · *supports* · basis: general knowledge
  > Meta en kolay bir şekilde satabileceği reklam grubuna ağırlık vererek bütçeyi orada yoğunlaştırabilir

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2175) @36:15 · Burak Mermi · 2026-07-06 · *qualifies* · basis: general knowledge
  > yüksek fiyatlı ürünlerinizi farklı CBO kampanyasında değerlendirebilirsiniz

### <a id="k5"></a>K5 · well supported · confidence 0.83

Use the Meta Ad Library to research competitors' ads (creatives, copy, formats), and treat ads that have run for months as likely winners to borrow hooks and angles from.


*Assessment:* All five members agree the Ad Library is a useful way to see competitors' creatives, and this is a low-risk research step. The "long-running means winner" inference is a heuristic that none of them back with data. The library shows no spend, conversions or ROAS for commercial ads, and an ad can run a long time without being profitable. The evidence is mostly general knowledge from creators who sell courses or agency services. I could not retrieve the official page text, so the docs check is silent.


*Test with your own data:* Pick 5 competitor ads that have run for 3 months or more and 5 newer ones. Build similar hooks for each and run them for 7–14 days at the same budget. Compare cost per trial (StartTrial) between the two groups to see whether the longevity signal helps.


- Official source: [https://www.facebook.com/business/help/2405092116183307](https://www.facebook.com/business/help/2405092116183307) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=546) @9:06 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > Alternatively, you can also go to the Facebook ads library.

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=993) @16:33 · Gürkanzone · 2026-08-15 · *supports* · basis: own experience · conflict of interest: sells a course
  > Reklam kütüphanesine gireceksiniz.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=763) @12:43 · Ben Heath · 2026-02-20 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > you can see the primary text, you can see where they're running, you can see the videos themselves

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=771) @12:51 · App Masters · 2026-10-20 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > you're going to try to find something that has been running for a long time

- [How to build a $100k MRR B2B SaaS business with ads](https://youtu.be/NMl7-u2UaRk?t=75) @1:15 · Denis Shatalin · 2025-11-03 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > if you can filter for the ads which are running for more than three, four, six months, most likely they are making money with them.

### <a id="k6"></a>K6 · likely · confidence 0.78

When testing ads on Meta, test clearly distinct creative concepts (different hooks, angles, formats, pain points) rather than several near-identical variations of the same ad.


*Assessment:* Five channels agree, which fits Meta's general push for creative diversification after Andromeda. However, most rest on general knowledge with no screen-shown data, and several creators sell agency services or courses. Only AdConversion claims first-hand experience, and it gives no data. Meta's docs mention a diversification strategy but say nothing specific about distinct versus near-duplicate ads. The direction is plausible and uncontested.


- Official source: [https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance) — “as businesses upload more and more creatives to support a diversification strategy”

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=476) @7:56 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > When you start, don't mix five slightly different versions of the same ad.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1181) @19:41 · Burak Mermi · 2026-07-06 · *supports* · basis: general knowledge
  > Örneğin 3 tane görsel eklediniz, 3 tane de video eklemeniz gerekiyor

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=924) @15:24 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > We want to test out different concepts, right?

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=469) @7:49 · AdConversion · 2025-11-12 · *supports* · basis: own experience · conflict of interest: sells a course, sells agency services
  > That is what we're seeing actually move the needle for meta.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=633) @10:33 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > launch a lot of different static ads as well with different pain points, different desired outcomes, different features

### <a id="k7"></a>K7 · likely · confidence 0.71

To optimise Meta delivery toward paying subscribers, send Meta a higher-intent trial signal (e.g. a 'qualified trial' that is not cancelled within 1–3 hours, or a custom value event) rather than every raw trial start.


*Assessment:* Most members describe the same tactic, and several repeat the same vendor feature (Adapty/RevenueCat Qualified Trials). Those members are mostly general knowledge or other-creator content from vendors that sell tooling or agency services, so they are not independent evidence. Only the Sub Club member (EyoYQU6JyV8:C7) is first-hand, and it shows no data. Meta's docs say nothing specific about qualified-trial events. They do warn that an optimisation event must occur about 50 times a week per ad set, so a stricter filter can starve learning on a small budget. The no-trial-paywall member (kXXFtl0ocU0:C19) is a different tactic that also changes the product, so it only partly fits this claim.


*Test with your own data:* Run two ad sets for 2–3 weeks with the same creative and budget. One optimises on raw StartTrial and the other on the qualified-trial event. Compare cost per paid subscriber (or trial-to-paid rate), and check that the qualified-trial ad set reaches about 50 events per week.


- Official source: [https://en-gb.facebook.com/business/help/269269737396981](https://en-gb.facebook.com/business/help/269269737396981) — “If your budget is too low to receive around 50 optimisation events, the ad set is unlikely to exit the learning phase.”

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1812) @30:12 · App Leaders by Adapty · 2025-12-26 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > showing meta users no trial paywalls, because I need that signal

- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1354) @22:34 · Sub Club by RevenueCat · 2026-09-02 · *supports* · basis: own experience
  > and we're feeding the highest intent users back to Meta.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1583) @26:23 · App Leaders by Adapty · 2026-09-11 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > combining as custom events and sending some, I wouldn't say PLTV, but some kind of value to your trial

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1097) @18:17 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > You can create a custom event, which says, for instance, trial started, but not canceled in the same hour.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1249) @20:49 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > we check if after two hours the user didn't cancel the event okay if the trial started is still active then we will count that as a trial qualified

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1185) @19:45 · App Leaders by Adapty · 2026-09-11 · *supports* · basis: other creator · conflict of interest: sells agency services
  > We are just sending the signals if the user didn't cancel the trial in three hours.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1496) @24:56 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Bir saat ya da iki saat içerisinde iptal etmeyen kullanıcıların sinyalini metaya gönderelim.

### <a id="k8"></a>K8 · likely · confidence 0.80

To measure installs and in-app events (such as free trials) for a Meta app campaign, especially on iOS, the app needs the Meta SDK and/or an MMP integration. Tracking does not work out of the box.


*Assessment:* Most members agree that you need an SDK or an MMP to get conversion data on iOS, and none of them contradicts that. The "SDK is mandatory" version (C7) is too absolute, because Meta also accepts MMP integrations (the install referrer page lists a direct option and an MMP option). The Meta page I fetched doesn't say that either an SDK or an MMP is required. All members are general knowledge with no screen-shown data; several creators sell courses or agency services. The viewer comment on C12 (55 actual trials vs 27 reported by Meta) shows that even with tracking set up, iOS AEM undercounts. C14 is about X and Reddit, so it doesn't belong in this cluster.


*Test with your own data:* Compare your backend or app-store count of free trials with the StartTrial count in Ads Manager over 7 days. If the gap is above ~30%, check your SDK event setup and consider adding an MMP.


- Official source: [https://developers.facebook.com/docs/app-ads/meta-install-referrer](https://developers.facebook.com/docs/app-ads/meta-install-referrer) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=862) @14:22 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > you can't just launch a campaign for a mobile app and the tracking just works out of the box.

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=862) @14:22 · Steven Cravotta · 2026-07-30 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > Facebook and TikTok will try to take credit for the installs and the events that you send on each one of their platforms.

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=317) @5:17 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > First, implement the meta SDK, set up your important conversion events and start running SDK conversion campaigns right away.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=155) @2:35 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > I recommend you to just use the Facebook SDK if this is your very first campaign.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=85) @1:25 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > For iOS, you need to connect SDK. So if you don't, you don't have results.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=85) @1:25 · Gui Costa · 2026-07-28 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > If you don't have an SDK installed, you cannot run app install campaigns.

### <a id="k9"></a>K9 · likely · confidence 0.68

For Meta ads (including B2B SaaS), broad or open targeting that lets Meta's algorithm find the audience generally performs as well as or better than tight interest stacking, though it is worth testing the two against each other.


*Assessment:* Four independent practitioners lean toward broad or open targeting, but all of them sell courses or agency services. None shows data on screen. Shatalin recommends testing both options, and AdConversion limits broad targeting to a large total addressable market without account-based marketing. A commenter says local campaigns do better with tight geography. The Meta docs for Advantage+ app campaigns only allow geography and language targeting. That fits broad delivery in app campaigns, but it says nothing about whether broad beats interest stacking.


*Test with your own data:* Run one ad set with broad targeting (country only) and one with an interest stack, using the same creative and budget. Run both for 7 to 14 days, or until each has at least 50 conversion events. Compare cost per StartTrial and cost per paying customer. Note that Advantage+ app campaigns may not support interest targeting, so this test needs a standard app campaign.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “Valid targeting options are `geo_locations` and `locales`.”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=397) @6:37 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > I typically recommend doing two different ads, one being open targeting, giving meta more control, and the other one being an interest stack

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=664) @11:04 · Sabri Suby · 2026-06-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Broad targeting with super specific creative is the new meta.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2147) @35:47 · Ben Heath · 2026-01-06 · *supports* · basis: own experience · conflict of interest: sells a course, sells agency services, paid community
  > we see better results now by giving Meta direction, and letting Meta's machine learning algorithm work it out

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=397) @6:37 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > the meta algorithm is so smart that it often provides the best results when you give it more freedom on the targeting side

- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=699) @11:39 · AdConversion · 2025-11-12 · *qualifies* · basis: own experience · conflict of interest: sells a course, sells agency services
  > then broad targeting could make a lot of sense for you because you have a massive total addressable market

### <a id="k10"></a>K10 · well supported · confidence 0.94

For a Meta app campaign, weekly budget should be about 50 times the cost per optimized event (e.g. trial), because about 50 events per week are needed per ad set to exit learning.


*Assessment:* Four of five members converge on the ~50 events per week heuristic, which matches Meta's developer docs (a games page, but the same learning-phase logic). None is first-hand data: they are general knowledge or repetition. The "10× per day" figure (70 per week) is a rough variant, not a contradiction. Several speakers sell agency services, but the number is the documented one.


*Test with your own data:* Compute 50 × your current cost per trial. If you cannot afford that weekly, run two weeks optimizing for a cheaper event (e.g. install or registration) against StartTrial at your budget. Compare cost per paying customer and the share of ad sets marked learning limited.


- Official source: [https://developers.facebook.com/documentation/games/acquire/click-to-play-ads/budget](https://developers.facebook.com/documentation/games/acquire/click-to-play-ads/budget) — “each ad set needs approximately 50 optimization events per week”

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1084) @18:04 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > I recommend ideally to have 50 times your cost per target event as your weekly budget.

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=1076) @17:56 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > Expected subscriber acquisitions around $95.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=75) @1:15 · Sub Club by RevenueCat · 2026-09-15 · *supports* · basis: other creator
  > The ballpark is always like 50, 50 a week. So I would say 10k is rather on the lower end, really.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=75) @1:15 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · basis: other creator
  > If you're a product that is going to have cost per conversion of like 50 bucks plus, then rather, yeah, estimate like five, five times of that, if not more.

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=2214) @36:54 · App Leaders by Adapty · 2026-09-11 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > you need to multiply that with 10 every day.

### <a id="k11"></a>K11 · likely · confidence 0.69

Cost per install (CPI) alone is a poor yardstick for app ad creatives or campaigns; judge them by downstream value (trials, purchases, revenue/ROAS) or by proxies such as spend share or cost per click.


*Assessment:* All five members agree that CPI should not be the main metric, but they propose different replacements: revenue/break-even, cost per click, or spend share. Evidence is verbal and all speakers sell agency services, so the replacement metrics are weakly supported. The core point (cheap installs may not become trials or purchases) fits Meta's own distinction between install optimization and in-app event optimization, though the docs say nothing about CPI as a KPI. The two members from the same Adapty series are not independent.


*Test with your own data:* Run your top 3 install-optimized creatives for at least 7 days. Compare each one's rank by CPI, by spend share and by cost per trial or purchase (from your MMP or SDK). If the rankings differ, stop using CPI as the selection metric and use cost per trial.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “ads reach people most likely to take the action you specify”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2187) @36:27 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > so don't use the cpi as the main proxy

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=534) @8:54 · Gui Costa · 2026-07-25 · *supports* · basis: own experience · conflict of interest: sells agency services
  > You're going to check their cost per click, right?

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=620) @10:20 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: own experience · conflict of interest: sells agency services
  > It's not even CPI, definitely not. It's the spend.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=860) @14:20 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: own experience · conflict of interest: sells agency services
  > Buna işte ben CPI'den çok spende bakıyorum bu noktada.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1171) @19:31 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: own experience · conflict of interest: sells agency services
  > Hiçbir şekilde böyle purchase'a ya da trial'a dönüşmeyen çok iyi CPI'li şeylerim de oldu.

### <a id="k12"></a>K12 · contested · confidence 0.53

Leaving Meta's automatic (Advantage+) placements on across all platforms generally performs better than restricting ads manually, for example to Instagram only, unless you need a specific placement.


*Assessment:* Two creators recommend all placements, but both rely on general knowledge with no data shown, and both sell agency services. The Instagram-only advice comes from one first-hand practitioner running message campaigns in Turkey, and the comments show mixed results: lowered campaign scores when Facebook is off, and the system recommending both platforms for WhatsApp. The Kamil YILDIRIM member only explains how to restrict placements, so it makes no efficacy claim. The official page I fetched returned only a title, so the docs check is silent. For app-install, trial, or sales objectives, the all-placements default is the more plausible starting point, because the objective and audience shape the answer.


*Test with your own data:* Run two ad sets with the same budget, creative and audience for 7 to 14 days (at least 50 trial events each if possible): one with Advantage+ placements, one Instagram-only. Compare cost per StartTrial and the trial-to-paid rate, and keep the winner.


- Official source: [https://www.facebook.com/business/help/965529646866485](https://www.facebook.com/business/help/965529646866485) — “”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2221) @37:01 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > If you are using a leads campaign or a sales campaign, just leave it as is.

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=1062) @17:42 · Aprendamos Marketing · 2026-01-13 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > yo sí te recomiendo que dejes habilitadas todas las plataformas ya que le das más opciones

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=858) @14:18 · Nida Yıldırım · 2026-04-29 · *contradicts* · basis: own experience · conflict of interest: sells agency services
  > O yüzden ben manueli tercih edip genellikle sadece Instagram üzerinden mesaj almayı uygun görüyorum.

### <a id="k13"></a>K13 · likely · confidence 0.66

A healthy paid acquisition target for a subscription app is an LTV:CAC ratio of at least about 3:1 (with 2–3x as a floor for larger Meta spenders).


*Assessment:* Four channels cite roughly 3:1 as the rule of thumb, but all are agencies or course sellers. Three are generic knowledge repeating a widely used SaaS heuristic, with no data shown. The Adapty speaker, who says it comes from client data, gives a looser 2–3x floor for spenders at 100K+/month. Meta's docs set no LTV:CAC benchmark. The figure is a convention, not a platform rule, and it depends on payback period, margins and cash constraints.


*Test with your own data:* Take your last 90 days of cohorts and compute gross-margin LTV per paying customer (from actual retention) divided by blended CAC (spend divided by paying customers). Check whether the ratio is at least 3 and whether payback comes within 6–12 months. If it falls short, adjust your bid or cost cap and compare again after 2–4 weeks.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=78) @1:18 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > The golden ratio for this is one to three.

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=868) @14:28 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > It needs to cost three times less than your LTV.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=233) @3:53 · Lorenzo Pravatà · 2026-03-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > usually, you want to have an LTV2COG that is at least 3x

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1348) @22:28 · App Leaders by Adapty · 2026-09-11 · *qualifies* · basis: client data · conflict of interest: sells agency services
  > Every successful, and by that I mean 100K plus meta-spenders have an LTV of 2 to 3x minimal.

### <a id="k15"></a>K15 · likely · confidence 0.61

The first seconds (about 3) of a video ad must stop the scroll with an attention trigger such as curiosity, unexpected motion or a baby on screen, and opening on the baby first may retain viewers better than opening on the mom.


*Assessment:* The general idea that the hook must grab attention in the first ~3 seconds is a widely repeated creative heuristic. It comes from two agency-linked creators who rely on general knowledge, not shown data. The baby-first claim has one practitioner source with a verbal 98% retention figure and no screen evidence. It applies to baby or parenting apps and is not proven for B2B. The official Meta page I fetched says nothing about the opening seconds.


*Test with your own data:* Run two versions of the same video ad that differ only in the first 3 seconds (for example, the old opening against a new attention hook). Give each at least 7 days or about 50 conversions. Compare 3-second hold rate, cost per trial (StartTrial) and trial-to-paid rate.


- Official source: [https://www.facebook.com/business/ads/video-ad-format](https://www.facebook.com/business/ads/video-ad-format) — “”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=622) @10:22 · Aazar Shad · 2026-04-02 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > showing the baby first is really important

- [Meta'nın Gizli Kuralı: Reklam Maliyetlerini Düşüren Yapı](https://youtu.be/PwokUZ0NB9Q?t=472) @7:52 · Deniz Pulcu · 2026-07-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Öncelikle arkadaşlar reklamımız muhakkak scroll stopper özelliği taşımalı.

- [Meta'nın Gizli Kuralı: Reklam Maliyetlerini Düşüren Yapı](https://youtu.be/PwokUZ0NB9Q?t=553) @9:13 · Deniz Pulcu · 2026-07-29 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Bebek düz yürümek yerine tersten yürürse yani geri geri yürürse

- [Meta'nın Gizli Kuralı: Reklam Maliyetlerini Düşüren Yapı](https://youtu.be/PwokUZ0NB9Q?t=553) @9:13 · Deniz Pulcu · 2026-07-29 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Yine bebek reklamı ise bir bebek gülmesi.

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=613) @10:13 · Alessandro Cutri · 2026-06-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > people typically give you about three seconds

### <a id="k16"></a>K16 · likely · confidence 0.69

When scaling Meta campaigns, raise budgets gradually (about 10–20% every 2–4 days) and avoid frequent changes; on a small budget, adjust only every 7–10 days.


*Assessment:* Four members converge on a rule of thumb of roughly 10–20% budget increases every 2–4 days, and one says not to raise it daily. Ben Heath's 7–10 day interval is a stricter version for small or low-volume accounts, so it qualifies the others rather than contradicting them. Only one member (C14) is first-hand, and none shows data. The others repeat common practice or docs, and some creators sell agency services or courses. I could not retrieve an official Meta page with a numeric threshold, and the search results were third-party blogs that call the 20% figure a rule of thumb. Since Andromeda (Dec 2024), Meta's delivery may tolerate larger steps, but I could not verify that.


*Test with your own data:* Over 2 weeks, raise the budget of one winning ad set by 15% every 3 days. Keep an equivalent ad set at a fixed budget and compare cost per trial (StartTrial) and learning-phase status between them. Then try a 7-day cadence for another 2 weeks.


- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: platform docs · conflict of interest: sells agency services
  > Hani 3-4 günde bir %20'nin altında bu bütçe artışını yapabilirsiniz.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1947) @32:27 · Burak Mermi · 2026-07-06 · *supports* · basis: general knowledge
  > Bütçe arttırımını 3-4 günde bir 2-3 günde bir hadi %10-15 şeklinde arttırmanız gerekiyor

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=154) @2:34 · Burak Mermi · 2026-07-06 · *supports* · basis: own experience
  > %15, %20, 3 günde bir artırma yaparak bu kampanyamızı ölçekleyebiliyorduk

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=314) @5:14 · Burak Mermi · 2026-07-06 · *supports* · basis: general knowledge
  > her gün bütçesini artırırsanız, burada bu kampanyanın stabil ilerlemesini bozabilirsiniz

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=229) @3:49 · Ben Heath · 2026-02-20 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > decide, I'm going to adjust my campaigns no more than once every seven days or 10 days

### <a id="k17"></a>K17 · contested · confidence 0.58

Should a small-budget advertiser narrow targeting to a hyper-specific segment, or keep targeting broad and let Meta's algorithm find the audience?


*Assessment:* The group mixes two ideas: Ben Heath says to go narrow in messaging and market segment, while the Turkish creators say to keep the platform's audience controls broad. These are partly compatible, because Heath's niche is mostly about creative and message and the others are about technical targeting settings. All four members rest on general knowledge or one creator's experience, and all four creators sell courses or agency services. The official docs I fetched say nothing on whether narrowing hurts results, so none of the claims is verified.


*Test with your own data:* Run two ad sets with the same budget for at least 7 days and about 50 StartTrial events each. One uses broad targeting with generic creative. The other uses broad targeting with creative aimed at one specific B2B niche. Compare cost per StartTrial and the trial-to-paid rate.


- Official source: [https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience/](https://developers.facebook.com/docs/marketing-api/audiences/reference/targeting-expansion/advantage-audience/) — “Non-negotiable business constraints are not expanded.”

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=380) @6:20 · Ben Heath · 2026-02-20 · *contradicts* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > The way you compete with those bigger businesses that have much larger budgets is you say, we're not going to touch 99% of this market

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=686) @11:26 · Ben Heath · 2026-02-20 · *qualifies* · basis: own experience · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > in my experience, most businesses, particularly those operating with small budgets, are far too broad as opposed to too niche

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=236) @3:56 · Menaf Avcı · 2025-12-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Kitleyi daralttıkça erişim düşüyor. Veri kaybı yaşanıyor ve sistemin öğrenme gücü yavaş yavaş azalıyor.

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1013) @16:53 · Nida Yıldırım · 2026-04-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > O yüzden ben çok detaylı bir hedefleme yapmanızı önermiyorum.

### <a id="k18"></a>K18 · well supported · confidence 0.92

When scaling Meta ads, keep producing a steady, high volume of new creatives (weekly, with winners being rare) because creative fatigue and a low winner rate are the main bottlenecks.


*Assessment:* All four members agree on the direction: keep a steady supply of new creatives. Meta's docs back the basic idea, because fatigued ads should be replaced with new creative. The numbers are not backed by the docs. "50 ads a month per winner" is one agency's own experience in B2B SaaS. "Hundreds a week" applies only to accounts spending about $1M a month. Every member is an agency or seller of services, and none shows data on screen. That makes the principle credible but the thresholds unverifiable for a small budget.


*Test with your own data:* Run a small batch of 5–8 new, distinct-concept creatives every week for 4 weeks. Compare cost per trial (StartTrial) and your own winner rate (ads beating your median cost per trial) against the prior 4 weeks. Also track the frequency and CTR decline of your older ads.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/ads-webhooks/creative-fatigue](https://developers.facebook.com/documentation/ads-commerce/marketing-api/ads-webhooks/creative-fatigue) — “To address the fatigued ad, try creating a new ad with different images or videos”

- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=1713) @28:33 · Lorenzo Pravatà · 2025-12-17 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > if you have a very low winner rate. You want to prove that first.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=934) @15:34 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > don't forget to keep pushing ads every single week that's a really important thing

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=2688) @44:48 · App Leaders by Adapty · 2026-09-11 · *qualifies* · basis: client data · conflict of interest: sells agency services
  > hundreds of ads produced every week.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=994) @16:34 · Lorenzo Pravatà · 2026-03-26 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > we saw that you basically need at least 50 new ads every month to just find one winner that actually scales the ad

### <a id="k19"></a>K19 · likely · confidence 0.67

When you raise the budget, a creative that worked at low spend may not hold up, so have fresh creatives ready and add more of them as spend grows.


*Assessment:* Four members from three channels agree that creative supply should grow with budget, but all rest on general knowledge with no data shown. Two of the three channels sell a course or agency services, which lowers the weight of their efficacy claims. The Meta pages I found describe creative fatigue and recommend refreshing creative, but I could not retrieve text that links it to budget increases, so the docs are silent on the specific claim. The "3 creatives at $1,000" figure is an unsupported example. Commenters report that Advantage+ often spends on only 1–2 creatives, which suggests that adding more creatives does not guarantee balanced spend.


*Test with your own data:* Before your next budget increase, add 3–5 new creatives to one campaign and leave a comparable campaign unchanged. Run both for 7 days after the increase. Compare cost per trial (StartTrial), frequency and CTR, and check how much spend each creative gets.


- Official source: [https://www.facebook.com/business/help/1346816142327858](https://www.facebook.com/business/help/1346816142327858) — “”

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=556) @9:16 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > An ad that works at $100 a day won't necessarily work at $1,000.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Elinde yeni büyük şeyler, kreatifler var mı hazır mı?

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1310) @21:50 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > you need to add a new creative to maintain a balanced distribution

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1385) @23:05 · Burak Mermi · 2026-02-16 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > If your budget is low, like $1,000, you can try 3 creatives.

### <a id="k20"></a>K20 · unverifiable · confidence 0.61

Small-budget Meta ad campaigns (roughly $1–3k/month) can produce very large MRR or sales growth for B2B/subscription offers within a few months.


*Assessment:* All four are unverified testimonial-style results with no screen-shown data. Two come from the same creator, who sells agency services, a course and a paid community, and the third is a testimonial from a mentorship ad in the coaching vertical, not B2B app trials. The fourth is an Adapty claim with no spend figures, and its vendor has a reason to promote attribution. These are best treated as marketing, not as benchmarks.


*Test with your own data:* Don't rely on these figures. Run a $30–50/day campaign for 2–3 weeks with a StartTrial optimization event and track cost per trial and trial-to-paid rate. Compare the resulting CAC with your customer LTV.


- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=80) @1:20 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > turned 3.1k in ad spend into 6.3k MRR within his first month inside my advisory program

- [How to build a $100k MRR B2B SaaS business with ads](https://youtu.be/NMl7-u2UaRk?t=0) @0:00 · Denis Shatalin · 2025-11-03 · *supports* · basis: client data · conflict of interest: sells agency services, paid community
  > one of my recent clients went from 10k to 140k in MRR in less than a year on just a 3k a month ad budget.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2962) @49:22 · Ben Heath · 2026-01-06 · *qualifies* · basis: client data · conflict of interest: sells a course, sells agency services, paid community
  > from 30 euros a day ad spend to a 100K month in sales in just 3 months

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=1107) @18:27 · App Leaders by Adapty · 2026-09-11 · *qualifies* · basis: client data · conflict of interest: sells agency services
  > in three months without increasing the spend on the ad networks. They tripled their MRR.

### <a id="k21"></a>K21 · likely · confidence 0.62

Content that already performed well organically (best past posts, viral TikToks, a long YouTube video) is a good source of paid ad creatives and is worth testing as Meta ads.


*Assessment:* Three independent agency owners say organic winners are good ad candidates, which fits a widely repeated practice. All three give only verbal claims with no data, and all sell services. The official pages I could reach (the organic content testing help pages) returned 404 on fetch, so the docs check is silent. The YouTube member describes running one long video, not showing it won, and a 46-minute video is an unusual format that may behave differently as a paid ad. Organic engagement is a hypothesis generator, not a guarantee of paid results.


*Test with your own data:* Take your top 3 organic posts by engagement or conversions and run them against 3 new creatives in one ad set for 7 to 14 days. Compare cost per StartTrial. Pass: the organic-derived ads beat the median new creative's cost per trial.


- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=319) @5:19 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > Do look at your best money-making posts over the past 12 months, could be on LinkedIn, Facebook, Twitter, elsewhere

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1090) @18:10 · Aazar Shad · 2026-04-02 · *supports* · basis: own experience · conflict of interest: sells agency services
  > the TikTok organic videos that go viral in TikTok, if we use them in meta, it's also like they're winner ads

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=445) @7:25 · Sabri Suby · 2026-06-12 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > I am running a 46-inute YouTube video with minimal editing right now.

### <a id="k22"></a>K22 · likely · confidence 0.66

Providing multiple primary text and headline variations per Meta ad (up to five each, or many more headline tests) lets Meta find and deliver better-performing combinations.


*Assessment:* All three creators recommend giving Meta several text and headline options. Two of them (Cravotta and Heath) describe the standard feature of up to five options per field. Heath is the only first-hand source, and none of them show data. Cravotta's claim is general knowledge and he sells a course. Suby's 20–40 headlines per variant goes well beyond the five-slot limit, and it comes from a large-budget agency context. His headlines are probably tested as separate ads, not inside one ad. The docs searches pointed to Meta help pages on multiple text optimization and dynamic creative, and search snippets say up to five options per field. I could not retrieve a verbatim quote, so I mark the docs check silent. None of this is evidence that more variations lower cost per trial on a small budget.


*Test with your own data:* Run two identical ads in the same ad set for at least 7 days or about 50 trial events each. Give one ad a single primary text and headline. Give the other five of each. Compare cost per StartTrial and click-through rate.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1321) @22:01 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > add all five, add as many different text variations as possible because Facebook will optimize based on the different text variations

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=3184) @53:04 · Ben Heath · 2026-01-06 · *supports* · basis: own experience · conflict of interest: sells a course, sells agency services, paid community
  > But, a good idea to test multiple options cuz it just increases the chance that A, you'll find an option that works really well

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=738) @12:18 · Sabri Suby · 2026-06-12 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > I'll be running, you know, 20, 30, 40 different headlines for an ad variant.

### <a id="k23"></a>K23 · likely · confidence 0.63

Meta needs roughly 50 optimisation events (such as trial starts or purchases) per week per ad set for delivery to exit the learning phase and stabilise.


*Assessment:* All three members repeat the commonly cited ~50 events/week learning-phase rule. None shows data, and all three speakers sell agency services or courses, so this is repetition of general knowledge rather than independent practitioner evidence. The Meta Help Center page "About the Learning Phase" exists, but my fetch returned only the title, so I couldn't verify any wording from it. Third-party sources cite about 50 events per ad set in the 7 days after the last significant edit. One of them also reports a lower threshold for app-install campaigns, which I couldn't verify. The Adapty "5 per day" figure is roughly 35 per week, which is a looser version of the same idea. Treat the number as a rule of thumb. It is a per-ad-set threshold, not a hard requirement.


*Test with your own data:* Pick the cheapest event that matches your goal, usually StartTrial. In Ads Manager, check the delivery status of your single ad set after 7 days without edits. Note whether it shows Learning, Learning Limited or Active, and track cost per trial. If you get fewer than about 35 trials a week and it shows Learning Limited, test a shallower event or a higher budget for 7 days.


- Official source: [https://www.facebook.com/business/help/112167992830700?locale=en_US](https://www.facebook.com/business/help/112167992830700?locale=en_US) — “”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=233) @3:53 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > So meta needs 50 events per week, and we're going to be optimizing for that trial

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=774) @12:54 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > So you need to give at least a day five events to optimize for meta, for a campaign properly.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1859) @30:59 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > haftada en az 50 event gerekiyor

### <a id="k24"></a>K24 · well supported · confidence 0.94

When starting a campaign on a small budget, use the default automatic bidding (Highest volume / maximize number of conversions) and avoid bid caps and cost-per-result goals until you have data.


*Assessment:* All three creators give the same advice, and none shows data. Each is general knowledge, and two sell agency services, so they aren't independent practitioner proof. The Meta developer docs back the mechanics: lowest cost spends the full budget, while a bid cap needs more management and may not spend the full budget. Nothing credible contradicts this for a beginner or small-budget account.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview/bid-strategy](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview/bid-strategy) — “Need to spend more time managing bids to control cost.”

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1783) @29:43 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Bana sorarsanız başlangıçta maximize number of purchase yapın.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1038) @17:18 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > Not something I'd recommend you mess with as a beginner.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1084) @18:04 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > As a campaign strategy here, I advise you to stick to highest volume or value

### <a id="k26"></a>K26 · likely · confidence 0.72

Significant edits to an ad set or campaign, including large budget increases, can send it back into the learning phase; the size of budget increase that triggers this is debated (roughly 20% versus 50%).


*Assessment:* All three agree that large edits or budget jumps can reset learning, but they give different thresholds (under 20% vs 50% or more). None is first-hand data. Two are general knowledge or repeated docs, and the creators sell courses or agency services. The Meta help page I fetched returned no body text, so it did not confirm any exact percentage. Meta's wording, quoted secondhand, depends on magnitude, which makes 20% a community heuristic. The only experiential comment (250 to 1000 TL/day, a 4x jump, then no sales) fits a large jump hurting results but doesn't separate 20% from 50%.


*Test with your own data:* Raise the budget on one ad set by about 20% and on a similar ad set by about 50%, waiting 3 to 4 days between changes. Check in Delivery whether each shows 'Learning' or 'Learning limited', and compare cost per StartTrial before and after.


- Official source: [https://www.facebook.com/business/help/112167992830700?locale=en_US](https://www.facebook.com/business/help/112167992830700?locale=en_US) — “”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *qualifies* · basis: platform docs · conflict of interest: sells agency services
  > %20'nin üstüne çıktığında learning'i bozuyor hakikaten.

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=154) @2:34 · Ben Heath · 2026-02-20 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > If you make a significant adjustment to a campaign ad set, so for example, you create a new ad, you change some of the settings of the ad set level

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1310) @21:50 · Burak Mermi · 2026-02-16 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > If you increase this budget by 50%, you will reset the learning process.

### <a id="k27"></a>K27 · contested · confidence 0.53

For Meta app campaigns, creative and offer are the dominant performance lever, more than targeting or funnel structure; a competing view says signal quality comes first.


*Assessment:* Two of the three members say creative is the main lever, and a third says signal quality comes before creative. None of them shows data, and all three sell agency services or courses. The 90% figure is a guess, not a measurement. The official-docs searches returned no facebook.com/business pages, so the docs check is silent. The views partly fit together: with Advantage+ and Andromeda, targeting is automated, so creative is the lever the advertiser controls. That only holds if the conversion signal (StartTrial events, tracked correctly) is reliable. Without a clean signal, even strong creative can't be optimized toward trials.


*Test with your own data:* First confirm that the StartTrial event fires reliably, and check the event match quality or the SDK/MMP event counts. Then run 2 weeks with 3–5 new, distinct creative concepts against your current ads at the same budget. Compare cost per StartTrial. If the new creatives move it much more than any setup change did, creative is your main lever.


- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=474) @7:54 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > your offer and your creative drive 90% of results in your campaigns

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=474) @7:54 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > the creatives is everything for Google and for meta is everything

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=785) @13:05 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *contradicts* · basis: general knowledge · conflict of interest: sells agency services
  > İlki her zaman için sinyal yani sinyal kalitesi her şeyin temelinde.

### <a id="k28"></a>K28 · likely · confidence 0.63

For a subscription app, the onboarding and first-paywall funnel usually matters more for trial starts and paid conversions than ads-manager tweaks, so it should be tested together with ad optimisation.


*Assessment:* Three sources lean the same way, but they aren't independent evidence. One is a practitioner who sells agency services and shows no data. One is a secondhand remark about someone else's client work. One is a general-knowledge rule of thumb (80%) that the speaker frames as his own opinion. The official docs cover event optimisation but say nothing about onboarding or paywall priority. The logic is sound: Meta can only optimise toward events users actually complete, so a broken funnel caps results. The 80% threshold is arbitrary and depends on how the paywall is placed.


*Test with your own data:* Take your current install-to-paywall-view rate and paywall-to-trial rate from your analytics. Run an A/B test of one onboarding or paywall change (for example, paywall placement or a shorter flow) for 2 weeks at constant ad spend and creative. Success means a higher paywall-to-trial rate and a lower cost per StartTrial.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1398) @23:18 · Aazar Shad · 2026-04-02 · *supports* · basis: own experience · conflict of interest: sells agency services
  > It's the first paywall they see if they start a free trial

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=631) @10:31 · Sub Club by RevenueCat · 2026-09-15 · *supports* · basis: other creator
  > Most of Marcus's client work is focused on onboarding, paywalls, pricing, not ads manager.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=320) @5:20 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Benim fikrimce bu %80'nin altındaysa bence sıkıntılı.

### <a id="k29"></a>K29 · likely · confidence 0.62

Adding other English-speaking tier-one countries (Canada, UK, Australia, New Zealand) alongside the US lowers the cost per install, because US traffic is the most expensive.


*Assessment:* Three creators from two channel families (Cravotta and two Adapty channels) give the same advice. None shows data, and two of them are repeating a known rule of thumb. Two sell courses or agency services. The docs only say that country targeting exists and don't say anything about cost by country. Cheaper installs are plausible, but for a B2B subscription app, install cost isn't the real goal. Lower-priced countries may produce fewer trials and paying customers.


*Test with your own data:* Run two ad sets with the same creative for 7-14 days: one US only, one US+CA+UK+AU+NZ. Compare cost per StartTrial and trial-to-paid rate, not just CPI.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1169) @19:29 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > if you do this, you will greatly reduce the cost of installs.

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=854) @14:14 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: own experience · conflict of interest: sells agency services
  > make sure that your at set level language setting is on English

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=628) @10:28 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Bence ilk 1000 dolarınızı purchase kampanyasından harcamayın derim.

### <a id="k30"></a>K30 · likely · confidence 0.76

Test new creatives in ABO (fixed ad-set budgets) and move proven winners into a CBO (Advantage+ campaign budget) campaign for scaling.


*Assessment:* The ABO-test, CBO-scale pattern is a widely repeated community convention. The support here is thin: one first-hand ecommerce seller who also sells a course, one creator repeating it, and one general-knowledge video. Meta's docs don't prescribe it. Gürkanzone's variant, which keeps scaling the winner in ABO while also duplicating it into CBO, draws overlap and cost-inflation concerns in comments. All three are ecommerce sales examples; none relate to B2B SaaS app-install campaigns. An Advantage+ app campaign has limited ABO/CBO control, so the pattern may not carry over.


*Test with your own data:* Run one ABO test ad set per creative at an equal budget for 5-7 days. Move the winners into a CBO campaign without duplicating them in the ABO campaign. Compare cost per trial (or per proxy event) against a control that keeps the winners in ABO. Use at least about 50 events per arm before deciding.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/split-testing](https://developers.facebook.com/documentation/ads-commerce/marketing-api/guides/split-testing) — “However, budget directly impacts reach for your test groups.”

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=1373) @22:53 · Gürkanzone · 2026-08-15 · *qualifies* · basis: own experience · conflict of interest: sells a course
  > Hem burada ölçekliyoruz. Hem de gidip CBO'nun içerisine atıyoruz.

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=391) @6:31 · Burak Mermi · 2026-07-06 · *supports* · basis: other creator
  > Yani alışveriş değil de sepete ekleme hedefi veriyoruz

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > An ABO gives you control over how much budget goes into each ad set. So every new creative gets a fair test.

### <a id="k32"></a>K32 · likely · confidence 0.67

For a small-budget Meta app campaign, use a daily budget with no end date rather than a lifetime budget, so you can run it continuously and pause or scale it as you like.


*Assessment:* Three channels agree on a daily budget, but this is a preference, not a measured result. All three sell agency services or courses and show no data. Meta's docs describe how each budget type behaves, with daily spend varying up to 25% and lifetime spend shifting between days. They don't say which one performs better, so the docs are silent on the recommendation. The practical point holds for small budgets and ongoing campaigns: a daily budget is easier to pause and scale.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview/budgets](https://developers.facebook.com/documentation/ads-commerce/marketing-api/bidding/overview/budgets) — “On days with better opportunities, up to 25% more than your daily budget may be spent.”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=685) @11:25 · Aprendamos Marketing · 2026-01-13 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > a mí me gusta trabajar con presupuesto diario, las campañas, no dejarlas por un tiempo fijo

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=890) @14:50 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > I prefer daily budgets. With a lifetime budget, you end up with a fixed-length campaign.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1409) @23:29 · Kamil YILDIRIM · 2026-05-31 · *supports* · basis: own experience · conflict of interest: sells agency services
  > Günlük bütçeden reklamımızı yayına alırız, dilediğimiz zaman da kapatırız.

### <a id="k36"></a>K36 · well supported · confidence 0.93

Meta delivers whatever event you optimize for; optimizing for raw trial starts yields trials (including low-quality ones that cancel immediately) that may not convert to paid subscriptions.


*Assessment:* The mechanism (delivery is optimized toward the chosen event) is supported by Meta's developer docs, and both videos state it. The docs don't say a trial event leads to poor paid conversion; that part is plausible inference. Both channels are agencies or vendors and give no data, and the claims are general knowledge rather than independent measurements. They are also partly the same idea repeated, so they don't count as independent proof.


*Test with your own data:* Run two ad sets with the same creative and budget for at least 2 weeks: one optimized for StartTrial and one for Subscribe/Purchase (or a value-based event). Compare cost per paid subscriber and trial-to-paid rate at day 7 to 14. If the Subscribe ad set gets too few events, keep the StartTrial ad set.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “Ads will be delivered to people most likely to take actions such as purchasing products in your app after app install”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1335) @22:15 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Meta'ya da biz hani hangi event için optimize ediyorsak Meta'da biz onu getiriyor.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1416) @23:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > O yüzden trial hep gönderip trial optimize edersek trial getirir.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1172) @19:32 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > the problem with the trial started is that a 30 second cancellation from a trial started looks exactly like a six month subscriber for meta

### <a id="k37"></a>K37 · well supported · confidence 0.91

For Meta app promotion, you launch an app installs campaign first (required for iOS), and the app events/subscription optimization only becomes available after Meta has received enough start-trial or purchase events.


*Assessment:* The docs confirm that iOS campaigns must use the app installs objective, and that app-event optimization requires events set up first. They don't state a specific volume threshold. The two First Try claims match common practitioner experience but come from one agency creator with no data shown. Gui Costa's "sales campaign for subscriptions" advice is unsupported by the docs I found, and the interface and objective names have changed over time (Advantage+ app campaigns).


*Test with your own data:* Run an app installs campaign with the StartTrial event integrated for 1–2 weeks. Check whether the app events optimization option appears in setup, and track the StartTrial count and cost per trial.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/error-reference/ios-14-error-codes](https://developers.facebook.com/documentation/ads-commerce/marketing-api/error-reference/ios-14-error-codes) — “All iOS 14 campaigns must be app installs campaigns. Select app installs as your campaign objective.”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=609) @10:09 · Gui Costa · 2026-07-25 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > And always that you create iOS campaigns you put app install campaigns as the goal.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=308) @5:08 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > You need to send a certain volume of these start trial or purchase events to Meta in order for them to make you eligible for this type of campaign.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1161) @19:21 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > If you don't see this, it means Meta didn't receive enough events to make you eligible for such campaigns.

### <a id="k38"></a>K38 · contested · confidence 0.52

For Meta app campaigns, StartTrial and Purchase events should be tracked in a specific way. One view is client-side SDK only. The other is SDK plus Conversions API (CAPI) with a shared event ID for deduplication, which is claimed to be needed for PLTV/value optimization.


*Assessment:* The docs confirm that SDK and CAPI app events can coexist and that event_id plus event_name are used to deduplicate them. They do not say that SDK-only tracking is wrong. They also do not say that PLTV needs CAPI. First Try recommends SDK-only, with no evidence. Its own commenter notes that trial-to-paid events happen off-device. RevenueCat's claim fits its business, because it sells server-side event forwarding. Both rest on general knowledge. SDK-only is the simplest setup for early StartTrial optimization. For renewals and post-trial conversions that happen off-device, server-side events are the only way to report them.


*Test with your own data:* Run two equal-budget campaigns for 2–3 weeks. Campaign A optimizes for StartTrial through the SDK only. Campaign B optimizes for the paid conversion, sent through CAPI and the SDK with a shared event_id. Compare cost per paid customer, and check the trial-to-paid rate in your own billing data.


- Official source: [https://developers.facebook.com/docs/marketing-api/conversions-api/app-events](https://developers.facebook.com/docs/marketing-api/conversions-api/app-events) — “The `event_id` is required for the deduplication setup case.”

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=155) @2:35 · First Try · 2026-02-03 · *contradicts* · basis: general knowledge · conflict of interest: sells agency services
  > I recommend you to just track the start trial and purchase events from the client, not anything server-side.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > with the app plus sdk is not uh going to work completely it needs to work through the conversions api

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > you need to send the event id on both sdk and servers so meta will merge the data

### <a id="k39"></a>K39 · likely · confidence 0.60

Redesigning the onboarding paywall into multiple screens that clearly present a 7-day free trial (and possibly a cheap monthly option) increases trial starts by roughly 20-56%.


*Assessment:* Two sources report paywall redesigns lifting trial starts, but only verbally, with no screen-shown data. Both sell agency services or courses. C3 only describes the setup and comes from another creator, so it adds no evidence. Meta's docs say nothing about paywall design, since this is app-side conversion work and not ad-platform behavior. The effect is plausible, but the size is unverified and the vertical is consumer apps, not B2B.


*Test with your own data:* A/B test the current paywall against a version with a short video screen and a '7 days free, we'll remind you in 2 days' screen. Use a remote-config or paywall tool (e.g. RevenueCat Experiments or Superwall). Run it for at least 2 weeks, until each arm has about 100 or more trial starts. Compare trial start rate per install, then trial-to-paid conversion at day 7-14.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1474) @24:34 · Aazar Shad · 2026-04-02 · *supports* · basis: own experience · conflict of interest: sells agency services
  > Like free trial increased, I think it was like 20% or 30% and also free trial converts

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=152) @2:32 · App Masters · 2026-06-09 · *supports* · basis: client data · conflict of interest: sells a course, sells agency services, sponsored
  > those two screens led to a 56% increase in trial activations

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=76) @1:16 · App Masters · 2026-06-09 · *supports* · basis: other creator · conflict of interest: sells a course, sells agency services, sponsored
  > We offer seven days for free. We'll remind you in two days.

### <a id="k40"></a>K40 · likely · confidence 0.62

Placing a paywall inside the app onboarding flow converts free users into paying subscribers, because most subscription purchases (60–80%) happen during onboarding.


*Assessment:* Two of the three members come from the same App Masters video. The sponsored, course- and agency-selling channel gives no screen-shown data. The third member is a different creator (Gui Costa) with first-hand experience, but it is a single app and has no numbers. The direction matches common subscription-app practice, but the 60–80% figure is unsourced, and Meta's docs say nothing on paywall placement. The claim is plausible but depends on the app and the audience.


*Test with your own data:* Run a 50/50 A/B test of onboarding with the paywall versus without it (or with a soft paywall) for at least 2 weeks or about 100 trials per arm. Compare the rate of installs that start a trial, the cost per StartTrial, and retention at day 7 or day 30.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=76) @1:16 · App Masters · 2026-06-09 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, sponsored
  > over 60 to 80% of all the people that end up buying, they do so during the onboarding process

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=943) @15:43 · Gui Costa · 2026-07-28 · *supports* · basis: own experience · conflict of interest: sells agency services
  > We created a paywall in the onboarding process.

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=380) @6:20 · App Masters · 2026-06-09 · *supports* · basis: client data · conflict of interest: sells a course, sells agency services, sponsored
  > Guess what happened? Bobby, more revenues and increase in retention.

### <a id="k41"></a>K41 · well supported · confidence 0.91

Test several different creative formats (selfie, talking head, static, podcast-style, etc.), match each format to its angle, and let the data show which format wins.


*Assessment:* All three members agree: diversify formats and let data decide. Meta's app campaign page also recommends using many creatives across the formats that suit your audience, which fits the Andromeda emphasis on creative diversity. The evidence is only verbal and from agency sellers, with no data shown. The one detail not backed by docs is putting each format in its own ad set. That is a structural choice, and on a small budget it fragments spend.


*Test with your own data:* For 2 weeks, run one Advantage+ app campaign with 3 distinct formats (talking head video, static, and a podcast/B-roll style) across 2 angles. Compare cost per StartTrial and the share of spend each format gets. Keep the formats that win.


- Official source: [https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns](https://www.facebook.com/business/ads/meta-advantage-plus/app-campaigns) — “Hedef kitlenize uygun en iyi reklam formatlarıyla birlikte en fazla 50 kreatif kullanarak daha iyi performans”

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=613) @10:13 · Alessandro Cutri · 2026-06-04 · *supports* · basis: own experience · conflict of interest: sells agency services
  > if you have these formats within a different ad set, you're giving yourself the best shot at success

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=703) @11:43 · Alessandro Cutri · 2026-06-04 · *supports* · basis: own experience · conflict of interest: sells agency services
  > we're going to test all these different formats and then we're going to let the data tell us what exactly works best from that

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=1447) @24:07 · Lorenzo Pravatà · 2026-03-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Something that helps a lot is to match the format to the angle.

### <a id="k42"></a>K42 · likely · confidence 0.60

On a small budget, test creatives by putting each one in its own ad set with an equal budget (a manual, ad-set-budget install campaign), because Advantage+ or a shared ad set concentrates spend on the creative Meta predicts will win and the others get no spend.


*Assessment:* Three members from two channels agree, and the practice is a common one (ABO with one creative per ad set for testing). Both channels sell agency services, only one is clearly first-hand, and none shows data. The docs confirm that Advantage+ app campaigns use a single ad set with several ads and that manual campaigns allow multiple ad sets, but they say nothing about how spend is split between ads. The mechanism, that Meta favours a predicted winner, is plausible but not documented. A separate point: a stricter version of the approach splits the budget so thin that no ad set exits learning, and that is a real risk at very small budgets.


*Test with your own data:* Run a manual app campaign with 3 creatives, each in its own ad set with an equal daily budget, for 7 days. Run the same 3 creatives in one Advantage+ campaign over the same period. Compare the spend share per creative and the cost per StartTrial. If the Advantage+ spend is heavily skewed and cost per trial is no better, keep the split structure for testing.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “Manually test up to 50 creative combinations.”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=229) @3:49 · Gui Costa · 2026-07-25 · *supports* · basis: own experience · conflict of interest: sells agency services
  > if you have a small budget, Meta will prioritize the results that you want to get and they're going to define by themselves what are the best creators

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=761) @12:41 · Gui Costa · 2026-07-25 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > put each ad set in that so you put the same amount of budget for the same ads and you don't prioritize the bad stuff

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1018) @16:58 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: own experience · conflict of interest: sells agency services
  > I would not let advantage campaign optimize for install, like to find the best creatives.

### <a id="k44"></a>K44 · contested · confidence 0.60

Your customer acquisition cost must stay below the customer's LTV or gross profit, and a common rule of thumb is to cap CAC at a fraction of that value (for example 3-4x LTV:CAC), not at the offer price.


*Assessment:* CAC below LTV or gross profit is basic unit economics, and C1 and C2 are consistent with it. C2's 3-4x ratio is a rule of thumb, not a platform fact. C9 says the maximum CAC equals the offer price. That is only break-even on a single upfront sale. It ignores margin, and for a subscription it ignores churn and payback time, so it holds only under conditions. All three come from agency sellers with no data, and Meta's docs don't address the subject.


*Test with your own data:* Work out your own numbers: gross-margin LTV (price × margin × expected months retained). Set the cost per result goal at 25-33% of it. Run for 2-4 weeks, or at least 50 trials. Check cost per trial × trial-to-paid rate against that target CAC.


- Official source: [https://developers.facebook.com/docs/marketing-api/bidding/overview](https://developers.facebook.com/docs/marketing-api/bidding/overview) — “within certain bidding constraints such as cost per result”

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=75) @1:15 · Alessandro Cutri · 2026-06-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > we want the LTV to be greater than customer acquisition costs

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=75) @1:15 · Alessandro Cutri · 2026-06-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > ideally, you want that to be in that $2,000 to $3,000 range

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=685) @11:25 · Aprendamos Marketing · 2026-01-13 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > Yo debería estar dispuesto a invertir hasta 2 mil pesos para generar un cliente.

### <a id="k45"></a>K45 · likely · confidence 0.67

Creatives that are too similar (same visual, hook, concept or audience) tend to be grouped by Meta's delivery and compete or reach the same people, so creatives should differ meaningfully in angle or concept.


*Assessment:* All three members agree on the direction, and the commenters' experience (one of five creatives gets all the spend) is consistent with it. The members rely on general knowledge or other creators, and two of them sell courses or agency services. Meta's Andromeda post only says that ad diversity helps and doesn't mention grouping or "entity IDs". Third-party sources agree that near-duplicates cluster, but the exact thresholds, such as whether the same hook, music or setting is enough, are unverified. Most likely it is true when the creatives are near-duplicates, and the effect is weaker when the angle differs.


*Test with your own data:* Run one ad set with 4 creatives that are visual variants of the same hook and angle. Run a second ad set with 4 creatives that use distinct angles (education, features, reviews, offer). Use the same budget for 7 days and compare spend distribution and cost per trial (StartTrial).


- Official source: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “Increased ad diversity can improve people's experience with ads and drive better advertiser outcomes.”

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1462) @24:22 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > The most common mistake here is if all the creatives are the same.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=1145) @19:05 · Lorenzo Pravatà · 2026-03-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > when you create ads that are pretty similar, they're going to go to the same audience

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1181) @19:41 · Burak Mermi · 2026-07-06 · *supports* · basis: other creator
  > Sürekli aynı hook'u kullanıyorsanız

### <a id="k49"></a>K49 · well supported · confidence 0.92

Ads in special ad categories (financial products, employment, housing, social issues/elections/politics) must be declared when creating the campaign. Otherwise ads can be rejected, the campaign restricted or stopped, or the ad account penalized.


*Assessment:* Both creators say the same thing, and it matches Meta's documented requirement to declare special ad categories. They are not independent practitioners (basis is general knowledge, and both sell agency services), but the rule is a well-established platform mechanic. The severity claims (whole ad account disapproved) are plausible but are not quantified in the docs I could open. The reader's B2B subscription app almost certainly falls outside these categories, so this applies mostly as a check.


- Official source: [https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category](https://developers.facebook.com/docs/marketing-api/audiences/special-ad-category) — “Businesses whose ads do not belong to a Special Ad Category must indicate NONE or send an empty array in the special_ad_categories field.”

- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=761) @12:41 · Aprendamos Marketing · 2026-01-13 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > te van a restringir la campaña o la van a parar porque justamente no lo mencionaste

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1113) @18:33 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > a good chance not only your ads will be rejected, but your whole ad account can get disapproved

### <a id="k53"></a>K53 · well supported · confidence 0.95

Under default (Advantage+) placements, Meta shows ads on Facebook and Instagram and other Meta surfaces, plus Audience Network, which serves ads inside third-party apps.


*Assessment:* Both members describe basic placement mechanics that are compatible. They are general knowledge, not independent practitioner evidence. Meta's developer docs confirm that Audience Network serves ads in third-party apps. Nothing found contradicts either claim.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/audience-network](https://developers.facebook.com/documentation/ads-commerce/marketing-api/audience-network) — “Facebook's Audience Network serves ads on other publishers' iOS and Android apps and mobile websites.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2891) @48:11 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > the audience network distribution which is just basically uh showing ads inside third-party applications

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1721) @28:41 · Kamil YILDIRIM · 2026-05-31 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Facebook'ta da gösterilir, Instagram'da da gösterilir.

### <a id="k54"></a>K54 · likely · confidence 0.74

Ads that look like organic, native content (podcast-style, interviews, educational or news-style) outperform ads that look like ads.


*Assessment:* Both creators are agency sellers who assert this from general knowledge with no data shown. The comments are anecdotal, with one giving a small result ($240 spend, about $4,000 in sales) that isn't verifiable. The idea is widely repeated and plausible, especially for Reels and Stories where the feed is full of organic content. Meta's docs only discuss native placements in Audience Network, and they warn that ads which look too much like surrounding content can confuse people. They don't say native-looking creative wins on Meta, so the claim is plausible but not proven. Also, "look like organic" can't mean disguising the ad: Meta's ad label stays.


*Test with your own data:* Run two ad sets with the same audience and budget for 7–14 days. One uses a native-style video (founder or UGC screen recording, no logo intro). The other uses your polished ad. Compare cost per StartTrial and the trial-to-paid rate, not CTR alone.


- Official source: [https://www.facebook.com/business/help/473039819825664](https://www.facebook.com/business/help/473039819825664) — “”

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=445) @7:25 · Sabri Suby · 2026-06-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > instead of making our ads look like ads, we are going to do the absolute opposite

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=1447) @24:07 · Lorenzo Pravatà · 2026-03-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > we focus on using formats that look more like content like more organic videos than normal ads

### <a id="k56"></a>K56 · likely · confidence 0.68

Simple, rough or native-looking ads with a strong message can outperform polished, expensive video ads, so producing many fast variants matters more than polish.


*Assessment:* Both creators, who sell agency services, say rough ads beat polished ones. One is general knowledge with no data, and the other is verbal with no numbers. Commenters mostly confirm from their own experience, but they give no numbers, and one says static did not beat video for them. The official docs say nothing about polished versus rough creative. They only mention testing up to 50 creative combinations. The claim is plausible as a heuristic, but it depends on the message, the format and the audience, and it is not a universal rule.


*Test with your own data:* Run 3-5 rough, message-led ads (UGC, a screen recording or a plain static) against your best polished video in the same Advantage+ app campaign or a split test. Run it for 7-14 days, or until each variant has about 50 or more optimization events. Compare cost per StartTrial and the click-through rate.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “”

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=555) @9:15 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > the ugly video is performing better or the ugly ads performing better because the message on it was better than the very polished ad video

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=74) @1:14 · Sabri Suby · 2026-06-12 · *supports* · basis: own experience · conflict of interest: sells agency services
  > these down and dirty native statics that I've created that literally are outperforming a VSSL that took 2 and 1/2 months to produce

### <a id="k57"></a>K57 · well supported · confidence 0.94

Instead of uploading new creative, you can pick an existing Instagram post or reel (including a creator's video used as a Spark-style ad) as the creative for a Meta ad.


*Assessment:* Using an existing Instagram post as the ad creative is a standard Meta feature, and Kamil Yildirim's Ads Manager screen shows it. Meta's developer guide "Use Posts as Instagram Ads" supports the general idea. Its API wording is loose, though, and I fetched it through a summarizing tool, so the quote may not be exact. Steven Cravotta adds that the brand "owns the video rights" and the Spark Ads code "in perpetuity". That is a course seller's general-knowledge claim. Rights and permissions depend on the creator agreement and on the partnership-ad or authorization flow, and the docs I found don't confirm perpetual ownership. Both speakers have a conflict of interest, but the mechanic itself is low-risk.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads](https://developers.facebook.com/documentation/ads-commerce/instagram/ads-api/guides/use-posts-as-ads) — “You can boost your Instagram content by using an existing Facebook Feed post or Story as part of your ad's creative.”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=702) @11:42 · Steven Cravotta · 2026-07-30 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > you own the video, the spark ads code, you own it all in perpetuity outright.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=2112) @35:12 · Kamil YILDIRIM · 2026-05-31 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Dilerseniz Instagram'da paylaşıp direkt paylaştığınız içeriği de seçebilirsiniz.

### <a id="k58"></a>K58 · contested · confidence 0.57

Optimize for sales/purchases only if the account produces enough of those events for Meta to learn (roughly 50 in two weeks, by one creator's rule); otherwise optimize for a higher-funnel event such as sign-ups or trials.


*Assessment:* Both creators give the same principle: move down the funnel only when there is enough event volume. Shatalin's "50 events in two weeks" is a looser version of the commonly cited ~50 events per week per ad set learning-phase guidance. Neither shows data, and both sell courses or agency services. The Help Center page I fetched returned no body text, so I couldn't verify it, and the docs check is silent. The principle is plausible, but the exact threshold is a rule of thumb. Meta's learning-phase guidance is usually cited as about 50 events per week, which is stricter than 50 per two weeks.


*Test with your own data:* Run StartTrial optimization for 2 weeks. If you get fewer than ~50 Subscribe/Purchase events in that time, keep optimizing for StartTrial. If you have enough volume, split-test the Purchase event against StartTrial at the same budget. Compare cost per paying customer, and look at the learning-phase status.


- Official source: [https://www.facebook.com/business/help/112167992830700?locale=en_US](https://www.facebook.com/business/help/112167992830700?locale=en_US) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=80) @1:20 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > If you can get 50 sales events in a two-week time frame, you can go for sales

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1558) @25:58 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > My preference would be to go for purchases provided you're generating enough purchases for Meta to be able to learn.

### <a id="k60"></a>K60 · contested · confidence 0.57

A campaign with a higher cost per trial (or lower ROAS) can be more profitable than a cheaper one if its users have higher LTV/ROI or it runs at larger scale, so judge campaigns by profit/LTV, not cost per result alone.


*Assessment:* The principle is basic unit economics: profit = (LTV − CAC) × volume. Both members state it, but only verbally, with no data. Both are general knowledge, and both creators sell agency services or courses. The Ben Heath claim is about ROAS and scale, not LTV, so it is adjacent. It also only holds if the margin stays positive and you can actually scale. The Meta docs describe value optimization and LTV but don't directly address this tradeoff. The one comment is a question and doesn't refute it.


*Test with your own data:* For 2–4 weeks, split trials by campaign or ad set and track each one's trial-to-paid rate and 30-day retention. Compute cost per paying customer and payback against LTV. Success means the campaign with the higher cost per trial has the lower cost per paying customer, or a shorter payback.


- Official source: [https://en-gb.facebook.com/business/help/1730784113851988](https://en-gb.facebook.com/business/help/1730784113851988) — “”

- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=631) @10:31 · App Leaders by Adapty · 2026-09-11 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > The cost per trial is higher. But when you look at the LTV and read ROI

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1372) @22:52 · Ben Heath · 2026-02-20 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > Much better to generate a 4x return on ad spend spending a million dollars a month than a 10x return on ad spend spending $10,000 a month.

### <a id="k61"></a>K61 · contested · confidence 0.57

Test creatives in a separate test campaign, then move only the proven winners into a scale campaign (cost cap or main ad set). Only a small share of tested ads (~5–10%) graduate, and this usually lowers cost per result.


*Assessment:* Both members describe the same test-then-scale funnel. They use different verticals and objectives: app installs and in-app events in one, B2B SaaS leads in the other. Both are verbal and give no data. Both creators sell agency services or communities, so their efficacy claims carry less weight. The 5–10% graduation rate is an expectation, not a measured result. Official Meta docs returned nothing on this structure. The only support is third-party blogs repeating the same practitioner advice. With small budgets, false winners are likely, which limits the claim.


*Test with your own data:* Run a test campaign for 7–14 days with a few creatives. Move the top 1–2 ads, by cost per StartTrial, into a separate scale campaign. Compare the scale campaign's cost per trial over the next 7–14 days to the blended cost per trial before the split. Only count it as a win if the cost is lower with at least 30–50 trials.


- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=934) @15:34 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > it's expected that around five to ten percent of the ads will reach uh this campaign

- [How to build a $100k MRR B2B SaaS business with ads](https://youtu.be/NMl7-u2UaRk?t=394) @6:34 · Denis Shatalin · 2025-11-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services, paid community
  > Most often, this gets us much cheaper cost per call because this is when you're only going to be now spending money on things which work

### <a id="k63"></a>K63 · likely · confidence 0.65

Frequent edits, or repeatedly switching ads on and off, disrupt Meta's learning phase. Leave campaigns alone and judge results over a longer window, such as a week.


*Assessment:* Both creators say the same thing, and it matches the widely documented idea that significant edits can reset learning. Neither shows data. One is a verbal anecdote from an agency owner, the other is general knowledge, and both sell agency services. The Meta Help Center pages I found (Best Practices to Reduce Cost Per Result, Last Significant Edit) appear to say much the same, but their text didn't load, so I can't quote them and have marked the docs check silent. The rule applies only to significant edits, such as changes to targeting, creative, optimization event or a long pause. Minor tweaks don't necessarily reset learning. For a small budget it matters more, because the ad set may never reach about 50 optimization events a week even without edits.


- Official source: [https://www.facebook.com/business/help/321695409726523](https://www.facebook.com/business/help/321695409726523) — “”

- [How to launch SaaS Meta ads with $100/day and actually get results](https://youtu.be/-3O8dR3rPu4?t=551) @9:11 · Denis Shatalin · 2025-12-29 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, paid community
  > meta doesn't think in days, it thinks in weeks

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1558) @25:58 · Nida Yıldırım · 2026-04-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > O yüzden reklam sürekli açmak ve kapamak doğru bir davranış değildir.

### <a id="k64"></a>K64 · likely · confidence 0.63

Smaller budgets generate fewer conversions, so a Meta campaign/ad set takes longer to exit the learning phase, which requires roughly 50 optimization events per week.


*Assessment:* Both members agree with the widely repeated rule of about 50 optimization events in 7 days per ad set, and with the logic that a low budget means fewer events and a longer learning phase. Both are general knowledge or repeated docs, not first-hand data. The Ben Heath commenters' experience (ads stuck in "learning limited" for a B2B campaign) is consistent with the claim. I could not retrieve the official help page (404 on both fetches), so the doc check is silent. The 50-event figure applies per ad set, and some third-party sources suggest that app campaigns may use a different threshold.


*Test with your own data:* Check Ads Manager for the delivery status (Learning / Learning Limited) of your StartTrial ad set. Compare weekly StartTrial count with 50. If it is far below, test optimizing for a higher-volume upstream event (e.g. install or registration) for 2 weeks and compare cost per trial and trial-to-paid rate.


- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=154) @2:34 · Ben Heath · 2026-02-20 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > The smaller your budget, typically, the lower number of conversions you're going to generate, the longer it is going to take you to exit the learning phase.

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=2436) @40:36 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: platform docs · conflict of interest: sells agency services
  > Evet özellikle o 50 conversion gelmesi önemli ki learning'ten çıksın.

### <a id="k65"></a>K65 · likely · confidence 0.67

For a small-budget subscription app campaign, keep the account structure consolidated (start with one or very few campaigns and few ad sets) instead of fragmenting into many ad sets, which prevents exit from the learning phase.


*Assessment:* Both members point the same way: fewer campaigns and ad sets, so each gets enough optimization events. One is first-hand, the other is general knowledge. Both creators have agency or sales ties, and the two sources aren't fully independent practitioner evidence. The Meta help page I fetched returned no body text, so I couldn't confirm it. Consolidation is widely repeated, but the "single campaign" prescription is a heuristic, and the exact thresholds are unverified.


- Official source: [https://www.facebook.com/business/help/112167992830700](https://www.facebook.com/business/help/112167992830700) — “”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2111) @35:11 · RevenueCat · 2026-09-12 · *supports* · basis: own experience · conflict of interest: sells agency services
  > running one campaign with 50 ad set and one ad in each ad set

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1097) @18:17 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Yani hatta başlangıçta tek kampanya yapın.

### <a id="k66"></a>K66 · unverifiable · confidence 0.60

Meta app-install campaigns for subscription/consumer apps can get installs at roughly $0.35–$2 each on small budgets, though the cost varies a lot by app, country and period.


*Assessment:* The two members report different install costs ($0.34–0.50 for Puff Count, about $2 for a travel app in the US and Europe). Both are outcome figures from the speakers' own accounts, so they are not directly comparable. One is spoken only and the speaker sells a course. The other shows Ads Manager but comes from an agency seller. Neither is about trials or paid conversion, which is the research goal, and install cost says little about StartTrial cost.


*Test with your own data:* Run an app-install campaign at about $20–30 per day for 7–14 days. Optimize one ad set for installs and another for StartTrial if you have enough events. Compare cost per install, cost per trial and trial-to-paid rate from your own data.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=156) @2:36 · Steven Cravotta · 2026-07-30 · *qualifies* · basis: own experience · conflict of interest: sells a course
  > We were spending around 34 cents, 50 cents, 43 cents per install. And those installs were earning us around a dollar, sometimes a dollar 50 in better months.

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=0) @0:00 · Gui Costa · 2026-07-25 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > about an average of 30 first-time downloads per day, okay? Our budget is $500, right?

### <a id="k67"></a>K67 · contested · confidence 0.57

Advantage+ creative enhancements: either leave most on and switch off only the message-altering ones (AI text, translation), or turn them all off so you know exactly what viewers see.


*Assessment:* Both creators agree the enhancements are individually controllable and that message-altering ones (text, translation) deserve caution. They differ on the default: Ben Heath says trust Meta and keep the rest on, First Try says turn everything off. Both are general-knowledge opinions with no test data, and both creators sell agency services. The docs I could fetch said nothing on which default is better.


*Test with your own data:* Run two identical ads in the same ad set for at least 7 days and about 50 or more trial starts in total. Leave visual enhancements on in one and turn all enhancements off in the other. Compare cost per StartTrial and the trial-to-paid rate.


- Official source: [https://www.facebook.com/business/help/297506218282224](https://www.facebook.com/business/help/297506218282224) — “”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=3703) @1:01:43 · Ben Heath · 2026-01-06 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > I would err on the side of trusting Meta with this.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1470) @24:30 · First Try · 2026-02-03 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > I'd say just deactivate it. Be safe. And you'll know what people will see.

### <a id="k68"></a>K68 · likely · confidence 0.64

In Advantage+ app campaigns, judge performance at the ad-set level, and don't cut individual creatives just because Meta spent little on them, because the algorithm allocates spend and sorts out winners over time.


*Assessment:* Both videos give the same practical rule: don't micromanage creatives, and let the algorithm allocate spend. Neither shows data, and both rest on general knowledge. One creator sells agency services. The official Meta page covers ad-set-level budgeting (50 events in 7 days) and says Advantage+ combines up to 50 assets. It says nothing about how spend is split among creatives or whether to judge at ad-set level, so it neither supports nor contradicts the claim. The rule is plausible with Advantage+ and Andromeda, which favour consolidation. It is weaker for a small budget, where an ad that gets almost no spend may never get a fair test.


*Test with your own data:* Run one Advantage+ app campaign for 14 days with a fixed budget and leave all creatives on. Compare cost per trial (StartTrial) at the ad-set level against the same period after you pause low-spend creatives. Keep whichever setup gives the lower cost per trial with at least 50 events.


- Official source: [https://developers.meta.com/horizon/resources/launch-ad-campaign/](https://developers.meta.com/horizon/resources/launch-ad-campaign/) — “”

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=1719) @28:39 · Burak Mermi · 2026-07-06 · *supports* · basis: general knowledge
  > Hiçbir şeye kreatif seviyesinde bakmayın. Reklam seti seviyesinde bakın.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=784) @13:04 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Ve o assetin minimum bütçesini de atıyorum 5 dolar yapıp.

### <a id="k71"></a>K71 · well supported · confidence 0.94

Since Meta's Andromeda update, advertisers need a large volume of diverse, fresh creatives for good performance and to avoid fatigue.


*Assessment:* Meta's own post says Andromeda copes with advertisers uploading many creatives for diversification and picks the best creative per person. That backs the direction of the claim. It does not say "absurd" volume is required, and third-party sources say the creatives must differ in concept, not just in small tweaks. Both members are agency sellers with no data shown, and they are not independent. The only first-hand signal is a comment about a 3-month creative lifespan at 15–20K leads a month, which is a much larger scale than a small budget.


*Test with your own data:* Run one app-promotion campaign with 3 clearly different concepts (different hook/angle/format) against 6–8 concepts, at the same budget for 2 weeks or until each has about 50 StartTrial events. Compare cost per StartTrial and how quickly performance drops after the first week (frequency and CTR).


- Official source: [https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance) — “as businesses upload more and more creatives to support a diversification strategy”

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=0) @0:00 · Sabri Suby · 2026-06-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > since Meta launched Andromeda, this thing is a hungry panda, and you need to feed it with an absolutely absurd amount of fresh creatives

- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=474) @7:54 · Gui Costa · 2026-07-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > one of the most important things here on meta right now and Andromeda to perform pretty well is volume

### <a id="k72"></a>K72 · likely · confidence 0.63

Meta's ad delivery mostly locks in on very early signals (roughly the first 5–10k impressions or the earliest conversions), so an ad that grabs most of the spend early may be a lucky early winner rather than the best creative.


*Assessment:* Both members make the same general point, but neither is first-hand: one repeats another creator, the other is general knowledge from an agency seller. Meta's docs confirm there is an early learning/exploration phase and that delivery uses predictions, not only past results. They give no 5–10k impression threshold, so that number is unverified. "Mostly optimizes for very early signals" is an oversimplification, because the system keeps updating after learning.


*Test with your own data:* Run two or three creatives in one ad set for about 7 days or 50 trial events. Then duplicate the early spend-hogging ad into a fresh ad set against the runner-up. Compare cost per StartTrial after at least 50 events each. If the early winner keeps the lower cost per trial, early allocation was right.


- Official source: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=231) @3:51 · Sub Club by RevenueCat · 2026-09-15 · *supports* · basis: other creator
  > meta does some sort of a decision making around first five to 10,000 impressions.

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=1238) @20:38 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Facebook mostly optimizes for very early signals.

### <a id="k73"></a>K73 · contested · confidence 0.43

Ad copy length: should B2B SaaS Meta ads use short, clean text, or long-form copy that describes the ideal customer to give the algorithm more signal?


*Assessment:* The two creators give opposite advice on copy length. Both are agency sellers with no data shown, so each rests on general knowledge. Meta's ad guide recommends only a 50-150 character primary text for display, which is a formatting guideline. It says nothing on whether copy length feeds targeting signal, and that is the claim that matters here. Cutri's claim is limited to static ads and says nothing about video. Suby's claim that copy gives the algorithm a bigger context window is an unproven mechanism. Since Andromeda (Dec 2024), creative is the main targeting signal, which may favour what the creative itself conveys over text length.


*Test with your own data:* Run two ads in the same Advantage+ app campaign with the same creative. One has about 100 characters of primary text and the other has 400+ characters that describe the ideal customer. Run both for 7-14 days, or until each has at least 50 trial starts. Compare cost per StartTrial and the trial-to-paid rate.


- Official source: [https://www.facebook.com/business/ads-guide/image/facebook-feed/traffic](https://www.facebook.com/business/ads-guide/image/facebook-feed/traffic) — “”

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=523) @8:43 · Alessandro Cutri · 2026-06-04 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > you want the text to be a lot shorter and cleaner because otherwise you're going to just lose people with a static ad

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=591) @9:51 · Sabri Suby · 2026-06-12 · *contradicts* · basis: general knowledge · conflict of interest: sells agency services
  > Therefore, the context window that Meta has is very very small.

### <a id="k74"></a>K74 · well supported · confidence 0.82

To validate Meta app tracking, compare Meta's reported installs or trial starts with App Store Connect (for example, the App Referrer report filtered to Facebook, Instagram and WhatsApp). A modest gap is acceptable.


*Assessment:* Both creators recommend cross-checking Meta numbers against App Store Connect, and the method is plausible. Third-party sources say SKAN and Meta figures typically differ by roughly 5–15% because of modeling, delays and privacy thresholds. One member is a single case (276 vs 312, about 11.5% lower) from an agency/course seller. The other is general knowledge with no data. Meta's official docs I searched were silent on this comparison. The App Store Connect side counts installs and attributed sources, not necessarily trial starts, so the two members are not strictly the same check.


*Test with your own data:* Over the next 28 days, record Meta installs and trial starts weekly. Compare them with App Store Connect (App Referrer for installs, subscription reports for trials). If the gap stays under about 15% and stable, tracking is likely fine. If it is larger or erratic, check the SDK and event setup.


- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=694) @11:34 · App Masters · 2026-10-20 · *supports* · basis: own experience · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > We have 312 under App Store Connect. On meta, we had 276.

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=686) @11:26 · Gui Costa · 2026-07-25 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > you click here in App Referrer and you put Facebook Instagram and WhatsApp messaging

### <a id="k75"></a>K75 · likely · confidence 0.62

Before turning a creative on or off in a Meta app-install campaign, give it a minimum amount of spend (about $100 per creative, or enough to reveal a bad CPA), because Meta's spend allocation can distort results.


*Assessment:* The two members are only loosely the same claim. Cravotta gives a $100 floor from general knowledge, and he sells a course. The RevenueCat guest describes a single audited account where a $100 CPI was left running to over $100k, and the rule of thumb of killing it at about $2,000 is a different number. I couldn't fetch any official Meta page that sets a per-creative spend threshold. Practical spend needed depends on your CPA: $100 buys about 1 trial at a $100 CPI, and far fewer trial or paid events for a B2B subscription.


*Test with your own data:* For two weeks, set a kill rule of about 10-20x your target cost per trial (not a flat $100) per creative. Compare your cost per StartTrial for creatives cut at that rule against ones left running, and see whether the rule saves spend without removing eventual winners.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=1636) @27:16 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > I recommend spending at least a hundred dollars on each creative before you decide whether to turn it on or off.

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=310) @5:10 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · basis: client data
  > Alper once audited an account that had spent over $100,000 on a single creative with a cost per install of $100.

### <a id="k76"></a>K76 · contested · confidence 0.58

Launch new creatives every week and keep testing angles on Meta app campaigns; serious accounts test as many as 25 or more new creatives per week.


*Assessment:* Both members agree that fresh creative should ship weekly. Both are unsupported by data: one is general knowledge from an agency seller, the other is another creator's claim. The weekly cadence is plausible, because creative diversity matters more in the Andromeda era. The "25 per week" figure is a threshold for large-spend accounts and is not documented anywhere. A small-budget account can't fund that volume, so it is probably too high. The Meta docs I checked say nothing about cadence.


*Test with your own data:* For 3 to 4 weeks, ship 3 to 5 genuinely different new creative angles per week into the same campaign. Retire the clear losers. Compare cost per StartTrial and cost per paying customer against the prior 4 weeks.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/advantage-app-campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/advantage-app-campaigns) — “”

- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=686) @11:26 · Gui Costa · 2026-07-25 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Be launching every week new creatives so you can start you can test more angles

- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=75) @1:15 · Sub Club by RevenueCat · 2026-09-15 · *qualifies* · basis: other creator
  > serious accounts are testing at least 25 new creatives a week.

### <a id="k77"></a>K77 · well supported · confidence 0.93

Test only one variable (or at most one or two) at a time so you can attribute performance changes to a specific change.


*Assessment:* Meta's split-testing documentation explicitly says to test one variable at a time, and both creators say the same. One is general knowledge from a course seller. The other is first-hand experience from an agency seller, with no data shown. This is standard testing practice, so the low evidence quality matters little. Caveat: with a small budget and Advantage+ delivery, isolation is imperfect because the algorithm allocates spend unevenly across ads.


- Official source: [https://developers.facebook.com/docs/marketing-api/guides/split-testing](https://developers.facebook.com/docs/marketing-api/guides/split-testing) — “While you can test many different types of variables, test only one variable at a time.”

- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=390) @6:30 · Steven Cravotta · 2026-07-30 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > you can only test one of these things at a time, whether it's changing your content, changing your messaging

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=232) @3:52 · Aazar Shad · 2026-04-02 · *supports* · basis: own experience · conflict of interest: sells agency services
  > I had like probably like 50 plus similar ads, and I was just testing one thing or two things

### <a id="k78"></a>K78 · contested · confidence 0.59

For B2B SaaS paid social, roughly $150–$200 per booked demo or call is a workable benchmark (for example, about $10K of spend yielding about 60 booked calls, or about $167 each).


*Assessment:* Both members land in a similar range ($200 per demo versus about $167 per call from $10K and 60 calls). Both come from agency sellers, one is general knowledge, and the other is unshown client data. Neither is independently verified, and a commenter points out that the first video's numbers are confusing. Meta's docs publish no such benchmark. Third-party sources put demo or trial CPL at about $120–$250, which is consistent but not authoritative. The figures depend heavily on offer, targeting and audience, and they apply to lead or booked-call objectives. They do not apply to app-install or StartTrial campaigns.


*Test with your own data:* Run a lead or demo campaign with a fixed budget, for example $1,500–$2,000 over 2–3 weeks, and compare your cost per booked demo with the $150–$200 range. Also track the show rate and cost per paying customer, not just the booking cost.


- Official source: [https://www.facebook.com/business/help](https://www.facebook.com/business/help) — “”

- [How I Run Facebook Ads For a B2B SaaS Company](https://youtu.be/6802r3zLtdo?t=153) @2:33 · Alessandro Cutri · 2026-06-04 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > this campaign is set up for success if we can hit a $200 cost per demo.

- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=692) @11:32 · Lorenzo Pravatà · 2026-03-26 · *supports* · basis: client data · conflict of interest: sells agency services
  > you might get with 10K outspend, maybe 60 booked calls

### <a id="k79"></a>K79 · well supported · confidence 0.92

The App promotion objective is only for businesses that have a mobile app to promote; businesses without an app should not use it.


*Assessment:* Both creators say the same thing, and it is close to a definition: app promotion campaigns drive installs of an app, so they need an app. Both are general knowledge and both creators sell agency services, but the claim is not about efficacy, so that matters little. The developer docs tie these campaigns to app installs, which is consistent with the claim.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “Specify `APP_INSTALLS` for this type of ads.”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=742) @12:22 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > If you've got an app, obviously the option to use. If you don't, don't use it.

- [İnstagram Reklam Verme 2026 - Meta Business Kurulumu ve İnstagrama Rek](https://youtu.be/quwU3ZjWclw?t=1015) @16:55 · Kamil YILDIRIM · 2026-05-31 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Uygulama tanıtım reklamlarında biz mobil uygulamamız varsa bunların tanıtımını yapıyoruz.

### <a id="k81"></a>K81 · likely · confidence 0.67

Square (1:1) creatives shown in 9:16 Stories/Reels placements perform poorly or get cropped (text cut off), so build separate vertical 9:16 creatives for those placements.


*Assessment:* Two independent practitioners (AdConversion, Ben Heath) give the same advice from their own experience, and it matches common creative guidance that Stories and Reels need full-screen 9:16. Both sell courses or agency services, but this is a low-stakes production tip, not an income claim. Neither shows performance data. The Meta Ads Guide pages I tried returned 404, so the docs check is silent. The "doesn't perform" part is anecdotal, while the text-cropping part is a mechanical risk. Note that Meta can auto-adapt creatives with Advantage+ enhancements, so how badly it crops depends on the setup.


*Test with your own data:* Upload one 9:16 version of your best square ad into the same Advantage+ app campaign. After about 7 days, or at least 50 installs or trials per variant, compare cost per StartTrial for Stories/Reels placements in the placement breakdown.


- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=313) @5:13 · AdConversion · 2025-11-12 · *supports* · basis: own experience · conflict of interest: sells a course, sells agency services
  > The story placement doesn't look very good. It doesn't perform.

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=2813) @46:53 · Ben Heath · 2026-01-06 · *supports* · basis: own experience · conflict of interest: sells a course, sells agency services, paid community
  > That just doesn't work, right? Cuts off all the text.

### <a id="k83"></a>K83 · likely · confidence 0.66

Meta's learning phase ends once an ad set collects about 50 optimization events within 7 days after its last significant edit.


*Assessment:* Both members give the same 50-events-in-7-days rule. Neither is independent first-hand evidence: one repeats Meta's documentation and the other is general knowledge. The Meta help page "About the Learning Phase" appeared in search, but I couldn't read its body, so I can't quote it. Search summaries and third-party sources consistently describe about 50 events as the exit threshold. The figure is a guideline, not a hard rule. The 7-day window is measured from the last significant edit. Post-Andromeda exit times may run longer, and small budgets often end up "Learning limited". For a small-budget B2B app, 50 StartTrial events a week may be unaffordable.


- Official source: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=1018) @16:58 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: platform docs · conflict of interest: sells agency services
  > Meta kampanya iyi çalışıp çalışmada başarılı olup olmadığını aslında haftada yani 7 gün içerisinde 50 tane bu optimizasyon eventini toplarsa sağlıyor.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=384) @6:24 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > many accounts have a learning curve of seven days for 50 conversions

### <a id="k84"></a>K84 · contested · confidence 0.58

Meta's learning phase typically lasts about 24–48 hours, depending on conversion volume, and account quality signals (business verification, 2FA, account age) may shorten it.


*Assessment:* Both members are general-knowledge statements from course/agency sellers, with no data shown. Meta's documented rule of thumb ties exit from learning to about 50 optimization events per week, so 24–48 hours is only reachable with enough conversion volume. Ben Heath's commenters (Rs 1000/day, stuck 8 days) show that low budgets with expensive events stay in learning far longer. The account-quality claim from Burak Mermi is not supported by anything I could find in the docs I could read, and I could not retrieve the full docs page text.


*Test with your own data:* Run one app-promotion ad set optimizing for StartTrial for 7 days and note the days until the status leaves Learning and the number of StartTrial events. Run a second ad set optimizing for a higher-volume event such as install or registration. Success metric: days in learning and cost per trial.


- Official source: [https://www.facebook.com/business/help/112167992830700](https://www.facebook.com/business/help/112167992830700) — “”

- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=154) @2:34 · Ben Heath · 2026-02-20 · *qualifies* · basis: general knowledge · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > The learning phase lasts typically, let's say 24 to 48 hours, but it is dependent on conversion volume.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=384) @6:24 · Burak Mermi · 2026-02-16 · *qualifies* · basis: general knowledge · conflict of interest: sells a course
  > have completed business verification, have two-factor authentication, and have been advertising for a long time

### <a id="k85"></a>K85 · contested · confidence 0.60

For subscription apps, Meta is the best or one of the best paid acquisition platforms, and works more often than TikTok.


*Assessment:* Two different channels agree that Meta ranks first for subscription apps. Both are agency-linked, and neither shows data on screen. One cites client observations ("more frequent to see companies succeeding in Meta than TikTok"), and the other is a general opinion. The official docs say nothing comparing platforms, so the claim can't be confirmed or refuted. It is plausible as a starting heuristic, but it depends on the app, the market, and the creative.


*Test with your own data:* Run Meta for 2 weeks with a fixed budget, and run a second platform (TikTok or Google) with similar budget and creatives. Compare cost per trial start and the trial-to-paid rate, and check whether Meta's CAC is lower.


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “”

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=228) @3:48 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > The best chances are on Meta, then on Google, then maybe Apple Search Ads, and then along maybe TikTok.

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2973) @49:33 · RevenueCat · 2026-09-12 · *supports* · basis: client data · conflict of interest: sells agency services
  > it's more frequent to see companies succeeding in meta than in tick tock

### <a id="k86"></a>K86 · single source · confidence 0.54

In US app-install campaigns, an IPM (installs per 1,000 impressions) below about 5 is weak, while about 10–15 signals a campaign or creative that is ready to scale.


*Assessment:* Both members come from the same Adapty-run channel family, and both sell agency services. One is based on experience and the other on general knowledge. Neither shows data, so they are not independent evidence. Meta's docs give no IPM benchmarks. The thresholds are plausible rules of thumb for US install-objective tests, but they don't apply directly to the topic's real goal, which is trial starts and paying customers on a B2B subscription app. Install IPM says little about trial quality.


*Test with your own data:* Run 3–5 creatives in an install test for about 3–5 days. Record IPM for each, then compare it with the cost per trial and the trial-to-paid rate of the installs it produced. Success: the creatives with IPM above 10 also have a lower cost per trial than those below 5.


- Official source: [https://www.facebook.com/business/help/335457916629140](https://www.facebook.com/business/help/335457916629140) — “”

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=774) @12:54 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: own experience · conflict of interest: sells agency services
  > if you have less than five IPM, you might have harder chances. And if you have 10, 15, go for it.

- [Adapty Talks · Bölüm 9 — Subscription app’lerde Meta Ads’e ilk $10K’yı](https://youtu.be/or8ciNzg6Cw?t=1016) @16:56 · App Leaders Club Türkiye by Adapty · 2026-02-09 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > IPM'iniz 5'in altında olmamalı diye düşünüyorum.

### <a id="k87"></a>K87 · single source · confidence 0.67

In the creator's review of 100 Meta accounts, a single CBO campaign with one ad group and many creatives had a 21% success rate at small budgets, 16% at mid and 14% at high budgets.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=543) @9:03 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > küçük bütçelerde %21 başarı oranına sahipmiş bu kampanya

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=620) @10:20 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > küçük bütçelerde %7, orta bütçelerde %9, yüksek bütçelerde de %3 başarı oranına sahip

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=700) @11:40 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > küçük bütçelerde daha iyi çalışmış %28, orta bütçelerde %32

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=700) @11:40 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > orta bütçelerde %28 çalışma oranı, yüksek bütçelerde ise %33 çalışma oranıyla

- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=620) @10:20 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > bu kampanyanın küçük bütçelerde çalışma oranı neredeyse yok diyebiliriz

### <a id="k104"></a>K104 · unverifiable · confidence 0.55

Before scaling Meta app campaigns for a subscription app, install-to-trial activation should be at least about 5–10%, and 10% or more with a hard paywall.


*Assessment:* Both members come from one video by one creator who sells agency services and courses and is sponsored. The thresholds are stated verbally with no data and no stated basis. Meta's docs describe Start Trial as an optimization event but give no install-to-trial benchmark. Third-party benchmarks vary widely (roughly 15–30% on Adapty or RevenueCat definitions), and they depend on how installs are counted. The 5–10% figure is a plausible rule of thumb but is not verified.


*Test with your own data:* Compute your own install-to-trial rate from MMP or RevenueCat data over the last 14 days, using the same install count as Meta. Run the Start Trial optimization campaign for at least 7 days on a small budget. Compare cost per trial and trial-to-paid against that rate, and scale only if CAC per paying customer is acceptable.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=154) @2:34 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > You want to at least have five to 10% install the trial activation

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=233) @3:53 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > If you have a hard paywall, you're aiming for at least 10% plus on that trial activation.

### <a id="k105"></a>K105 · unverifiable · confidence 0.54

For a subscription app, a paid intro offer is preferable to a plain free trial once trial activation exceeds about 10%, and at the higher monthly-equivalent price it can reach roughly 60–70% trial-to-paid.


*Assessment:* Both members come from one creator in one video. That creator sells a course and agency services and the video is sponsored. Neither claim has data or evidence behind it; they are verbal rules of thumb. Meta's docs only describe the StartTrial and Subscribe events and say nothing about paid intro offers or these thresholds. The 60–70% figure is also probably inflated by selection: people who pay up front are already committed.


*Test with your own data:* Run a 2–4 week A/B test of a free trial against a paid intro offer in the same app, with similar traffic. Compare cost per paying subscriber, and 30-day retention or refund rate. Keep the test only if the paid intro offer produces a lower CAC per retained subscriber.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “”

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=456) @7:36 · App Masters · 2026-06-09 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, sponsored
  > But on that one 99 a month, that's when you're gonna get above 60, 70% trial to paid.

- [56% More Trials With This One Change](https://youtu.be/bg0_DavI-DE?t=456) @7:36 · App Masters · 2026-06-09 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, sponsored
  > if you already got a great trial activation, okay, like above 10%, I would do the paid intro offers.

### <a id="k107"></a>K107 · single source · confidence 0.63

For the Built With Science fitness app (~$189/year), trial-to-paid conversion is about 25% from Meta ads and about 35–40% from warm organic YouTube traffic.


*Assessment:* Both claims come from one first-hand operator on one podcast episode and were stated verbally, with no screen-shown data. They are plausible: warm organic audiences usually convert better than cold paid traffic. Meta's docs define the trial metrics but give no benchmark for trial-to-paid, so they can't confirm or refute the figures. They are single-source and describe one B2C fitness app, so they are not a benchmark for B2B.


*Test with your own data:* Over 2–4 weeks, compare trial-to-paid conversion by source in your subscription tool (for example RevenueCat), splitting Meta-ad trials from organic trials. Use cohorts of at least 100 trials each. The success metric is the paid share at the end of the trial, and the cost per paying customer (CAC) for Meta.


- Official source: [https://www.facebook.com/business/help/215003022531733](https://www.facebook.com/business/help/215003022531733) — “”

- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1982) @33:02 · Sub Club by RevenueCat · 2026-09-02 · *supports* · basis: own experience
  > And trial to paid for meta is slightly lower, around 25%.

- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1982) @33:02 · Sub Club by RevenueCat · 2026-09-02 · *supports* · basis: own experience
  > we are around the 35% to 40% range.

### <a id="k111"></a>K111 · unverifiable · confidence 0.53

For Meta ads, a creative frequency of 1–2 is healthy, 2–3.5 is risky, and above 3.5 indicates creative fatigue.


*Assessment:* Both members come from one creator who sells a course. They state the thresholds as a rule of thumb, with no data shown. Meta's docs say fatigue shows up as frequency rises together with falling CTR and rising cost per action. They give no numeric cutoffs, so the docs are silent on these numbers. The only comment (2000 TL/day with 4 creatives, add more if frequency rises) is about operations and doesn't confirm the numbers. In practice, tolerable frequency depends on budget, audience size and the optimization event, so one fixed cutoff is unlikely to hold everywhere.


*Test with your own data:* For 2 weeks, log frequency, CTR and cost per trial (StartTrial) for each creative every day. Find the frequency at which cost per trial rises more than 25–30% above its first-week level. Use that as your own fatigue threshold and compare it with 3.5.


- Official source: [https://www.facebook.com/business/help/1346816142327858](https://www.facebook.com/business/help/1346816142327858) — “”

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1385) @23:05 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > If your creative frequency metric is between 1 and 2, we can call it a healthy frequency metric.

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1462) @24:22 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > The fatigue level is above 3.5.

### <a id="k132"></a>K132 · unverifiable · confidence 0.54

A subscriber reportedly made 9,000 MXN in one hour with a 200 MXN budget using the creator's methods.


- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=155) @2:35 · Aprendamos Marketing · 2026-01-13 · *—* · basis: client data · conflict of interest: sells agency services
  > logró hacer 9000 pesos en una hora con 200 pesos de presupuesto

### <a id="k133"></a>K133 · unverifiable · confidence 0.54

A subscriber who launched a campaign on 29 September 2025 reportedly quadrupled sales by 10 October 2025.


- [Cómo hacer Publicidad en Facebook 2026 (META ADS para negocios)](https://youtu.be/Dnh1Ki45zKw?t=155) @2:35 · Aprendamos Marketing · 2026-01-13 · *—* · basis: client data · conflict of interest: sells agency services
  > y el 10 de octubre ya logró cuadruplicar sus ventas

### <a id="k146"></a>K146 · single source · confidence 0.57

Predicted LTV signals did not always improve results; the speaker found that sending PLTV did not help when the underlying model did not make sense.


- [Scaling Subscription Apps Past $100K MRR: Advanced UA Tactics for Subs](https://youtu.be/QdIGi-tKr28?t=2529) @42:09 · App Leaders by Adapty · 2026-09-11 · *—* · basis: own experience · conflict of interest: sells agency services
  > And I did have experiences where sending PLTV didn't really make things better

### <a id="k154"></a>K154 · unverifiable · confidence 0.55

Heath Media says it has achieved a 20x ROAS for some clients and 3.2x at scale for others (not independently verifiable).


- [How to CRUSH Facebook Ads with a Small Budget in 2026](https://youtu.be/XLagiyzYYpE?t=1220) @20:20 · Ben Heath · 2026-02-20 · *—* · basis: client data · conflict of interest: sells a course, sells agency services, affiliate, sponsored
  > We will show the businesses that we're able to get a 20x return on ad spend for

### <a id="k159"></a>K159 · well supported · confidence 0.91

If you run only AEM (Aggregated Event Measurement) iOS app campaigns on Meta, you do not need to configure SKAdNetwork, because AEM does not use SKAdNetwork.


*Assessment:* Meta's docs present AEM and SKAdNetwork as two separate values of campaign_attribution, which is consistent with the claim. The claim comes from a single creator who sells agency services and is giving general knowledge, not first-hand evidence. The docs describe this as an attribution choice and do not state that you can skip SKAdNetwork setup in general. Whether any SKAdNetwork configuration is still needed depends on how the campaign is set up and on current Meta defaults.


- Official source: [https://developers.facebook.com/docs/app-ads/SKAdNetwork-aem-and-limitations/](https://developers.facebook.com/docs/app-ads/SKAdNetwork-aem-and-limitations/) — “If you want to use Meta's Aggregated Event Measurement, then set this field to AEM.”

- [Launching your first Start Trial mobile app campaign on Meta Ads with ](https://youtu.be/x2tKbtJoSrM?t=929) @15:29 · First Try · 2026-02-03 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > If you are launching only AEM campaigns because AEM doesn't use SK AdNetwork.

### <a id="k166"></a>K166 · single source · confidence 0.63

A no-trial option (pay upfront with 20% off) versus a 14-day free-trial toggle performed worse for the warm organic audience, because the extra friction hurt even with a 30-day money-back guarantee.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=3326) @55:26 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > we're seeing it's quite negative just because it does, of course, add a little more friction

### <a id="k170"></a>K170 · well supported · confidence 0.90

Value-based optimization on Meta requires conversion tracking that sends the value of each lead or purchase back to Meta (Meta pixel and/or Conversions API); without it the optimization cannot work.


*Assessment:* Meta's developer docs say value and currency must be added to the events used for value optimization. They can be sent via the pixel, the Conversions API, or both. The creator's "pixel" wording is slightly narrow, because the Conversions API alone works too. For an app campaign, the SDK or an MMP sends the value instead of the pixel. The core point, that without value data it can't work, is standard and uncontroversial. The speaker sells courses and agency services, but this is a basic mechanic, not an efficacy claim, so that conflict matters little.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/value-optimization](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/value-optimization) — “Value and currency should be added to existing events you want to use value optimization for.”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1408) @23:28 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > you're going to need to have the Meta pixel installed and the values of each lead being sent back to Meta.

### <a id="k187"></a>K187 · single source · confidence 0.63

Sending trial starts as a Trial event instead of as Purchase lowered one audited app's cost per trial by roughly 35% without changing ads.


- [Before you spend more on Meta Ads, watch this](https://youtu.be/E9NF-6AjQhs?t=389) @6:29 · Sub Club by RevenueCat · 2026-09-15 · *—* · basis: client data
  > All we did was mapping their trial event to trial and the actual cost per trial went down by I think around 35%.

### <a id="k192"></a>K192 · well supported · confidence 0.90

With the Andromeda update, Meta reports about 3x higher inference throughput (queries per second) and about 6% better recall in ad retrieval.


*Assessment:* Meta's engineering blog confirms over 3x higher QPS and +6% recall improvement. The speaker gave no source and paraphrased loosely: "faster query response" is really throughput (QPS), and "relevance" is really recall. The numbers are Meta's own self-reported figures, and the speaker sells agency services. The claim is a platform-mechanic fact with no direct effect on trial or CAC results.


- Official source: [https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/) — “The effort has enhanced end-to-end model inference queries per second (QPS) by over 3x.”

- [Meta Reklamları 2026: Algoritma, Kampanya Yapısı ve Kreatif Dönemi](https://youtu.be/PjvKJQfGg9Q?t=160) @2:40 · Menaf Avcı · 2025-12-28 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > 3 kat daha hızlı sorgu yanıtı artmış.

### <a id="k207"></a>K207 · single source · confidence 0.55

Switching to a skit-style UGC ad with a relatable creator dropped cost per free trial from about $60 to about $30, which became the new benchmark.


- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=463) @7:43 · Aazar Shad · 2026-04-02 · *—* · basis: own experience · conflict of interest: sells agency services
  > I remember like we were like 60 and then suddenly the cost per free time went to 30 and that was our new standard

### <a id="k212"></a>K212 · single source · confidence 0.57

Founder-recorded content, where the founder explains how they use the app, is among the best-performing ad creative in the speaker's experience with clients.


- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2656) @44:16 · RevenueCat · 2026-09-12 · *—* · basis: client data · conflict of interest: sells agency services
  > their own content is one of the best performing contents that i've seen

### <a id="k215"></a>K215 · single source · confidence 0.56

Meta doesn't show hook rate or hold rate for the old AAA (Automated App Ads) campaign type, and the speaker believes that campaign type no longer exists.


*Assessment:* The docs confirm that AAA was renamed Advantage+ app campaigns. So the campaign type isn't gone; it has a new name. The docs say nothing about hook or hold rate reporting. Those are usually computed from video metrics such as 3-second plays and ThruPlays, not shown as built-in columns. The claim comes from one agency-selling speaker with no evidence shown, so it is only partly right: the rename is true, but "doesn't exist" is misleading.


*Test with your own data:* In Ads Manager, open your Advantage+ app campaign. Add the 3-second video plays and ThruPlays columns, or build a custom metric. Compute hook rate as 3-second plays divided by impressions, and hold rate as ThruPlays divided by 3-second plays. This takes minutes. If the columns appear, the metrics are available to you.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/advantage-app-campaigns](https://developers.facebook.com/documentation/ads-commerce/marketing-api/advantage-catalog-ads/advantage-app-campaigns) — “Advantage+ app campaigns (formerly known as Automated App Ads (AAA))”

- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1322) @22:02 · Aazar Shad · 2026-04-02 · *qualifies* · basis: own experience · conflict of interest: sells agency services
  > Meta does not even give you like hook rate, hold rate of all those

### <a id="k257"></a>K257 · unverifiable · confidence 0.54

The agency's client generated $800,000 in new business pipeline from Meta ads after initially being skeptical and running LinkedIn-focused campaigns.


- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=0) @0:00 · AdConversion · 2025-11-12 · *—* · basis: own experience · conflict of interest: sells a course, sells agency services
  > they opened up $800,000 in new business pipeline from meta ads as a channel

### <a id="k258"></a>K258 · unverifiable · confidence 0.54

Meta has produced roughly half the cost per lead of LinkedIn for the agency's B2B clients, with lower cost per qualified opportunity.


- [Meta Ads for B2B: What Actually Works in 2026](https://youtu.be/9lfItyusOmw?t=0) @0:00 · AdConversion · 2025-11-12 · *—* · basis: own experience · conflict of interest: sells a course, sells agency services
  > I'm talking half the cost per lead, lower cost per qualified opportunity.

### <a id="k263"></a>K263 · single source · confidence 0.60

In Ads Manager, Campaign Budget Optimization (CBO) is now labelled "Advantage Campaign Budget".


*Assessment:* This is a naming fact from a single member whose basis is general knowledge. The official developer page uses the term "Advantage campaign budget" for the feature, and it still links to "About campaign budget optimization". It doesn't state the rename outright. Several third-party sources also describe the rename, and nothing credible contradicts it. The point is low-stakes and consistent with how Meta now labels the feature.


- Official source: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “”

- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=397) @6:37 · Benji · 2026-10-20 · *supports* · basis: general knowledge
  > In Ads Manager, it's now called Advantage Campaign Budget.

### <a id="k269"></a>K269 · single source · confidence 0.63

Before scaling paid spend, measure a trial-to-paid baseline for cold paid traffic (took about one month) and use it to calculate the maximum allowable spend per customer.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1188) @19:48 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > we just needed to get a baseline of what that number would be in order for us to calculate how much we could actually spend to our customer

### <a id="k272"></a>K272 · well supported · confidence 0.94

Ads Manager has an AI-powered feature that analyzes an ad's performance and suggests improvements.


*Assessment:* The claim is a simple UI-feature description shown on screen in Ads Manager. Meta's own page says the Meta AI business assistant gives campaign recommendations inside Ads Manager, which matches it. The creator sells agency services, but that does not matter for a feature-existence claim. Exact button name and availability may vary by account and region.


- Official source: [https://www.facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors) — “Use Meta AI business assistant for what it does best: personalized guidance, issue resolution, and campaign recommendations”

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1319) @21:59 · Nida Yıldırım · 2026-04-29 · *supports* · basis: platform docs · conflict of interest: sells agency services
  > reklamınızın analizini bu kısımdan yaptırabiliyorsunuz yapay zeka üzerinden

### <a id="k273"></a>K273 · well supported · confidence 0.91

The ad account's payment card must stay valid with enough balance, otherwise ads stop and the account may be restricted or closed.


*Assessment:* This is a basic billing mechanic. Meta's Help Center covers payment failures and recommends a backup payment method; search results indicate ads pause until the outstanding balance is paid. The creator's claim is general knowledge and she sells agency services, but the claim is low-risk and matches the docs. "Closed" is a stronger outcome than the usual pause. Repeated failures can lead to a disabled account, so the claim is slightly overstated but directionally right.


- Official source: [https://www.facebook.com/business/help/2726198024366416](https://www.facebook.com/business/help/2726198024366416) — “”

- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=1558) @25:58 · Nida Yıldırım · 2026-04-29 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Ödeme bilgilerinizde kartınız güncel olmalı ve kartınızda sürekli bakiye olmalı.

### <a id="k274"></a>K274 · single source · confidence 0.64

Before running conversion campaigns on a new Meta ad account, warm it up for about five days with a harmless engagement campaign using static ads, then run seven days of engagement; the speaker says fresh accounts that start converting immediately often won't spend at all.


- [5 Steps to Scale Your App With Meta Ads in 2026](https://youtu.be/P3kJIY0-0xQ?t=317) @5:17 · Benji · 2026-10-20 · *—* · basis: own experience
  > set up an engagement campaign, just run some harmless static ads, put them on five days, do seven days of engagement, and then just set up conversion campaigns.

### <a id="k282"></a>K282 · single source · confidence 0.63

The quiz-versus-App-Store gap appears on iOS only; a quiz on Android converted at the same rate as the web quiz.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1594) @26:34 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > that actually is converting equivalent to our conversions on the web

### <a id="k286"></a>K286 · single source · confidence 0.63

Showing only the annual plan first on the paywall, with the price unchanged, shifted subscription choice from roughly 60/40 monthly/annual to about 75-80% annual.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=3168) @52:48 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > all we did was change the layout so that it presented the annual up front and reduce risk of actually starting the free trial

### <a id="k295"></a>K295 · well supported · confidence 0.90

Meta's predicted lifetime value (pLTV) optimization requires at least 100 conversions per week and allows only one event per dataset to carry the predicted value, which is restrictive for new apps.


*Assessment:* Meta's pLTV page confirms both the 100 conversion events per week minimum (for each of the last 4 weeks) and the limit of one pLTV event per dataset. The member's claim comes from general knowledge, but the docs back it. The docs also say pLTV does not currently support app events, so the claim may not apply to app campaigns at all. For a small-budget B2B subscription app, 100 attributed events per week is hard to reach, especially for paid conversions.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “You have a minimum of 100 conversion events per week attributed to Meta for each of the last 4 weeks.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1639) @27:19 · RevenueCat · 2026-09-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > you need to have at least more than 100 conversions per week

### <a id="k341"></a>K341 · single source · confidence 0.62

In the creator's review, accounts with a high creative-diversity score (7-10 on his subjective scale) had higher success rates than low-diversity accounts (1-3), regardless of budget.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2251) @37:31 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > kreatif farklılık puanı yüksek olan hesaplarda bütçe fark etmeksizin başarı oranının arttığını görüyorsunuz

### <a id="k342"></a>K342 · single source · confidence 0.62

In the creator's review, accounts whose ads were fully AI-generated and uploaded directly failed regardless of budget, while human-designed or real-content accounts had higher success rates.


- [100 Meta Reklam Hesabını İnceledim | Meta Ads En İyi Ölçekleme Yönteml](https://youtu.be/yWNVkb32lXM?t=2326) @38:46 · Burak Mermi · 2026-07-06 · *—* · basis: client data
  > Bu tarz hesaplar bütçe fark etmeksizin başarısız olmuş

### <a id="k353"></a>K353 · well supported · confidence 0.93

Meta's Advantage+ Creative now includes video generation tools that turn static image ads into video, including 9:16 vertical format.


*Assessment:* The single member repeats a platform feature with no on-screen evidence. Meta's developer docs describe an image_animation enhancement that turns a static image into a short animated video, which matches the gist. The docs don't say "9:16 video generation" explicitly, and availability varies by account and rollout, so the claim holds only in part.


- Official source: [https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started](https://developers.facebook.com/docs/marketing-api/creative/advantage-creative/get-started) — “a static image in your ad to be automatically transformed into a short animated video that adds subtle motion”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=624) @10:24 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: platform docs · conflict of interest: sells agency services
  > Video Generation tool'lara geldi.

### <a id="k356"></a>K356 · well supported · confidence 0.90

Send the key optimization event (trial or purchase) to Meta as fast as possible after it happens, within minutes or seconds.


*Assessment:* Meta's docs recommend sending events in real time or within 1 hour, so the direction of the advice is supported. The "within seconds" precision is stricter than the docs require, and the creator gives no evidence (general knowledge, agency seller). Faster is better, but the gain from seconds versus minutes is unproven; the docs only show that long delays (24 hours or more) clearly hurt.


- Official source: [https://developers.facebook.com/docs/marketing-api/conversions-api/guides/end-to-end-implementation](https://developers.facebook.com/docs/marketing-api/conversions-api/guides/end-to-end-implementation) — “Sending your events in real time or within 1 hour helps ensure that they can be used for attribution and optimized for ad delivery.”

- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=1177) @19:37 · App Leaders by Adapty · 2025-12-26 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > make sure that your most important signal is sent to Meta within the first few minutes, if not first few seconds

### <a id="k364"></a>K364 · well supported · confidence 0.91

Meta app campaigns can optimize for custom in-app events, not only standard events such as purchase or start trial.


*Assessment:* Meta's developer docs confirm custom app event optimization exists, set with the OFFSITE_CONVERSIONS goal and a custom_event_str. It is not new, though. The 2016 docs already describe it, so "now" is loose. The docs limit it to the App Installs objective, and other pages describe a different Advantage+ app structure, so availability depends on the setup. The only source is one speaker with general knowledge, who sells agency services.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “At this time, optimising for custom app events is only available in the App Installs objective.”

- [Mobil Uygulamalarda Meta Ads: Sinyal Optimizasyonu, İleri Seviye UA Ta](https://youtu.be/V6cRfcRarAM?t=624) @10:24 · App Leaders Club Türkiye by Adapty · 2026-08-27 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > Aslında custom event optimization yapabiliyorsunuz artık.

### <a id="k370"></a>K370 · well supported · confidence 0.92

In Advantage+ audience ad sets, audience controls (location, minimum age, languages, custom audience exclusions) are hard limits, while audience suggestions are only signals that Meta may go beyond.


*Assessment:* Meta's Advantage+ audience page lists minimum age, location, language and custom audience exclusions as controls the AI stays within. Suggestions are described as a priority signal, not a restriction. Ben Heath's claim matches this. He sells courses and agency services, but the claim is a documented mechanic rather than an efficacy claim, so that conflict matters little. The page was fetched in Turkish, so the quotes are in Turkish.


- Official source: [https://www.facebook.com/business/ads/meta-advantage-plus/audience](https://www.facebook.com/business/ads/meta-advantage-plus/audience) — “Hedef kitle önerileri eklediğinizde sistem, bu profille eşleşen hedef kitlelere öncelik verir.”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=1706) @28:26 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > anything set within the control section is a hard constraint, a hard boundary.

### <a id="k374"></a>K374 · well supported · confidence 0.91

With campaign budget optimization (CBO), Meta dynamically distributes spend toward the best-performing ad sets, ads, times and placements, while ad set budgets spend more linearly.


*Assessment:* Meta's docs confirm that campaign-level budget is distributed in real time across ad sets toward the best opportunities. The docs say nothing about spend being spread "linearly" across the day under ad set budgets, or about time-of-day or placement shifting. Those parts rest on general knowledge from one course seller with no evidence shown. The core mechanic is sound, but the details are unverified.


- Official source: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “Facebook automatically and continuously finds the best available opportunities for results across your ad sets”

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=156) @2:36 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > the CBO campaign uses dynamic intelligent distribution

### <a id="k375"></a>K375 · single source · confidence 0.55

After Meta's Andromeda update, the creator sees better results when the budget is set at ad set level rather than campaign level.


- [0’dan İleri Seviyeye Meta Reklam Eğitimi (Gerçek Stratejilerle)](https://youtu.be/fevjPnlXjqM?t=781) @13:01 · Nida Yıldırım · 2026-04-29 · *—* · basis: own experience · conflict of interest: sells agency services
  > ben reklam seti bütçesinde çok daha iyi sonuçlar alındığını görüyorum

### <a id="k378"></a>K378 · well supported · confidence 0.91

Early results in a new Meta campaign are unstable (for example, early sales spikes followed by drops) because the delivery system is still in the learning phase, so give it time and avoid premature changes.


*Assessment:* Meta's help center describes the learning phase as a period when delivery is still being optimized and performance is less stable, which matches the general mechanism. The search summary also shows that significant edits restart learning and that about 50 optimization events per week are needed to exit it. The page text could not be fetched, so I have no verbatim quote. The member is a single, verbal, general-knowledge statement from a course seller. The "spike then drop" explanation is plausible but only one of several causes, such as audience saturation, novelty effects, or small-sample noise. Also, "give it time" only holds if the budget can produce enough events. On a small budget with a deep-funnel event like paid subscription, learning may never finish.


*Test with your own data:* Run one campaign for 7 days with no edits, optimizing for StartTrial. Compare daily cost per trial for days 1–3 against days 4–7. Check whether Ads Manager shows 'Learning' or 'Learning limited'. If cost per trial stabilizes after about 50 events, waiting is justified.


- Official source: [https://www.facebook.com/business/help/112167992830700/](https://www.facebook.com/business/help/112167992830700/) — “”

- [Meta Andromeda Güncellemesi: Kampanya Yapınız YANLIŞ!](https://youtu.be/cSlGkDYU_tg?t=1077) @17:57 · Burak Mermi · 2026-02-16 · *supports* · basis: general knowledge · conflict of interest: sells a course
  > We need to give the algorithm a chance during the learning phase.

### <a id="k386"></a>K386 · unverifiable · confidence 0.55

Before running Meta app install campaigns, a mobile subscription app should have at least about $3 of LTV per install.


*Assessment:* This is a single-source rule of thumb from an agency and course seller. The speaker gives no data and no derivation, and the claim is general knowledge. Meta's docs define cost per install and describe value optimization, but they set no LTV-per-install threshold. A sensible threshold depends on your CPI, margin and payback window, and B2B subscription apps with high price points may need a very different number.


*Test with your own data:* Take your last 60–90 days of installs and compute realized LTV per install, using revenue per cohort including trial-to-paid conversion and retention. Compare it with your Meta cost per install. Run a small test campaign for 7–14 days and check that CPI is below LTV per install with your target payback. The success metric is payback within your accepted window, not the $3 figure.


- Official source: [https://www.facebook.com/business/help/335457916629140](https://www.facebook.com/business/help/335457916629140) — “”

- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=384) @6:24 · App Masters · 2026-10-20 · *supports* · basis: general knowledge · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > we're going to stick with at least a $3 LTV per install

### <a id="k389"></a>K389 · unverifiable · confidence 0.54

For free-trial or credit-card app funnels, typical cost per acquisition is around $10–15 (about $20 for a paid subscription).


*Assessment:* This is a single source: an agency owner citing verbal numbers with no screen-shown data. The speaker sells agency services, and the video has a moderate clickbait score. Meta's official documentation gives no CPA benchmarks for trials. CPAs vary widely by country, product price, and creative, so the range is plausible but can't be verified or applied to a different account.


*Test with your own data:* Run your Advantage+ app campaign optimized for StartTrial for at least 7 days with enough budget for about 50 trials. Compare your cost per trial with the $10–15 range, then compute CAC as spend divided by paying customers after the trial ends.


- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=1397) @23:17 · Lorenzo Pravatà · 2025-12-17 · *supports* · basis: client data · conflict of interest: sells agency services
  > we can see CPAs also $10, $15. For example, for a free trial or credit card.

### <a id="k390"></a>K390 · unverifiable · confidence 0.60

Over a 12-month period the speaker's subscription app had $283,000 in sales against about $112,000 of combined Facebook ($31k) and TikTok ($81k) ad spend; sales are gross, before Apple's 15% cut.


- [the meta ads strategy that made my app $283,273](https://youtu.be/04l69IvsW98?t=0) @0:00 · Steven Cravotta · 2026-07-30 · *—* · basis: own experience · conflict of interest: sells a course
  > this one mobile app did $283,000 in sales. And in that same period, we spent $31,000 on Facebook ads and $81,000 on TikTok ads.

### <a id="k391"></a>K391 · single source · confidence 0.63

Ads that push cheap trial starts with click-bait angles can produce a large drop in trial-to-paid conversion, so trial-to-paid should be checked per ad.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1354) @22:34 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > So we'll see a huge drop in trial to pay

### <a id="k396"></a>K396 · single source · confidence 0.55

A quiz-based funnel never worked properly for this app's ads.


- [How I Scaled An App To $4M/Year With Meta Ads (Step by step)](https://youtu.be/2WIiNEdsI60?t=1167) @19:27 · Aazar Shad · 2026-04-02 · *—* · basis: own experience · conflict of interest: sells agency services
  > Quiz has never worked properly for us

### <a id="k402"></a>K402 · unverifiable · confidence 0.41

Meta's ad delivery algorithm is inherently biased toward static ads over video ads (because it can show more statics per session).


*Assessment:* The claim comes from a single creator who sells agency services, with no data shown and no documentation. Commenters with first-hand experience say video beat static, including one who converted the same statics to video and saw better results on every metric. Meta's official pages say nothing about a static bias. Third-party blogs conflict: some say Meta favors video or Reels, others say static has lower CPMs. Results likely depend on placement, objective and creative quality, not on a fixed algorithmic bias.


*Test with your own data:* Run the same creative as a static and as a video in separate ad sets of one Advantage+ app campaign with equal budgets. Run it for at least 7 days, or until each has about 50 trial starts. Compare cost per StartTrial and cost per paying customer, not CPM or CTR.


- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=74) @1:14 · Sabri Suby · 2026-06-12 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > their algorithm is actually has a bias towards static ads

### <a id="k405"></a>K405 · doubtful · confidence 0.06

Meta's PLTV (predicted lifetime value) feature survives iOS App Tracking Transparency because the data is sent through the Conversions API, including for app purchase/subscription campaigns.


*Assessment:* The speaker (an agency-affiliated source) gives this as general knowledge with no evidence. Meta's current pLTV guide says it requires a web Conversions API integration and does not support app events, so the claim is not accurate for an app promotion campaign. Server-side sending can reduce reliance on device-level tracking, but the docs don't say pLTV "survives ATT", and the claim may rest on an earlier or different rollout.


*Test with your own data:* Open your Events Manager and ads setup for the app. Check whether a predicted-value option is available for your app dataset. If it isn't, run an ad set optimized for purchase or subscribe events with values for 2 to 4 weeks. Compare the cost per paying customer with your StartTrial-optimized ad set.


- Official source: [https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value](https://developers.facebook.com/documentation/ads-commerce/conversions-api/guides/predicted-lifetime-value) — “pLTV does not support app events at this time.”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=1487) @24:47 · RevenueCat · 2026-09-12 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > the cool thing about this new pltb logic is that it survives the att on ios

### <a id="k408"></a>K408 · single source · confidence 0.73

In App Store Connect, free-trial starts are found under Analytics > Metrics > Subscriptions > Events > Offer starts, filtered to free trials.


- [Before You Spend $1 on Meta Ads, Watch This](https://youtu.be/2jH64ziB7uM?t=694) @11:34 · App Masters · 2026-10-20 · *—* · basis: own experience · conflict of interest: sells agency services, sells a course, sponsored, affiliate
  > So under subscriptions, events, and then offer starts.

### <a id="k416"></a>K416 · single source · confidence 0.70

Hook rate is the share of people who saw the video ad and watched its first 2–3 seconds (about 3-second plays divided by impressions).


*Assessment:* Hook rate is not an official Meta metric. It is an industry convention, usually 3-second plays divided by impressions. Meta's docs define 3-second plays but not hook rate or its formula. The single source is a course seller who restates the common definition and shows the 65% figure from an e-commerce account in Turkey. The definition is fine, but the 65% is only an example and not a benchmark. The creator's "2–3 seconds" is looser than Meta's 3-second play (or 97% of the video if it's shorter than 3 seconds), and the denominator may be impressions or reach.


- Official source: [https://en-gb.facebook.com/business/help/743427195703387](https://en-gb.facebook.com/business/help/743427195703387) — “”

- [Sıfırdan Reklam Eğitimi: Başa Baş Noktası, Kreatif ve Canlı Sonuçlar](https://youtu.be/AQVJnAho5Nc?t=1606) @26:46 · Gürkanzone · 2026-08-15 · *supports* · basis: platform docs · conflict of interest: sells a course
  > Gören insanların %65'i videonun ilk 2-3 saniyesini izledi.

### <a id="k418"></a>K418 · unverifiable · confidence 0.53

Apps should aim for a customer lifetime value of about $100 or more so they can afford higher Meta CPAs and scale.


*Assessment:* This is a single-source rule of thumb from an agency owner, based on general knowledge with no data shown. Meta's docs describe ROAS and bid strategies for app campaigns but give no LTV threshold. The right LTV depends on margin, payback period and the trial-to-paid rate. For a B2B subscription, $100 may be low or high, so treat the figure as a rough heuristic.


*Test with your own data:* Calculate your own break-even CPA from trial-to-paid rate × average gross-margin LTV. Then run the campaign for 2 weeks with a cost cap near that CPA. Success is cost per paying customer below LTV divided by your target LTV:CAC ratio (for example 3).


- Official source: [https://developers.facebook.com/docs/app-ads/advantage-app-campaigns](https://developers.facebook.com/docs/app-ads/advantage-app-campaigns) — “”

- [How I Scaled An App To $3M/Month With Meta Ads (Step by step)](https://youtu.be/Re7wQSHK8mU?t=1397) @23:17 · Lorenzo Pravatà · 2025-12-17 · *supports* · basis: general knowledge · conflict of interest: sells agency services
  > So you should have a light on value of $100 or more.

### <a id="k421"></a>K421 · unverifiable · confidence 0.55

Some B2B SaaS companies reportedly scale to $2 million a month using Meta as their primary channel while spending over $200K a month (unnamed clients, no data shown).


- [How This B2B SaaS Scaled to $2M/Month Using Meta Ads (Full Breakdown)](https://youtu.be/feR7eaNNq8g?t=0) @0:00 · Lorenzo Pravatà · 2026-03-26 · *—* · basis: client data · conflict of interest: sells agency services
  > These B2B SaaS scale to $2 million a month using Meta as their primary channel

### <a id="k428"></a>K428 · well supported · confidence 0.92

Meta app promotion campaigns can optimize for app installs and also for in-app events such as in-app purchases.


*Assessment:* The claim is a basic platform mechanic, and Meta's developer docs confirm that app ads can be delivered to people likely to purchase in the app. The creator's basis is general knowledge, and he sells courses and agency services. That matters little here because the claim is verifiable in the docs. The one comment only says the viewer didn't know the option existed, so it adds no independent evidence.


- Official source: [https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad](https://developers.facebook.com/docs/app-ads/optimizing-your-app-ad) — “Ads will be delivered to people most likely to take actions such as purchasing products in your app after app install”

- [The BEST Facebook Ads Tutorial For Beginners in 2026](https://youtu.be/dAJyqo6wnq4?t=742) @12:22 · Ben Heath · 2026-01-06 · *supports* · basis: general knowledge · conflict of interest: sells a course, sells agency services, paid community
  > You can use app promotion not just for getting more people to install your app, but also for trying to sell in-app events

### <a id="k435"></a>K435 · unverifiable · confidence 0.56

Cost per install for the campaign was about $0.87 in the last month, according to the creator, which conflicts with the roughly $2 CPI quoted earlier.


- [How I Got 1.2K App Installs for This iOS App With $500](https://youtu.be/81oWUwreWtk?t=838) @13:58 · Gui Costa · 2026-07-25 · *—* · basis: own experience · conflict of interest: sells agency services
  > last month was about $0.87 per dollar right?

### <a id="k437"></a>K437 · unverifiable · confidence 0.56

For the same client, Meta app install campaigns produced a cost per install of about 2.38.


- [How I Scaled This App to 25K+ Downloads With Meta and Google Ads](https://youtu.be/gjLLdIrkS54?t=791) @13:11 · Gui Costa · 2026-07-28 · *—* · basis: own experience · conflict of interest: sells agency services
  > 1.93 on Google, 2.38 CPI on Meta.

### <a id="k445"></a>K445 · well supported · confidence 0.90

Putting several winning creatives into one CBO campaign lets Meta's algorithm shift spend toward the creatives that get the best results.


*Assessment:* The docs confirm that CBO distributes budget in real time across ad sets toward the best opportunities for results. They describe allocation across ad sets, not across individual creatives. Spend shifting between creatives inside one ad set is a related but separate mechanism, and Meta's optimization favors early leaders, so it is not always the creative that would convert best. The speaker sells agency services and cites no data. The claim is plausible but loosely worded.


- Official source: [https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget](https://developers.facebook.com/docs/marketing-api/bidding/guides/advantage-campaign-budget) — “Facebook automatically and continuously finds the best available opportunities for results across your ad sets”

- [Learn 97% of Meta Ads in Under 19 minutes](https://youtu.be/NTmWqnPIb2s?t=371) @6:11 · Sabri Suby · 2026-06-12 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > you chuck them in a CBO, you let Facebook's AI do its thing and it's going to basically pivot the spend

### <a id="k458"></a>K458 · well supported · confidence 0.93

Meta Ads Manager can show fewer events than Events Manager, so compare the two to check that the data makes sense before trusting either.


*Assessment:* Meta has an official help article titled "Differences between event counts in Meta Ads Manager, Ads Reporting and Events Manager". Search summaries of it say Ads Manager counts only deduplicated events that Meta can attribute to ads, while Events Manager counts all received events. I could only fetch the page title, not the body, so no verbatim quote is given. The member's explanation ("sometimes Meta doesn't show all the data") is vague, but the advice to cross-check is sound. The creator sells agency services, which matters little for this mechanical claim.


- Official source: [https://www.facebook.com/business/help/337196340694086](https://www.facebook.com/business/help/337196340694086) — “”

- [How to scale Meta ads for subscription apps [Shipaton 26]](https://youtu.be/IAiTKh-FtF0?t=2187) @36:27 · RevenueCat · 2026-09-12 · *supports* · basis: own experience · conflict of interest: sells agency services
  > sometimes meta is not going to show all the data so just make sure that the data between the ads manager and events manager actually makes sense

### <a id="k468"></a>K468 · single source · confidence 0.63

In a head-to-head test, sending traffic to a long personalised web quiz converted better than sending the same traffic straight to the App Store listing.


- [Why 90% of their paid traffic goes to a quiz, not the App Store](https://youtu.be/EyoYQU6JyV8?t=1513) @25:13 · Sub Club by RevenueCat · 2026-09-02 · *—* · basis: own experience
  > we've noticed that the quiz just has a much higher conversion

### <a id="k473"></a>K473 · unverifiable · confidence 0.52

A typical IPM (installs per 1,000 impressions) for a US install campaign with a broad audience is roughly 5 to 50.


*Assessment:* The only source is a single agency-affiliated speaker offering general knowledge with no data. The range of 5 to 50 is so wide it is nearly meaningless, and it conflicts with the 10 to 15 readiness threshold the same passage gives. Meta's docs publish no IPM benchmarks, and third-party sources say IPM varies heavily by category, platform and geography. Gaming averages around 8 to 9 (Adjust-sourced summary), which sits inside the range but does not confirm it for a B2B subscription app.


*Test with your own data:* Run your Advantage+ app campaign for 7 days with at least 50,000 impressions. Compute IPM from Ads Manager as installs divided by impressions times 1,000. Use your own result as the baseline and compare creatives against it. Track cost per trial as the success metric, because IPM is only a proxy.


- [LTV mastery: Getting high-value subscribers from Meta](https://youtu.be/kXXFtl0ocU0?t=774) @12:54 · App Leaders by Adapty · 2025-12-26 · *qualifies* · basis: general knowledge · conflict of interest: sells agency services
  > that should be around five to 50 for a US install campaign in a broad audience