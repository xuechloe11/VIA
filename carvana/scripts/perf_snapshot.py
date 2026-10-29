import glob, pandas as pd, numpy as np
import os
exec(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'load_loans.py')).read())
P=os.environ.get('CVNA_WORK', '.')+'/abs/perf/'
def status(deal, acc):
    y=pd.read_csv(P+f'{deal}_{acc}.csv.gz',dtype=str)
    y['bal']=pd.to_numeric(y.reportingPeriodActualEndBalanceAmount,errors='coerce').fillna(0)
    y['dq']=pd.to_numeric(y.currentDelinquencyStatus,errors='coerce')
    y['co']=y.zeroBalanceCode.isin(['4','2'])   # 4 = charged off; charged-off loans are later re-coded 2 (third-party sale)
    y['closed']=y.zeroBalanceCode.notna()
    y['active']=(~y.closed)&(y.bal>0)
    y['repo']=y.repossessedIndicator.eq('true')
    y=y.drop_duplicates('assetNumber',keep='last')
    return y[['assetNumber','reportingPeriodEndingDate','bal','dq','co','closed','active','repo']]
