# VIA – software vs. services mix

`model/VIA_software_services_mix.xlsx` (rebuild with `python3 model/build_model.py`)

| Tab | What it does |
|---|---|
| Summary | Headline outputs and takeaways |
| Bleecker_Replication | Bleecker's actual method (gross-margin back-out from TaaS unit economics): as published, arithmetic corrected, and updated with 2026 contract $/hr and TTM adj. GM; cross-checked against the reported cost split |
| Margin_Inputs | Revenue, 3-way cost-of-revenue split, adjusted gross profit (FY24–Q2'26) |
| Margin_Decomp | Mix backed out from the reported cost split for a given services GM; sensitivity grids |
| Blended_Formula | (gS − g)/(gS − gV) on reported blended GM |
| Contracts | Tracker incl. hourly rates (micro/para) from pre- and post-Dec-2025 contracts |
| Consensus_Check | Bloomberg consensus (Q3'25A–Q4'27E): margins, opex leverage, insurance-in-G&A test, valuation multiples, illustrative SOTP |
| ACV_CrossCheck | Alternative: Bleecker 72% baseline + incremental contract ACV |
| Sources | URLs for every hardcoded number |

Key results:
- Bleecker as published: 71.7% services (Q3'25 adj GM 40%, TaaS GM 26.2%, SaaS GM 75%).
- Their inputs sum to a 29.2% TaaS GM, not 26.2%; corrected, their method gives 76.4%.
- Updated with 2026 pricing (micro $67.26/hr avg of Douglas Co. $70 and University Park $64.52; para $67.75), +3% cost inflation, TTM adj GM 40.25%: **76.0% services** (73.3% at Q2'26 adj GM; 73.1% with paratransit at 30% of hours).
- Cross-check: that mix implies services cost of 53.8% of revenue (reported: 51.9% tech-enabled, 57.5% incl. launch & support) and software GM of 73%.
- Via's FY25 10-K confirms insurance and customer support costs sit in G&A, not cost of revenue.

Consensus (BBG): GM stays ~40–41% through FY27 (no 50% path assumed); FY27 revenue +22% with opex +3.9% and G&A +1.8%, taking adj. EBITDA margin from −1.3% (FY26E) to +4.4% (FY27E). At ~$29.57: EV ~$2.15B = 7.8x FY27E GP, 73x FY27E adj. EBITDA.
