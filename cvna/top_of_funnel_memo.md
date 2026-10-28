# CVNA: top-of-funnel thesis test (Amazon Autos + LLM migration)

As of 2026-10-28, pre-Q3'26 print (Carvana reports after close today). Latest hard data is Q2'26.
Labels: **[D]** = sourced data, **[I]** = our inference. Full ad-spend table: `cvna_kmx_advertising.csv`.

## The thesis as drafted (Tab 2)

> Top-of-funnel competition from entrants like Amazon Autos, combined with user migration from Google search to LLMs (seemingly less favorable to CVNA than to CarMax and local dealers), means CVNA must grow advertising at or above revenue growth, limiting operating leverage.

## Bottom line

| Sub-claim | Verdict | Key evidence |
|---|---|---|
| Carvana is "not materially better service, just early" vs Amazon Autos | **Mostly false.** True only on post-sale CX | Amazon Autos is a dealer marketplace: pickup only, 75-mi radius, dealer recons/delivers. Carvana ~$3.4k op. profit/retail unit vs CarMax ~$1.0k pre-tax. Vroom/Shift died copying the front end; Driveway and CarGurus' CarOffer retreated |
| LLMs route away from CVNA ("Gemini doesn't route to CVNA") | **Not supported** for ChatGPT Search / Google AI Mode; untested for standalone Gemini app | Parse: CVNA overall AI-answer share 7% = CarMax 7%; best avg. position (2.9 vs CarMax 3.6); AI Mode 9% > ChatGPT 5%; on the used-car-financing topic CVNA leads CarMax (26% vs 20%). Real negative: rated worse on price in 96% of AI price comparisons (CarMax 82%) |
| CVNA buys subprime / bad-credit keywords | **Plausible, unverified** | Sole source is one ex-marketing head quoted by Hindenburg (Jan-25). No public keyword/ad-copy data confirms or refutes |
| Ad spend must grow ≥ revenue, limiting op. leverage | **Supported on a per-unit basis, but not yet caused by LLMs/Amazon** | Ad $/unit up YoY 5 straight quarters ($515 Q3'24 → $613–654); marginal ad $ per incremental unit ~$743 (2025), ~$772 (H1'26). Mgmt attributes it to brand campaigns |

**Better version of the thesis [I]:** Carvana's top-of-funnel advantage today is *bought* on Google. It holds ~53% of paid clicks among online car retailers vs CarMax at ~2%. In LLM answers it can't buy that position; it sits at parity with CarMax (~7% each) and is weak on bad-credit and price prompts. Each shopper who moves from Google to an LLM moves from a channel where CVNA dominates by spend to one where it is merely equal and is framed as the pricier option. That is a Carvana-specific headwind even though LLMs don't "route away" from Carvana. Caveat: much of the Google "dominance" is brand defense (paying for clicks on people already searching "carvana"), so the at-risk piece is the non-brand, conquest and generic traffic. Amazon is the same story on a different surface: it captures *shopping intent*, not fulfillment.

---

## 1. Amazon Autos: is Carvana "just early"?

**What Amazon Autos is [D]** ([aboutamazon.com](https://www.aboutamazon.com/news/retail/how-to-buy-a-car-with-amazon-autos)):
- A marketplace, not a retailer ("isn't a direct-to-consumer car store").
- Dealers own the inventory, recondition it, do the paperwork and hand over the car. There is no home delivery; pickup is typically within 3 days.
- Search radius is 75 miles. Amazon charges dealers no fees.
- Used/CPO cars carry a ≥3-day/300-mi return (Ford CPO: 14-day).
- Timeline:
  - Hyundai new cars, Nov-24; Hyundai used/CPO, 2025.
  - Hertz Car Sales, Aug-25 ([BusinessWire](https://www.businesswire.com/news/home/20250820673392/en)).
  - Chase/Santander/Wells lenders, Oct-25.
  - Ford Blue Advantage CPO, Nov-25 ([Inquirer](https://www.inquirer.com/business/ford-used-cars-amazon-online-shoppers-buy-certified-20251118.html)).
  - 1,000+ dealers in 130+ cities in 2026; Prime $1,500 gift-card promo, Sep–Oct 2026.
- Footprint is scaling fast: 130+ cities, up from 48 ([WSJ via PYMNTS, Apr-26](https://www.pymnts.com/amazon/2026/amazon-autos-ramps-up-focus-on-new-car-sales/)). "Pickup only" fits all current coverage, but one early Bloomberg piece on the Hyundai launch mentioned home delivery, so treat it as likely, not proven.
- Traction is thin and undisclosed. One CA Kia dealer sold 1 car in 6 weeks ([PYMNTS/WSJ, Apr-26](https://www.pymnts.com/amazon/2026/amazon-autos-ramps-up-focus-on-new-car-sales/)).
- Hyundai says >10 shoppers research on Amazon for every 1 who buys there ([MediaPost, Sep-26](https://www.mediapost.com/publications/article/418026/hyundai-amazon-release-details-of-shopping-engage.html?edition=143859)). So Amazon is a **research/ad funnel**, not a transaction engine yet.
- Amazon–Carvana partnership: only an unsourced Substack rumor.

**Head-to-head [D unless marked]**

| | Carvana Q2'26 | CarMax FQ2'27 (to 8/31/26) | Amazon Autos |
|---|---|---|---|
| Retail units | 197,325 (+38% YoY) | 227,391 (+13.8%, off a −9% comp; driven by GPU cuts plus FTC pricing enforcement on rivals per mgmt) | not disclosed |
| Retail GPU | $3,547 | $2,105 | dealer's margin |
| Total GP / retail unit | $7,014 (incl. ADESA wholesale + loan sales) | ~$4,112 incl. CAF [I] | none (no fee) |
| SG&A / retail unit | $3,568 GAAP | ~$2,764 [I] | borne by dealer |
| Op. profit / retail unit | ~$3,446 [I] | ~$981 pre-tax [I] | n/a |
| Footprint | 19 ADESA-integrated recon sites (~1.5M/yr capacity), no retail lots | 255+ stores | dealer lots |
| Fulfilment | home delivery, same-day in 20+ states | store or delivery | dealer pickup ~3 days |
| % sales fully online | ~100% | 13% (68% omni) | n/a |
| Price vs market (iSeeCars) | +3.9% | +4.2% | dealer-set |

**Copycat graveyard [D]:**
- Vroom shut e-commerce in Jan-24.
- Shift went Ch. 11 in Oct-23.
- Lithia Driveway cut its burn and never reached its $9B target.
- CarGurus wound down CarOffer at end-2025.

The pattern [I]: copying the front end without owning recon, logistics and finance fails.

**Where "not materially better" has teeth [D]:**
- Post-sale experience is weak. A study of 5,380 reviews (Jan-24 to Jun-26) averages 2.83/5: ~15% of shopping-stage reviews are unhappy vs ~90% of ownership-stage reviews. Top complaints are mechanical defects, unreachable support, and title/registration problems ([Dimension Labs](https://assets.dimensionlabs.io/carvana-report)).
- A local dealer with a service bay competes exactly there.
- In LLM answers, Carvana is framed as *worse on price* in 96% of pricing comparisons (Parse).

**Sell-side framing [D]:** BofA, Citizens JMP and William Blair all treat Amazon like CarGurus/TrueCar (lead gen) with any CVNA impact pushed out. Carvana grew units +38–40% in H1'26 while the industry was flat, so there's no evidence of share loss yet.

**Verdict [I]:**
- The listing/search/prequal layer is a commodity, and Amazon (traffic plus Prime trust) can win it.
- Recon, logistics, ADESA and in-house finance are not a commodity. Amazon has none of them, and its CX is capped by the weakest dealer.
- Amazon's real damage path is CAC inflation and price transparency, not stealing transactions.
- **What would change this:** Amazon adding owned or exclusive delivery, a CarMax or large dealer-group fulfilment partnership, or 7-day returns as standard.

## 2. LLMs: do they route away from Carvana?

**AI-answer share: Parse [D]**
- Coverage: ChatGPT Search and Google AI Mode, Jul 5 – Oct 25, 2026, n = 3,949 responses ([parse.gl/brands/carvana](https://www.parse.gl/brands/carvana)).

| Brand | Mention rate (online vehicle marketplace prompts) | Avg. position | Overall share (ChatGPT / AI Mode) |
|---|---|---|---|
| Autotrader | 38% | 5.3 | – |
| Cars.com | 37% | 5.8 | – |
| CarGurus | 33% | 4.8 | – |
| CarMax | 33% | 3.6 | 7% (5% / 9%) |
| **Carvana** | **32%** | **2.9 (best)** | **7% (5% / 9%)** |
| Edmunds | 25% | 6.4 | – |

By prompt type, Carvana is mentioned in:

| Prompt type | Carvana mention rate |
|---|---|
| "Best online car buying sites" | 95% |
| Instant selling | #1 (68%) |
| "Bad credit car loans" | **18%** |
| "Where can I get a used car loan" | 22% |
| Auto financing category share | **3%** (vs KBB 32%, Edmunds 28%) |

**Reads [I]:**
- The "Gemini doesn't route to CVNA" anecdote is contradicted for **Google AI Mode** (Gemini-powered, the highest-volume Gemini surface), where Carvana does *better* than in ChatGPT.
- Neither the standalone Gemini app nor Perplexity is measured. That anecdote is the one thing to test by hand: run the bad-credit prompts below in Gemini.
- **Financing/bad-credit intent** is a weak spot for *all* retailers, not specifically Carvana. LLMs answer those queries with advice content (CFPB, Consumer Reports, NerdWallet, Reddit, Edmunds), not retailers. That is exactly the segment Hindenburg's source says Carvana buys on Google, so Carvana loses a channel it can buy without losing ground to CarMax.
- The 18% bad-credit figure comes from a single prompt with an undisclosed sample. Parse says its counts are "not weighted estimates of demand." Treat it as anecdotal.
- **Price perception is the clearer CVNA-specific negative:** rated worse than a rival in 96% of AI price comparisons, vs 82% for CarMax. In an LLM-mediated funnel, the summarized "is it overpriced?" judgment replaces the ad.

**Deals and integrations [D]:**
- **CarMax has a ChatGPT app** (since 2026-02-27; 45k vehicles plus trade-in quotes) ([press release](https://media.carmax.com/press-releases/news-release/2026/CarMax-Launches-First-of-Its-Kind-Car-Shopping-and-Selling-Experience-in-ChatGPT-App-Store/default.aspx)).
- CarMax ran **ChatGPT text ads** on used-car prompts, Jul–Sep 2026 ([sprites.ai](https://www.sprites.ai/chatgpt-ads-library/industry/used-car-marketplaces)).
- CarGurus, Cars.com, Autotrader, Edmunds, KBB and CARFAX are also in the ChatGPT app directory.
- **Carvana has no ChatGPT app.** It also has no OpenAI Agentic Commerce, Google UCP, Perplexity or Copilot integration found.
- Carvana's AI is inward-facing: the Sebastian assistant, Shaqbot (Sep-25), and >30% of buyers / 60% of sellers completing with no human touch.
- Management has not discussed AI search or LLM traffic on calls.
- The 10-K risk factor names "AI tools" alongside search engines as traffic sources competitors can outbid on.
- Google is building auto ad slots *inside* AI Mode: vehicle feeds in Search ads (Mar-26), vehicle ads in Shopping (May-26), and local inventory inside Gemini-generated lists. **[I]** Paid placement may follow shoppers into AI answers, which would help the biggest bidder (Carvana).
- Morgan Stanley (Daniela Haigian, 2026-09-28 note, reported by TheStreet on 2026-09-30): Carvana "screens as the best-positioned auto retailer in their framework, with franchise dealers facing more pressure if AI agents take a larger role in vehicle shopping." It puts CarMax GPU ~$740 below Carvana's and franchise dealers ~$1,106 below ([Yahoo/TheStreet](https://finance.yahoo.com/technology/ai/articles/carvana-carmax-jockey-agentic-ai-013700290.html)). Note that separate MS agentic-commerce work argues AI agents *raise* paid-traffic costs, which cuts toward our thesis.

**Size of the channel today [D]:**
- ChatGPT is ~0.06% of carvana.com visits (Semrush, Sep-26).
- AI referrals to franchise dealer sites grew 15x YoY but remain a small slice; ChatGPT is ~89% of AI referrals and Gemini rose from 1.5% to 8.5% (Fullpath, Feb/May-26).
- 19% of 2025 car buyers used AI tools; 63% plan to next time (Cox).

## 3. Quantifying bought Google position vs LLM position

| Surface | Carvana | CarMax | Source |
|---|---|---|---|
| Google paid click share, US online car retailers, Sep-26 | **52.8%** (20.8% Mar-25 → 26.6% Jan-26 → 52.8%) | 1.7% | [Adthena](https://www.adthena.com/market-share/us-automotive-online) [D] |
| Google paid spend share, Sep-26 | 35–45% (peak 52.6%) | 5–6% | Adthena [D] |
| AI-answer share (ChatGPT Search + AI Mode) | 7% | 7% | Parse [D] |
| google.com share of site referrals | ~11% (2022) → 26–30% (2025–26) | 20% | Semrush [D] |
| Brand search volume, Sep-26 | "carvana" 3.35M/mo | "carmax" 3.35M/mo | Semrush [D] |
| Brand term as % of organic traffic | 51.5% | 1.2% | Semrush [D] |
| Ad $ / retail unit (FY25 / FY26) | **$608** | **$363** | 10-Ks [D] |

**Caveats:**
- Adthena and Parse measure different keyword/prompt universes, so the 53% vs 7% gap is directional, not like-for-like.
- Semrush's estimate of carvana.com paid traffic (~44K/mo) is implausibly low next to Adthena; it appears to miss Shopping/vehicle-listing ads.
- Similarweb (Sep-26) puts paid search at 41.1% of carvana.com traffic (#1 channel), while carmax.com is led by direct at 36.3%. Both are **desktop-only**, and Similarweb counts brand-ad clicks as paid. So the 41% is largely Carvana paying to defend navigational "carvana" searches, a cost line rather than a dependence on finding new demand. LLMs bypass the SERP and with it both the brand ad and the organic listing.

**Operating-leverage test [D, from 10-Ks and letters]:**

| | Ad $/unit | Note |
|---|---|---|
| 2017–2022 | ~$1,130–1,260 | flat; "leverage" in % of revenue came only from rising ASPs |
| 2023 | $729 | cut spend in the restructuring |
| 2024 | $550 (trough $515 in Q3'24) | conversion up: units per 1k MUV 19 (2022) → 32 (2025) |
| 2025 | $608 | new brand campaign from Q3'25 |
| Q1'26 / Q2'26 | $630 / $613 | +$92 / +$27 YoY |
| Marginal: incremental ad $ ÷ incremental units | ~$743 (2025), ~$772 (H1'26) | above the average, so growth is being bought |

- Ad as % of revenue is flat at 1.6–1.9%, but revenue per unit is inflated in 2026 by gross-revenue treatment of marketplace-partner vehicles. **Use $/unit.**
- **Management's counter:** mature 2013–16 cohorts run ~1.0% of revenue on advertising vs 1.8% company-wide, and getting there is one of two levers to the 13.5% EBITDA-margin target. At ~$37k revenue per unit, 1.0% ≈ $375/unit vs $613 today, a ~$240/unit (~0.65 pt margin) bridge item.
- **Thesis framing [I]:** if LLM/Amazon migration keeps ad $/unit ≥ $600 while unit growth decelerates, ~0.6 pt of the 13.5% margin target is at risk.
- **Magnitude check [I]:** advertising is ~$600/unit vs ~$3.4k op. profit/unit. Even +25% CAC is ~$150/unit (~4% of op. profit/unit). This is a margin-bridge issue, not a thesis-breaker on its own.

**Illustrative sensitivity [I]: how much can LLM migration raise CAC?**
- Model: ad $/unit = $613 × (1 + f × m × (k − 1)).
  - f = search share of the ad budget (not disclosed; Carvana also runs TV and brand).
  - m = share of search-originated shoppers who move to LLMs.
  - k = cost to re-acquire them elsewhere, as a multiple of today's cost.
- Margin impact is measured against ~$37k revenue per unit. Full grid: `sensitivity.md`.

| Case | f | m | k | Ad $/unit | Δ EBITDA margin |
|---|---|---|---|---|---|
| Mild | 35% | 10% | 1.5x | $624 | −0.03 pt |
| Mid | 50% | 25% | 1.5x | $651 | −0.10 pt |
| Severe | 65% | 40% | 2.0x | $772 | −0.43 pt |

- **Read:** even the severe case costs < 0.5 pt of margin.
- The bigger exposure is the **opportunity cost**: management's 13.5% target assumes advertising falls toward ~1.0% of revenue (~$375/unit), about +0.65 pt.
- If LLM/Amazon pressure just keeps ad $/unit flat at ~$600+, that 0.65 pt never arrives. Combined with the severe case, roughly 1 pt of the 13.5% target is at risk.
- That ~1 pt is the honest size of this thesis. It is a real but second-order lever next to GPU and credit; frame it as part of a GPU/credit short, not the core.

## 4. Subprime keyword claim

- **Source [D]:** [Hindenburg (2025-01-02)](https://hindenburgresearch.com/carvana/), quoting one former marketing head. "Low credit / bad credit auto loan" SEM was "one of the most expensive but highest ROI areas," and "behind the scenes they are doing a lot to push that market."
- **Not verified:**
  - No keyword lists or screenshots.
  - The VIC writeup body is an image; we could not read it, so someone should screenshot it.
  - SpyFu and Google Ads Transparency Center were not machine-accessible. Check by hand: adstransparency.google.com → "Carvana" → text ads.
- **Credit mix [D]:**
  - Non-prime ABS pools (N-shelf): WA FICO 567–589.
  - 2025-N1: 58% of the pool at FICO ≤600 or no score; WA APR 22%; LTV 100.6%; DBRS expected CNL 15.9%.
  - Hindenburg estimates ~44% of securitized loans are non-prime.
  - CarMax CAF's own Tier 2/3 is <5% of units; 3rd-party Tier 2/3 lenders take ~23.5%.
- **Sizing [I]:**
  - ~80% of Carvana buyers finance in-house, and ~40–50% of that is non-prime, so roughly 30–40% of units involve non-prime credit.
  - But most demand is navigational ("carvana" ≈ half of organic traffic). Generic bad-credit search is probably ~2–6% of units.
  - That slice is over-weighted in high-gain-on-sale loans, so the profit at risk is larger than the unit share.

## 5. Red-team: weakest points in our own argument

1. **Parse shows Carvana and CarMax as a wash** (same 7% / 5% / 9%, from one pooled 3,949-response set). If CarMax's ChatGPT app mattered, CarMax would lead on ChatGPT; it doesn't. "No ChatGPT app" is a watch item, not evidence.
   - *Would change this:* CarMax's ChatGPT share pulling ahead in Parse's time series after Feb-26, or CarMax disclosing leads attributed to the app.
2. **"Paid-search dependence" is partly a Similarweb classification artifact.** Brand navigational clicks are counted as paid.
   - *Would change this:* a brand vs non-brand split of the paid keywords, and **ad $/unit rising while retail GPU falls**. Q2'26 already showed that combination: ad $/unit $613 vs $586, GAAP retail GPU −2.4% YoY.
3. **"Amazon is not a threat" describes today's product, not a structural limit.** Pickup-only and the 75-mile radius are choices Amazon can change. It added a fleet seller (Hertz) and OEM CPO (Ford) within a year, and CarMax's rebound shows price perception moves share.
   - *Would change this:* Carvana's unit growth or monthly unique visitors (MUV) slowing in the Amazon launch metros (LA, Seattle, Dallas, Houston) relative to other markets; MUV growing slower than units; Amazon adding delivery or its own financing.

## 6. Open items / what would move us

1. **Q3'26 tonight:** ad $/unit vs $654 (Q3'25). Management guided ad $ up. Above ~$650 with decelerating units supports the thesis; flat or down undercuts it.
2. Test the standalone Gemini app and Perplexity by hand on these prompts:
   - "I have bad credit, where can I buy a used car"
   - "best place to buy a used car online"
   - "Carvana vs CarMax"
3. Watch for a Carvana ChatGPT app or Google AI Mode vehicle-ads adoption. Either would show Carvana can buy or build its way into LLM surfaces.
4. Paywalled data worth buying or borrowing: EMARKETER AI Visibility Index, Automotive, Q4-26; Similarweb paid-channel split; SpyFu keyword list (filter "credit|loan|finance").
5. Amazon: any delivery capability, a CarMax or big-dealer fulfilment deal, disclosed volumes.

## Sources

- **Carvana:**
  - [Q2'26 letter (8-K, 2026-07-29)](https://www.sec.gov/Archives/edgar/data/0001690820/000169082026000054/ex99_1q22026.htm)
  - [Q1'26 letter](https://www.sec.gov/Archives/edgar/data/0001690820/000169082026000034/ex99_1q12026.htm)
  - [Q4'25 letter](https://investors.carvana.com/~/media/Files/C/Carvana-IR/documents/cvna-shareholder-letter-q4-2025.pdf)
  - [Q2'26 10-Q](https://www.sec.gov/Archives/edgar/data/0001690820/000169082026000055/cvna-20260630.htm)
  - 10-Ks FY17–FY25 (EDGAR XBRL `AdvertisingExpense`, CIK 1690820)
- **CarMax:**
  - [FQ2'27 release (2026-09-29)](https://www.sec.gov/Archives/edgar/data/0001170010/000117001026000102/q2fy27earningsrelease.htm)
  - Q4 releases FY18–FY26
- **Amazon:**
  - [aboutamazon.com](https://www.aboutamazon.com/news/retail/how-to-buy-a-car-with-amazon-autos)
  - [Hertz](https://www.businesswire.com/news/home/20250820673392/en)
  - [Ford CPO](https://www.inquirer.com/business/ford-used-cars-amazon-online-shoppers-buy-certified-20251118.html)
  - [PYMNTS/WSJ](https://www.pymnts.com/amazon/2026/amazon-autos-ramps-up-focus-on-new-car-sales/)
  - [CBT News](https://www.cbtnews.com/international-expansion-of-amazon-autos-2027/)
  - [BofA](https://www.tipranks.com/news/the-fly/bofa-sees-any-impact-on-carvana-sales-from-amazon-autos-as-likely-pushed-out-thefly)
  - [Citizens JMP](https://www.tipranks.com/news/the-fly/citizens-jmp-says-amazon-autos-not-threat-to-carvana-cargurus-thefly)
- **AI search:**
  - [Parse Carvana](https://www.parse.gl/brands/carvana)
  - [Parse CarMax](https://www.parse.gl/brands/carmax)
  - [Parse auto financing ranking](https://www.parse.gl/rankings/consumer-reviews/auto-buying-financing-services)
  - [ChatGPT apps index (3rd-party)](https://github.com/rdmgator12/awesome-chatgpt-apps)
  - [Fullpath Feb-26](https://www.fullpath.com/wp-content/uploads/2026/02/Fullpaths-Auto-Intelligence-Index-February-2026.pdf)
  - [Fullpath May-26](https://www.fullpath.com/wp-content/uploads/2026/05/Fullpath-Auto-Intelligence-Index-May-2026-1.pdf)
  - [Cox Car Buyer Journey](https://www.coxautoinc.com/wp-content/uploads/2026/01/2025-Cox-Automotive-Car-Buyer-Journey-Press-Release.pdf)
  - [Google AI Mode auto ads](https://www.clickheredigital.com/insights/automotive-advertising-in-ai-mode-capturing-conversational-car-shoppers)
- **Search:**
  - [Adthena online car retailers](https://www.adthena.com/market-share/us-automotive-online)
  - [Semrush carvana.com](https://www.semrush.com/website/carvana.com/overview/)
  - [Semrush carmax.com](https://www.semrush.com/website/carmax.com/overview/)
- **Credit:**
  - [Hindenburg](https://hindenburgresearch.com/carvana/)
  - [DBRS 2025-N1](https://dbrs.morningstar.com/research/448343)
  - [KBRA Aug-26 ABS index](https://www.kbra.com/publications/nGfSyykg/u.s.-auto-loan-abs-indices-august-2026)
  - [VIC writeup](https://www.valueinvestorsclub.com/idea/CARVANA_CO/3997733949)
- **CX:**
  - [Dimension Labs review study](https://assets.dimensionlabs.io/carvana-report)
  - [iSeeCars price comparison](https://www.iseecars.com/articles/carmax-vs-carvana)
