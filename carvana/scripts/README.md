# Scrape pipeline (Carvana customer profile)

Set `CVNA_WORK` to a scratch folder; raw downloads stay there, only summary tables go in `../data/scraped/`.

| Step | Script | Source |
|---|---|---|
| Loan-level borrower data | `parse_absee.py` (stdin XML -> CSV), `parse_perf.py` (monthly status) | SEC EDGAR ABS-EE exhibit 102 (Reg AB II) for Carvana Auto Receivables Trusts and CarMax Auto Owner Trusts |
| Extension rates | `extensions.py` (share of active loans ever / newly extended, by pool and month; needs `paymentExtendedNumber` from `parse_perf.py`) | Monthly ABS-EE files, Carvana and CarMax |
| October snapshot | `perf_snapshot.py` (per-loan status; charged-off = zero-balance code 4 or later re-code 2) | Latest monthly ABS-EE files |
| Loan loader / derived fields | `load_loans.py` (FICO, implied income = monthly payment / PTI x 12, LTV, vehicle age) | — |
| Vehicle segments | `segments.py` (pickup / SUV / car / EV keyword map) | — |
| Census join | `census.py` | ACS 2024 table-based summary files (www2.census.gov) + 2024 ZCTA gazetteer |
| Reddit | `arctic.py` | Arctic Shift Reddit archive API |
| Text mining | `textmine.py` (buyer/seller split, theme keywords) | App Store RSS, Google Play (google-play-scraper), Reddit |

Example: `curl -A "<name> <email>" <ex102 url> | python3 parse_absee.py 2026-P3 $CVNA_WORK/abs/loans/2026-P3.csv.gz`
