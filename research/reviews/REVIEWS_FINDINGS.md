# Customer reviews: what they say, and where they fit in the short

Tags follow THESIS_BRIEF.md: **[F]** filing · **[P]** public records/press · **[B]** Bleecker · **[M]** our analysis · **[V]** verify

## Bottom line
- **"The product is bad" is only half supported.** Riders who write reviews are unhappy. But they are just as unhappy with Spare, the main software rival. The reviews do not show that Via is worse than its competitors, and a bull can point to Via's 4.7-star headline rating. **Don't make this a pillar.**
- **What the reviews do support is the contractor thesis.** Riders mostly complain about capacity: waiting, late pickups, no ride available, cancellations. Only more vehicle-hours fix that, so better service costs the agency more hours. Those hours are billed as services revenue at services margins, and the support and insurance they need sit in G&A.
- **The decisions that set revenue are made by agencies, not riders.** At the agency level the evidence is stronger: downsells, terminations, lost software bids, and an audit of NYC school buses saying Via didn't deliver the routing software it was paid for.

## 1. App-store data (scraped 2026-09-24)
Via publishes a white-label rider app for almost every agency customer, under the developer "Via Transportation, Inc." That makes app reviews a structured, cross-customer dataset.

- **Coverage:** 282 iOS apps and 156 Google Play apps; **6,938 written reviews** (5,825 from riders, 1,113 on the Via Driver app) **[M]**
- **Limits:** the stores only return recent reviews (≤500 per iOS app, ≤1,000 per Play app). Reddit blocks scraping from this environment, so it isn't included.

**Headline stars vs. written reviews (iOS, same method for every group)**

| | Apps | Star ratings | Headline avg | Written reviews | Written avg | 1–2★ share |
|---|---|---|---|---|---|---|
| **Via** agency rider apps | 280 | 52,809 | **4.71** | 1,872 | **2.90** | 50% |
| Spare (rival) | 158 | 5,595 | 4.58 | 312 | 2.92 | 47% |
| RideCo (rival) | 66 | 1,328 | 3.92 | 391 | 3.17 | 44% |
| Uber + Lyft | 2 | 34.6M | 4.91 | 50 | 3.76 | 30% |

- The gap between 4.7 headline stars and 2.9 in written reviews most likely comes from in-app rating prompts after completed trips. Written reviews skew negative in every app store. **[M]**
- **Via ≈ Spare.** The problem belongs to microtransit as a category, not to Via specifically. **[M]**

**By product (Via, both stores, written reviews)**

| Product | Reviews | Avg | 1–2★ |
|---|---|---|---|
| Microtransit | 5,605 | 2.87 | 51% |
| Paratransit | 89 | 3.25 | 39% |
| School (NYC School Bus, Field Trips) | 131 | **1.74** | **82%** |
| Via Driver (driver app) | 1,113 | 2.81 | 51% |

**What riders complain about** (keyword tags; share of 1–2★ reviews vs. share of 4–5★ reviews)

| Topic | 1–2★ | 4–5★ |
|---|---|---|
| Waiting / late / no-show | **34.2%** | 7.7% |
| App bugs / login / crashes | 15.9% | 2.5% |
| Service area / hours cut | 10.4% | 4.6% |
| Payment / fare | 7.4% | 4.1% |
| Cancellations | 6.1% | 0.7% |
| No ride available | 4.3% | 0.5% |
| Driver conduct | 4.2% | 1.1% |

- 14% of negative reviews name a specific wait of 30+ minutes or an hour or more. **[M]**
- Worst Via apps (recent written avg, n≥20 reviews): NYC School Bus 1.21, Calgary 1.66, Durham DRT 1.75, Via Jersey City 2.00, Edmonton 2.24, DCTA GoZone 2.32 (n=355), UTA On Demand 2.37 (n=275), Arlington 2.39 (n=208) **[M]**
- Representative quotes:
  - *UTA On Demand, Apr 2026:* "it takes over an hour to book a ride and then another 30-40 min. for the ride to pick you up. just bring back the bus stops."
  - *Silicon Valley Hopper, Dec 2025:* "The cities … should add more drivers … can't satisfy the needs"
  - *FlexRide Milwaukee, Nov 2023:* "Keeps saying no Cars available. It's like 3 people are driving"
  - *Putnam On-Demand, Nov 2025:* "Recently, there haven't been many rides available, often ending up in me paying for an uber"

**Via Driver app:** 28% of negative reviews mention pay, e.g. "Via make drivers compete for shifts." Most of these reviews are from 2017–2019, when Via ran its own NYC consumer rideshare, so they say little about today's agency drivers. **Weak; don't use.**

## 2. Agency-level evidence (this is what drives revenue)
- **Jersey City:** the Via contract cost more than $8M a year. The mayor told the council he intended to end it. The outcome (Jul 2026) was an "agreement in principle": shorter hours, Saturday service ended, and fee changes **[P]**
- **DCTA GoZone (Denton, TX):** average wait was 25.7 min (Feb 2022). Via quoted **$715K** to bring ETAs to 15–20 min, or **$1.04M** to reach ~15 min, i.e. more vehicle-hours. The board also raised complaints about unsafe driving **[P]**. *This is the clearest case of service quality being bought in hours, not software.*
- **LA Metro Micro:** $32.40 per boarding in FY24 ($24.7M for 763K boardings). Ridership was ~2,300 a day vs. a 5,090 target. Spare took the software (bidding one cent for three years), leaving Via with drivers and vehicles **[P][B]**
- **NYC school buses:** Via holds ~$50M of DOE contracts. The routing software was promised for 2021, then Sept 2025, and is now "pressure testing" for Sept 2026. A comptroller audit found DOE "did not hold Via Transportation accountable for implementing technology it was contracted and paid to do" **[P]**. The rider app averages 1.2★ in recent reviews. *This is the one place where Via's software itself is failing, and it cuts directly against the software label.*
- **Terminations and lost bids:** Baldwin County terminated (services ended Q3'25). One agency ended Via's paratransit software for "inability to meet required functionality" and moved to Ecolane. Via lost paratransit operations to Easton Coaches. Ben Franklin Transit picked RideCo over Via's lower bid **[B]**
- **Arlington, TX:** contract ceiling cut 31% ($30.2M → $20.8M, Dec 2024); fares raised to $3–8 in Mar 2026 **[B][P]**
- **Hampton Roads Transit (Virginia Beach):** HRT OnDemand ended on Jan 10, 2026; the Newport News zone continues **[P]**. The rider app is published by Via **[M]**. Confirm who operated the Virginia Beach zone **[V]**

## 3. Where this fits in THESIS_BRIEF.md
- **Thesis 1 (contractor):** add DCTA as a supporting fact. Wait time is a function of vehicle-hours, so improving service means selling more hours, which is services revenue.
- **Thesis 2 (hour-driven costs):** 16% of negative reviews are app, login or payment problems. Those go to customer support, which the 10-K places in G&A. It's color, not proof that costs scale.
- **Supporting / risk of downsell:** Jersey City, Arlington and HRT show agencies facing budget pressure with unhappy riders. They cut hours and don't churn.
- **Q&A, "Via wins on software":** cite the NYC DOE audit.
- **Don't** claim riders hate Via specifically. Spare scores the same.

## Method and caveats
- Scripts are in `scripts/`. Raw data: `via_app_reviews.csv` (every written review with topic tags) and `via_ios_apps.csv` (every Via iOS app with its headline rating and count).
- The keyword tagging is rough; read the CSV before quoting a number.
- The year-by-year trend isn't reliable because newer, larger apps hit the store caps. It is not shown here.
- The two Reddit threads you found were not re-checked (Reddit is blocked from this environment).

## Sources
- Gothamist, Jersey City: https://gothamist.com/news/jersey-city-weighs-cutting-via-microtransit-service-amid-budget-crisis
- TAPinto, Jersey City: https://www.tapinto.net/towns/jersey-city/sections/government/articles/jersey-city-weighs-cutting-via-service-as-costs-top-8-million-annually
- Jersey City Times, hours cut: https://jcitytimes.com/via-to-cut-hours-and-change-fees-wednesday-as-part-of-citys-plan-to-reduce-budget-deficit/
- Denton Record-Chronicle, GoZone wait times: https://dentonrc.com/news/dcta/improving-gozone-wait-times-could-cost-upward-of-1-million-says-contractor/article_6256b580-6228-5f55-981f-9ede2273ae69.html
- The Basin, Metro Micro cost per boarding: https://basin.la/articles/thirty-two-forty.html
- Chalkbeat, NYC school bus routing: https://www.chalkbeat.org/newyork/2026/05/18/nyc-school-bus-scorecard-vendor-accountability-via-routes/
- NYC Comptroller, school bus audit: https://comptroller.nyc.gov/wp-content/uploads/2025/12/School-Bus-Audit-Policy-Wrap-Report-20251217.pdf
- Bleecker Street Research: https://www.bleeckerstreetresearch.com/research/via
- WTKR, Hampton Roads: https://www.wtkr.com/transportation/hampton-roads-transit-expands-microtransit-service-makes-changes-for-2026
- UT Arlington, Via fare change (Mar 2026): https://www.uta.edu/pats/news/2026/New%20VIA%20Arlington%20Transit%20Fare%20Rates%20Begin%20Monday,%20March%202.php
- Apple iTunes Search/RSS APIs and Google Play (via `google-play-scraper`)
