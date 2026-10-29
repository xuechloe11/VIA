# Who gets extended, and what happens to them a year later. Carvana vs CarMax.
# Input: parse_mods.py files in $CVNA_WORK/abs/mods/ for Aug and Sep of 2025 and 2026 (same pools as extensions.py).
# Outputs (../data/scraped/):
#   cure_by_extension.csv          per pool, Sep 2025 and Sep 2026: of loans 30+ days late in Aug, share extended in Sep;
#                                  of Sep extensions, share that were 30+ late in Aug; by FICO band
#   extension_outcomes_sep2026.csv loans extended in Sep 2025, by Aug 2025 status, and their status at Sep 30, 2026
#   repurchases_by_pool.csv        lifetime repurchases (zero-balance code 3) vs charge-offs, and status before repurchase
import glob, os
import pandas as pd

W = os.environ.get('CVNA_WORK', '.') + '/abs/mods/'
OUTD = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'scraped')
first = pd.read_csv(W + 'first_report.csv').set_index('deal').first_absee

def band(s):
    s = pd.to_numeric(s.fillna('').str.extract(r'(?:FICO\s*)?(\d{3}(?:\.\d+)?)\s*$')[0], errors='coerce')
    return pd.cut(s, [0, 649.5, 699.5, 749.5, 1000], labels=['<650', '650–699', '700–749', '750+'])

def load(deal, period):
    y = pd.read_csv(f'{W}{deal}_{period}.csv.gz', dtype=str)
    y['end'] = pd.to_numeric(y.reportingPeriodActualEndBalanceAmount, errors='coerce').fillna(0)
    y['dq'] = pd.to_numeric(y.currentDelinquencyStatus, errors='coerce').fillna(0)
    months = pd.to_numeric(y.paymentExtendedNumber.fillna('').str.split('|').str[0], errors='coerce').fillna(0)
    y['ext'] = y.reportingPeriodModificationIndicator.eq('true') & (
        y.modificationTypeCode.fillna('').str.contains(r'(?:^|\|)4(?:$|\|)') | (months > 0))
    return y.drop_duplicates('assetNumber', keep='last').set_index('assetNumber')

# 1. Cure by extension: Aug status -> Sep extension
rows = []
for yr in ['2025', '2026']:
    for f in sorted(glob.glob(f'{W}*_{yr}-09.csv.gz')):
        deal = os.path.basename(f).split('_')[0]
        a, s = load(deal, f'{yr}-08'), load(deal, f'{yr}-09')
        a = a[(a.end > 0) & a.zeroBalanceCode.isna()]
        j = a[['dq', 'obligorCreditScore']].join(s[['ext']], how='inner')
        j['band'] = band(j.obligorCreditScore)
        age = (pd.Period(f'{yr}-09', 'M') - pd.Period(first[deal][:7], 'M')).n
        for b, g in [('all', j)] + list(j.groupby('band', observed=True)):
            late = g.dq >= 30
            rows.append(dict(deal=deal, issuer=deal.split('-')[0], period=f'{yr}-09', pool_age_months=age, fico=b,
                             active_aug=len(g), late_aug=int(late.sum()), late_aug_extended_sep=int((late & g.ext).sum()),
                             current_aug_extended_sep=int((~late & g.ext).sum())))
c = pd.DataFrame(rows)
c['dq30_aug_pct'] = 100 * c.late_aug / c.active_aug
c['late_extended_pct'] = 100 * c.late_aug_extended_sep / c.late_aug.where(c.late_aug > 0)
c['extensions_from_late_pct'] = 100 * c.late_aug_extended_sep / (c.late_aug_extended_sep + c.current_aug_extended_sep).where(lambda x: x > 0)
c['late_cured_by_ext_pct_of_pool'] = 100 * c.late_aug_extended_sep / c.active_aug
c.round(3).to_csv(os.path.join(OUTD, 'cure_by_extension.csv'), index=False)

# 2. One-year outcomes of loans extended in Sep 2025
rows = []
for f in sorted(glob.glob(f'{W}*_2025-09.csv.gz')):
    deal = os.path.basename(f).split('_')[0]
    a, s, z = load(deal, '2025-08'), load(deal, '2025-09'), load(deal, '2026-09')
    a = a[(a.end > 0) & a.zeroBalanceCode.isna()]
    b = a[['dq']].join(s[['ext', 'end', 'zeroBalanceCode']], how='inner')
    b = b[((b.end > 0) & b.zeroBalanceCode.isna()) | b.ext]
    b = b.join(z[['zeroBalanceCode', 'dq']].rename(columns={'zeroBalanceCode': 'zb', 'dq': 'dq26'}), how='left')
    late = b.dq >= 30
    for name, m in {'late Aug, extended Sep': late & b.ext, 'late Aug, not extended': late & ~b.ext,
                    'current Aug, extended Sep': ~late & b.ext, 'current Aug, not extended': ~late & ~b.ext}.items():
        g = b[m]
        rows.append(dict(deal=deal, issuer=deal.split('-')[0], group=name, loans=len(g),
                         charged_off=int(g.zb.isin(['2', '4']).sum()), repurchased=int(g.zb.eq('3').sum()),
                         late_30plus=int((g.zb.isna() & (g.dq26 >= 30)).sum()), paid_off=int(g.zb.eq('1').sum())))
pd.DataFrame(rows).to_csv(os.path.join(OUTD, 'extension_outcomes_sep2026.csv'), index=False)

# 3. Repurchases (zero-balance code 3)
rows = []
for f in sorted(glob.glob(f'{W}*_2026-09.csv.gz')):
    deal = os.path.basename(f).split('_')[0]
    s, a = load(deal, '2026-09'), load(deal, '2026-08')
    new = s.index[s.zeroBalanceCode.eq('3')].difference(a.index[a.zeroBalanceCode.eq('3')])
    prior = a.loc[a.index.intersection(new), 'dq']
    rows.append(dict(deal=deal, issuer=deal.split('-')[0], pool_age_months=(pd.Period('2026-09', 'M') - pd.Period(first[deal][:7], 'M')).n,
                     loans=len(s), repurchased_lifetime=int(s.zeroBalanceCode.eq('3').sum()),
                     charged_off_lifetime=int(s.zeroBalanceCode.isin(['2', '4']).sum()),
                     repurchased_in_sep=len(new), of_which_30plus_late_in_aug=int((prior >= 30).sum())))
r = pd.DataFrame(rows)
r['repurchased_pct'] = 100 * r.repurchased_lifetime / r.loans
r.round(3).to_csv(os.path.join(OUTD, 'repurchases_by_pool.csv'), index=False)
print('done')
