import pandas as pd, numpy as np, glob, re, os
D=os.environ.get('CVNA_WORK', '.')+'/abs/loans'
def load():
    fs=sorted(glob.glob(D+'/*.csv.gz'))
    df=pd.concat([pd.read_csv(f,dtype=str) for f in fs],ignore_index=True)
    num=['originalLoanAmount','originalLoanTerm','originalInterestRatePercentage','vehicleModelYear','vehicleValueAmount',
         'paymentToIncomePercentage','reportingPeriodScheduledPaymentAmount','nextReportingPeriodPaymentAmountDue']
    for c in num: df[c]=pd.to_numeric(df[c],errors='coerce')
    s=df['obligorCreditScore'].fillna('')
    df['fico']=pd.to_numeric(s.str.extract(r'FICO\s*(\d{3})')[0].fillna(s.str.extract(r'^\s*(\d{3})(?:\.\d+)?\s*$')[0]),errors='coerce')
    df['vantage']=pd.to_numeric(s.str.extract(r'VS\s*(\d{3})')[0],errors='coerce')
    df['orig_month']=pd.to_datetime(df['originationDate'],format='%m/%Y',errors='coerce')
    df['orig_year']=df['orig_month'].dt.year
    # monthly payment: scheduled amount if >0 else next due if >0 else amortization formula
    r=df['originalInterestRatePercentage']/12; n=df['originalLoanTerm']; P=df['originalLoanAmount']
    amort=P*r/(1-(1+r)**(-n))
    pay=df['reportingPeriodScheduledPaymentAmount'].where(df['reportingPeriodScheduledPaymentAmount']>0)
    pay=pay.fillna(df['nextReportingPeriodPaymentAmountDue'].where(df['nextReportingPeriodPaymentAmountDue']>0)).fillna(amort)
    df['payment']=pay
    pti=df['paymentToIncomePercentage']
    pti=pti.where(pti<1, pti/100)   # guard if reported as percent
    df['pti']=pti
    df['income_annual']=(df['payment']/df['pti']*12).where((df['pti']>0.005)&(df['pti']<0.6))
    df['ltv']=df['originalLoanAmount']/df['vehicleValueAmount']
    df['veh_age']=df['orig_year']-df['vehicleModelYear']
    df['lender']=np.where(df['deal'].str.startswith('KMX'),'CarMax','Carvana')
    df['deal_year']=df['deal'].str.extract(r'(20\d\d)')[0].astype(int)
    return df
