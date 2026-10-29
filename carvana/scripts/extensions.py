# Monthly extension / modification rates by pool, pool age and FICO band, Carvana vs CarMax.
#
# Input: files from parse_mods.py, named $CVNA_WORK/abs/mods/<ISSUER>-<deal>_<YYYY-MM>.csv.gz
#   (e.g. CVNA-2025-P2_2026-09.csv.gz, KMX-2024-1_2026-09.csv.gz), plus a pool-age table
#   $CVNA_WORK/abs/mods/first_report.csv with columns deal,first_absee (issuance ABS-EE filing date).
# Output: ../data/scraped/extensions_by_pool_month.csv and extensions_by_fico.csv
#
# Field meanings (SEC ABS XML spec v3.1, auto loans):
#   reportingPeriodModificationIndicator  loan modified from original terms during the period
#   modificationTypeCode                  1 APR, 2 principal, 3 term, 4 extension, 98 other (can repeat)
#   paymentExtendedNumber                 months the loan was extended during the period
# Both issuers fill these only on loans modified that month, so every rate here is a monthly flow:
#   ext_rate_pct  = loans extended this month / loans with a balance at the start of the month
import glob, os, re
import pandas as pd

W = os.environ.get('CVNA_WORK', '.') + '/abs/mods/'
OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'scraped')
first = pd.read_csv(W + 'first_report.csv').set_index('deal').first_absee

def fico_band(s):
    # Carvana 2026 pools report 'VS 655, FICO 686'; take the FICO number
    s = s.fillna('').str.extract(r'(?:FICO\s*)?(\d{3}(?:\.\d+)?)\s*$')[0]
    s = pd.to_numeric(s, errors='coerce')
    return pd.cut(s, [0, 599.5, 649.5, 699.5, 749.5, 1000], labels=['<600', '600–649', '650–699', '700–749', '750+'])

rows, frows = [], []
for f in sorted(glob.glob(W + '*_????-??.csv.gz')):
    deal, period = re.match(r'(.+)_(\d{4}-\d{2})\.csv\.gz$', os.path.basename(f)).groups()
    y = pd.read_csv(f, dtype=str)
    y['beg'] = pd.to_numeric(y.reportingPeriodBeginningLoanBalanceAmount, errors='coerce').fillna(0)
    y['end'] = pd.to_numeric(y.reportingPeriodActualEndBalanceAmount, errors='coerce').fillna(0)
    y['dq'] = pd.to_numeric(y.currentDelinquencyStatus, errors='coerce').fillna(0)
    y['mod'] = y.reportingPeriodModificationIndicator.eq('true')
    codes = y.modificationTypeCode.fillna('')
    y['months_ext'] = pd.to_numeric(y.paymentExtendedNumber.str.split('|').str[0], errors='coerce').fillna(0)
    y['ext'] = y['mod'] & (codes.str.split('|').apply(lambda c: '4' in c) | (y.months_ext > 0))
    y['other_mod'] = y['mod'] & ~y['ext']
    y['fico'] = fico_band(y.obligorCreditScore)
    a = y[y.beg > 0]                                     # loans with a balance at the start of the month
    act_end = y[(y.end > 0) & y.zeroBalanceCode.isna()]  # still active at month end
    p = pd.Period(period, 'M')
    age = (p - pd.Period(first[deal][:7], 'M')).n
    ext = a[a.ext]
    rows.append(dict(
        deal=deal, issuer=deal.split('-')[0], period=period, pool_age_months=age, loans_start=len(a),
        ext_rate_pct=100 * a.ext.mean(),
        ext_rate_bal_pct=100 * a.loc[a.ext, 'beg'].sum() / a.beg.sum(),
        months_ext_per_100=100 * a.months_ext.sum() / len(a),
        other_mod_rate_pct=100 * a.other_mod.mean(),
        ext_current_at_month_end_pct=100 * (ext.dq < 30).mean() if len(ext) else None,
        dq30_end_pct=100 * (act_end.dq >= 30).mean(),
        fico_lt650_pct=100 * a.fico.isin(['<600', '600–649']).mean()))
    for b, g in a.groupby('fico', observed=True):
        frows.append(dict(deal=deal, issuer=deal.split('-')[0], period=period, pool_age_months=age,
                          fico=b, loans_start=len(g), ext_rate_pct=100 * g.ext.mean()))

out = pd.DataFrame(rows).sort_values(['issuer', 'deal', 'period'])
out.round(3).to_csv(os.path.join(OUTD, 'extensions_by_pool_month.csv'), index=False)
pd.DataFrame(frows).round(3).to_csv(os.path.join(OUTD, 'extensions_by_fico.csv'), index=False)
print(out.round(2).to_string(index=False))
