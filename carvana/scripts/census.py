import pandas as pd, numpy as np
import os
C=os.environ.get('CVNA_WORK', '.')+'/census'
def _t(prefix,t):
    d=pd.read_csv(f'{C}/{prefix}_{t}.dat',sep='|',dtype=str)
    d=d.set_index('GEO_ID')
    return d[[c for c in d.columns if '_E' in c]].apply(pd.to_numeric,errors='coerce')
def build(prefix):
    p=_t(prefix,'b01003')['B01003_E001'].rename('pop')
    inc=_t(prefix,'b19013')['B19013_E001'].rename('med_hh_income')
    age=_t(prefix,'b01002')['B01002_E001'].rename('med_age')
    ten=_t(prefix,'b25003'); own=(ten['B25003_E002']/ten['B25003_E001']).rename('owner_share')
    com=_t(prefix,'b08301'); transit=(com['B08301_E010']/com['B08301_E001']).rename('transit_share')
    ed=_t(prefix,'b15003'); ba=((ed['B15003_E022']+ed['B15003_E023']+ed['B15003_E024']+ed['B15003_E025'])/ed['B15003_E001']).rename('ba_share')
    emp=_t(prefix,'b23025'); af=(emp['B23025_E006']/emp['B23025_E001']).rename('armed_forces_share')
    veh=_t(prefix,'b25044'); hh=veh['B25044_E001']
    zero=((veh['B25044_E003']+veh['B25044_E010'])/hh).rename('zero_car_hh_share')
    two=((veh['B25044_E005']+veh['B25044_E006']+veh['B25044_E007']+veh['B25044_E008']+veh['B25044_E012']+veh['B25044_E013']+veh['B25044_E014']+veh['B25044_E015'])/hh).rename('two_plus_car_hh_share')
    out=pd.concat([p,inc,age,own,transit,ba,af,zero,two,hh.rename('households')],axis=1)
    try:
        vet=_t(prefix,'b21001'); out['veteran_share']=vet['B21001_E002']/vet['B21001_E001']
    except Exception: pass
    return out
def zcta():
    z=build('z'); z=z[z.index.str.startswith('860Z200US')]; z.index=z.index.str[-5:]
    g=pd.read_csv(f'{C}/gaz/2024_Gaz_zcta_national.txt',sep='\t',dtype={'GEOID':str}); g.columns=[c.strip() for c in g.columns]
    g=g.set_index('GEOID')
    z=z.join(g['ALAND_SQMI']); z['density']=z['pop']/z['ALAND_SQMI'].replace(0,np.nan)
    return z
FIPS={'01':'AL','02':'AK','04':'AZ','05':'AR','06':'CA','08':'CO','09':'CT','10':'DE','11':'DC','12':'FL','13':'GA','15':'HI','16':'ID','17':'IL','18':'IN','19':'IA','20':'KS','21':'KY','22':'LA','23':'ME','24':'MD','25':'MA','26':'MI','27':'MN','28':'MS','29':'MO','30':'MT','31':'NE','32':'NV','33':'NH','34':'NJ','35':'NM','36':'NY','37':'NC','38':'ND','39':'OH','40':'OK','41':'OR','42':'PA','44':'RI','45':'SC','46':'SD','47':'TN','48':'TX','49':'UT','50':'VT','51':'VA','53':'WA','54':'WV','55':'WI','56':'WY','72':'PR'}
def states():
    s=build('s'); s=s[s.index.str.startswith('0400000US')]; s.index=s.index.str[-2:].map(FIPS)
    z=build('z'); z=z[z.index.str.startswith('0400000US')]; z.index=z.index.str[-2:].map(FIPS)
    s['veteran_share']=z['veteran_share']
    return s
