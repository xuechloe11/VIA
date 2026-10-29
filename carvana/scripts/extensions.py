# Extension rates by pool and pool age, Carvana vs CarMax.
# Input: per-pool monthly status files from parse_perf.py (must include paymentExtendedNumber),
#   named $CVNA_WORK/abs/perf/<deal>_<period>.csv.gz, where <period> sorts by month (e.g. 2026-09).
# Output: ../data/scraped/extensions_by_pool_age.csv
#
# Metrics per pool-month (active loans only):
#   ext_ever_pct   share of active loans extended at least once
#   ext_new_pct    share of loans active last month whose extension count rose this month
#   ext_per_loan   average extensions per active loan
# Compare pools at the same age (months since first report), as in same_age_oct2025_vs_oct2026.csv.
import glob, os, re, sys
import pandas as pd

P = os.environ.get('CVNA_WORK', '.') + '/abs/perf/'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'scraped', 'extensions_by_pool_age.csv')

files = sorted(glob.glob(P + '*.csv.gz'))
if not files:
    sys.exit(f'no status files in {P}')

def load(path):
    y = pd.read_csv(path, dtype=str)
    if 'paymentExtendedNumber' not in y.columns:
        sys.exit(f'{path} has no paymentExtendedNumber column: re-run parse_perf.py')
    y['bal'] = pd.to_numeric(y.reportingPeriodActualEndBalanceAmount, errors='coerce').fillna(0)
    y['ext'] = pd.to_numeric(y.paymentExtendedNumber, errors='coerce').fillna(0)
    y['active'] = y.zeroBalanceCode.isna() & (y.bal > 0)
    return y.drop_duplicates('assetNumber', keep='last').set_index('assetNumber')

by_deal = {}
for f in files:
    m = re.match(r'(.+?)_(.+)\.csv\.gz$', os.path.basename(f))
    if m:
        by_deal.setdefault(m.group(1), []).append((m.group(2), f))

rows = []
for deal, items in by_deal.items():
    items.sort()
    prev = None
    for i, (period, f) in enumerate(items):
        y = load(f)
        a = y[y.active]
        r = dict(deal=deal, period=period, month_index=i, active_loans=len(a),
                 ext_ever_pct=100 * (a.ext > 0).mean() if len(a) else None,
                 ext_per_loan=a.ext.mean() if len(a) else None, ext_new_pct=None)
        if prev is not None:
            both = prev[prev.active].join(y[['ext']], rsuffix='_now', how='inner')
            if len(both):
                r['ext_new_pct'] = 100 * (both.ext_now > both.ext).mean()
        rows.append(r)
        prev = y

out = pd.DataFrame(rows)
out['issuer'] = out.deal.str.contains('carmax', case=False).map({True: 'CarMax', False: 'Carvana'})
out.round(3).to_csv(OUT, index=False)
print(out.round(2).to_string(index=False))
# Note: month_index counts available files, not months since issuance. To compare same-age pools,
# include each pool's first monthly file, or join to reportingPeriodEndingDate vs issuance month.
