# Carvana Short: Testing the Credit Catalysts (October 2026)

As of Oct 29, 2026. Follows `CUSTOMER_PROFILE.md`, which found that Carvana's and CarMax's 2026 financed buyers earn the same, but a quarter of Carvana's are under 650 FICO and they take bigger loans on longer terms with less equity. This note tests the four things that would turn that into a catalyst for the short.

Tags as in `CUSTOMER_PROFILE.md`: **[F]** filing or call · **[L]** loan-level SEC data · **[P]** press / rating agency · **[M]** our estimate

## Bottom line
| Test | Result | Helps the short? |
|---|---|---|
| 1. Gain on loan sales vs originations | Margin fell from 9.9% to 7.6% of principal sold in a year. Gain per retail unit fell 17% to $1,753 **[F][M]** | **Yes, partly.** The GOS reset is happening, but management says it is deliberate and volume more than offsets it |
| 2. Loss curves by vintage | Prime 2025–26 pools perform the same as or better than 2024 at the same age. Nonprime deals keep drifting above DBRS's initial loss expectations as they season **[L][P]** | **Not yet** in prime. Nonprime is the weak spot, but 2025–26 nonprime deals are not public |
| 3. Extension rates vs CarMax | **Not tested.** The monthly loan files are on www.sec.gov, which is blocked from this workspace. The script is ready | — |
| 4. Is the sub-650 share rising? | Flat at ~25%. Under-600 nearly tripled (3.9% → 10.8%), but 750+ also grew. Mix-adjusted expected charge-offs are flat **[L][M]** | **No.** The mix is a barbell, not a slide down the credit curve |

**What this means:** on public data, the credit side is not a near-term catalyst. The GOS compression is the strongest evidence for the short. To use it, the short has to argue that the rate give-back is forced (by competition or funding costs) rather than chosen, or that unit growth can't keep covering it. Management already says growth is supply-constrained.

### Two corrections to the earlier framing
- **CarMax's "no sub-650 buyers" is a change in what CarMax securitizes.** CarMax's 2021 public pools had 21.5% sub-650 borrowers. By 2025 they had none. CarMax's lower-credit loans now sit elsewhere, so the 25% vs 0% gap overstates the difference in customers **[L]**.
- **Longer loans haven't produced worse losses so far.** Among 2024 loans, those over 72 months have charged off 2.5% vs 3.8% for 72 months or less. This isn't controlled for income or FICO: long terms went to higher-income buyers. Even so, "longer loans = more losses" isn't showing in the data yet **[L]**.

---

## 1. Gain on loan sales vs originations

Source: Carvana XBRL financial data (10-Q and 10-K, via data.sec.gov), quarterly figures backed out of year-to-date values **[F][M]**.

| Quarter | Gain on loan sales | Loans originated | Principal sold (est.) | Gain ÷ principal sold | Gain per retail unit |
|---|---|---|---|---|---|
| Q3'24 | $224M | $2.16B | $2.23B | 10.1% | $2,062 |
| Q1'25 | $273M | $2.66B | $2.43B | 11.3% | $2,039 |
| Q3'25 | $331M | $3.43B | $3.34B | 9.9% | $2,123 |
| Q4'25 | $315M | $3.63B | $3.42B | 9.2% | $1,926 |
| Q1'26 | $354M | $4.25B | $3.95B | 9.0% | $1,889 |
| Q2'26 | $349M | $4.75B | $4.67B | 7.5% | $1,769 |
| **Q3'26** | **$381M** | **$5.18B** | **$5.02B** | **7.6%** | **$1,753** |

- Year over year, gain on loan sales rose 15% while originations rose 51%.
- Q3'26 gain per retail unit is the lowest since Q2'24 ($1,705).
- The VIC pitch modeled GOS falling toward ~6%. At 7.6%, it is moving that way. But FY26 adjusted EBITDA is guided to the high end of $2.7–3.0B, well above the pitch's $2.44B, because volume grew faster than the margin fell **[F]**.

**Management's explanation (Q3'26 call) [F]:**
- Non-GAAP other GPU (mostly finance) was $2,709, down $299 year over year.
- The main driver was a decision in late 2025 to pass gains back to customers as lower rates relative to benchmarks. Higher benchmark rates in Q3 also weighed on it.
- The CEO said customers' rates have fallen by more than 100bp over two years, mostly for prime customers, and that this has pulled in more prime and higher-priced deals.
- The call gave no specifics on loan-buyer pricing or spreads. Delinquencies and nonprime were not discussed.

**Read:** the compression is real. Management presents it as a deliberate customer investment, not loan buyers pulling back. Nothing here shows buyers demanding higher yields.

*Method note:* principal sold is estimated as sale proceeds minus gain. Gain on loan sales also includes fair-value changes on loans held for sale, so treat these margins as approximate. The trend is the useful part.

## 2. Loss curves by vintage

### Prime (public pools, loan-level) [L]
| Same age, same season | 30+ days late | Cumulative charge-off |
|---|---|---|
| 16–17 months (2024-P2 → 2025-P2) | 2.69% → 2.95% | 1.82% → 1.70% |
| 13–14 months (2024-P3 → 2025-P3) | 2.34% → 2.35% | 1.17% → 1.04% |
| 10–11 months (2024-P4 → 2025-P4) | 1.50% → 1.67% | 0.82% → 0.61% |
| 7–8 months (2025-P1 → 2026-P1) | 1.38% → 0.99% | 0.43% → 0.24% |

- The step-down came earlier. 2024-P2 is at 3.9% charged off by month 29, vs 2.3% for 2021-P1 by month 28.
- The 2025–26 pools are not worse than 2024. There is no fresh deterioration to point to.

### Nonprime (private deals; rating-agency summaries only) [P]
DBRS reviews the nonprime deals every 6–8 months and says whether losses are tracking above or below its initial expectations.

| DBRS release | Tracking **above** initial loss expectations | In line or below | Downgrades |
|---|---|---|---|
| Feb 7, 2025 | 2021-N3 through 2023-N4 | 2021-N1, 2021-N2; 2024-N1 to N3 | 0 |
| Oct 7, 2025 | 2021-N2 through **2024-N1** | 2021-N1; 2024-N2, 2025-N1 | 0 |
| May 13, 2026 | 2021-N2 through **2024-N2** | 2021-N1; 2024-N3, 2025-N1 | 0 |

- Each review, the "above expectations" group extends one deal further. 2024-N1 and 2024-N2 both started "below" and moved "above" as they seasoned.
- DBRS also said total delinquencies were trending higher in every deal (May 2026).
- Bondholders are protected: credit enhancement has grown and there have been no downgrades. The cost of losses running above plan falls on the residual holders and on pricing for future deals.
- I found no public nonprime deal after 2025-N1 (Feb 2025). The KBRA dashboard and DBRS monthly reports are subscriber-only. **So the 2025–26 nonprime vintages can't be checked from public data.** This is the main blind spot.

## 3. Extension rates vs CarMax (not tested)
Extensions push missed payments to the end of the loan, so they can keep a loan out of "delinquent" status. They matter here because Bridgecrest, the servicer, is a related party.

- The monthly loan files (ABS-EE exhibit 102) report each loan's extension count (`paymentExtendedNumber`). They're on www.sec.gov, which this workspace can't reach. data.sec.gov works but only has filing lists and financial data.
- **Ready to run:**
  - `scripts/parse_perf.py` now keeps `paymentExtendedNumber`.
  - New `scripts/extensions.py` reports, for each pool and month: the share of active loans ever extended, the share newly extended that month, and extensions per loan. It writes `data/scraped/extensions_by_pool_age.csv`.
  - Tested on synthetic files.
- **To run:** allow www.sec.gov (Settings > Capabilities), re-download the Sep 2025 and Sep 2026 status files for the Carvana prime pools and same-age CarMax pools, then run `extensions.py`.

## 4. Is the low-credit share rising? [L][M]
FICO mix of public-pool loans, by year made, with the expected charge-off rate if each band charged off at its 2024-vintage rate to date:

| | Under 600 | 600–649 | 650–699 | 700–749 | 750+ | Mix-implied charge-off |
|---|---|---|---|---|---|---|
| Carvana prime, 2021 | 3.9% | 21.7% | 26.1% | 20.9% | 27.4% | 3.19% |
| Carvana prime, 2024 | 6.2% | 22.2% | 24.0% | 19.3% | 28.3% | 3.26% |
| Carvana prime, 2025 | 9.2% | 16.8% | 23.9% | 20.7% | 29.4% | 3.20% |
| **Carvana prime, 2026 (Jan–Jul)** | **10.8%** | 14.5% | 21.2% | 20.9% | **32.7%** | **3.10%** |
| 2026-P3 (prospectus, Aug 2026) | 12.6% | 15.5% | 21.1% | 20.1% | 30.7% | 3.24% |
| CarMax, 2026 (Jan–Aug) | 0% | 0% | 18.2% | 22.3% | 59.5% | 1.78% |

*2024-vintage charge-off rates to date by band: under 600 6.5%, 600–649 5.5%, 650–699 3.8%, 700–749 2.3%, 750+ 1.0%.*

- Sub-650 is steady at about a quarter of loans. Within it, under-600 nearly tripled.
- The top end grew at the same time, so the mix-implied loss rate hasn't moved.
- The under-600 tail is still the group to watch: 7.6% of active 2025 loans under 600 are 30+ days late, vs 0.5% for 750+.
- Caveat: the 2024 rates mostly reflect 550–599 borrowers. Newer pools hold more under-550 loans (3.6% of 2026 loans vs 0% in 2021), so the under-600 band may be riskier than its 2024 rate suggests.

---

## What to watch next
- **Mid-November monthly filings:** 30+ day delinquency for the 2025–26 prime pools against the same-age table above, plus the extension test once www.sec.gov is allowed.
- **Next DBRS / KBRA review of the nonprime deals** (DBRS's last was May 2026, so the next is likely late 2026): whether 2024-N3 and 2025-N1 move into "above expectations." That would make it every nonprime deal since 2021-N2.
- **Q4'26 (Feb 2027):** gain ÷ principal sold (7.6% now; the VIC pitch's ~6% would be a further 1.6 points down) and other GPU per unit, plus any comment on loan-buyer pricing.

## Data files
- `data/scraped/gos_by_quarter.csv`: gain on loan sales, originations, principal sold and per-unit gain, Q1'24–Q3'26.
- `data/scraped/fico_mix_implied_chargeoff.csv`: FICO mix by year made and mix-implied charge-off.
- `data/scraped/dbrs_nonprime_surveillance.csv`: DBRS nonprime groupings by release.
- `scripts/extensions.py`: extension-rate test (needs www.sec.gov).

## Sources
- Carvana XBRL company facts (CIK 1690820), data.sec.gov: GainLossOnSalesOfConsumerLoans, PaymentsForOriginationAndPurchasesOfLoansHeldForSale, ProceedsFromSaleOfLoansHeldForSale.
- Q3'26 call: [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/10/29/carvana-cvna-q3-2026-earnings-call-transcript/). Q3'26 results: [8-K exhibit 99.2](https://www.sec.gov/Archives/edgar/data/0001690820/000169082026000066/ex99_2q32026.htm).
- Morningstar DBRS rating actions: [Feb 2025](https://dbrs.morningstar.com/research/447618/morningstar-dbrs-takes-credit-rating-actions-on-15-carvana-auto-receivables-trust-transactions), [Oct 2025](https://dbrs.morningstar.com/research/464421/morningstar-dbrs-takes-credit-rating-actions-on-16-carvana-auto-receivables-trust-transactions), [May 2026](https://dbrs.morningstar.com/research/480905/morningstar-dbrs-takes-credit-rating-actions-on-14-carvana-auto-receivables-trust-transactions).
- [KBRA nonprime rating actions (Nov 2025)](https://www.kbra.com/publications/RKXDwtcD/kbra-affirms-and-upgrades-ratings-from-carvana-auto-receivables-trust); KBRA surveillance dashboard is subscriber-only.
- Loan-level pool data and 2026-P3 prospectus stats: see `CUSTOMER_PROFILE.md`.
