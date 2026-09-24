# Evidence: network deals are services contracts

Tags follow THESIS_BRIEF.md: **[F]** filing · **[P]** public records · **[M]** our estimate · **[V]** verify
Reproduce the NTD figures with `python3 model/ntd_network_check.py` (FTA National Transit Database 2022–24, datasets j5uj-anzx and ekg5-frzt on data.transportation.gov).

## The argument
1. **A network deal's value is the agency's whole bus operating budget.** Via's contract prices come out at ~95–107% of each customer's total transit operating expense. **[P][M]**
2. **Federal data shows what that budget is made of.** Across 165 mid-sized US bus systems, ~72% of operating cost is labor. Fuel, parts and insurance take another ~16%. Every category that could include software sits inside "services," which is 8.8% and also covers contracted maintenance, security and professional services. **[P]**
3. So by construction, **at least ~90% of a network contract pays for labor, fuel, parts and insurance.** The customer data backs this up at the systems Via runs. **[M]**

---

## 1. Contract value ≈ the agency's entire operating budget **[P][M]**

| Customer | Via contract | Agency total transit operating expense, 2024 (NTD) | Via ÷ opex | Implied $ per vehicle revenue hour |
|---|---|---|---|---|
| Mobile, AL (The Wave) | $12.1M/yr (from Oct 2025) | $12.73M | **95%** | **$103** |
| Rochester, MN (RPT) | $14.6M/yr ($77.8M / 64 mo, from Sep 2026) | $13.64M | **107%** | **$107** |
| Sioux Falls, SD (SAM) | Took over 2024 | $11.48M, of which **96.4%** was paid to the contractor | 96% | $139 all modes |

- **Benchmark (NTD 2024, mid-sized full reporters, $5–50M opex):**
  - Bus systems run by the agency: median **$137/hr** (IQR $114–162, n=165)
  - Bus systems run by a contractor: median **$137/hr** (IQR $121–157, n=87)
- Via's implied $103–107/hr sits at the low end of what contract operators charge. It is **priced as bus operations, not as software.**
- Rochester's 107% is consistent with a full-operations price plus the 20% union wage raise and service growth by 2026.

## 2. What the budget buys: NTD cost structure **[P]**

US bus systems run by the agency itself, full reporters with $5–50M opex, 2024 (n=165, $2.88B):

| Expense type | Share |
|---|---|
| **Labor** (operator and other wages, paid absences, fringe) | **71.8%** (median agency 71.8%, IQR 67.3–76.0%) |
| Fuel, tires, parts | 12.6% |
| Casualty & liability (insurance) | 3.7% |
| Services (contracted maintenance, security, professional services, **incl. any IT/software**) | 8.8% |
| Utilities, taxes, misc. | 3.1% |

**Via's own customers, the year before the handover:**

| Customer | Year | Labor share | Operating model |
|---|---|---|---|
| Sioux Falls | 2023 | **69%** | Agency-run, then contracted to Via in 2024 |
| Mobile | 2024 | **68%**, plus 8% insurance | Agency-run (Transdev managed) |
| Fort Wayne (Via drivers unionized, per the 10-K) | 2024 | **74%** | Agency-run |

**Read-through:** even if the whole "services" line were software, software could be at most ~9% of a network deal. The rest is labor and vehicles, which is ≤10% software, ≥90% services **[M]**. This is the market-wide basis for the ~96% services figure (Sioux Falls: 96.4% of system cost is paid to Via).

## 3. The regulator files these as contracted bus service **[P]**
- **NTD reclassified Sioux Falls** from agency-run ("directly operated," 2022–23) to contracted ("purchased transportation," 2024) when Via took over. That is the same federal category as Transdev, MV and Keolis bus contracts, covering **~$4.6B** of US bus operating expense in 2024.
- **Rochester has always been contracted** (Transdev, ~70% of system cost). Via is replacing one contract operator with itself.

## 4. Via's own filings **[F]**
- **Licensing** (FY25 10-K): where Via uses "employed drivers, larger vehicles, and/or operate[s] … paratransit or fixed route, we are typically licensed as a **motor carrier** or under a more traditional regulatory framework for public transit service."
- **Unions** (FY25 10-K): "we employ drivers … including in **Sioux Falls** … **Mobile** … and Fort Wayne … those employees have unionized and are party to collective bargaining agreements" (ATU, Teamsters, SMART). Two of the four network deals are already on that list.
- **Competitors** (FY25 10-K): "transit operators (such as Deutsche Bahn, Transdev, and MV Transit)."
- **Cost of revenue, Q2'26 10-Q:**
  - Tech-enabled services (driver and fleet management, support) $69.8M of $80.1M
  - Up $13.6M YoY "to support new customers and our growth with existing customers"
- **The revenue label hides the mix.** All subscription services are booked as "a single performance obligation" priced on volume. Driver labor on a bus network and a software licence end up in the same "subscription" revenue, and Via discloses no split.
- **Catalyst:** the FASB's new expense-disaggregation rule (ASU 2024-03, effective FY2027 annual reporting) requires a tabular split of expenses including **employee compensation**. The labor intensity would show up in reported numbers.

## Caveats
- Contract values are ceilings or estimates from council records, and scope can differ from the NTD year (Rochester adds a 2026 wage reset; Mobile adds a route redesign).
- The NTD "services" line isn't split further, so the ≤9% software ceiling is an upper bound, not an estimate.
- Twin Cities, MI is a reduced reporter, with no expense breakdown.
- NTD 2025 (Mobile's first Via year, Sioux Falls' second) isn't released yet. When it is, check Mobile's switch to contracted service and its purchased-transportation share. **[V]**
