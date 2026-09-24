import json, re, collections, statistics as st
ia={m['app_id']:m for m in json.load(open('ios_apps.json'))}
R=[]
for r in json.load(open('ios_reviews.json')):
    R.append(dict(store='ios',app=ia[r['app_id']]['name'],rating=r['rating'],text=(r['title']+'. '+r['text']),date=r['date'][:10]))
for a in json.load(open('gp.json')):
    for r in a['reviews']: R.append(dict(store='gp',app=a['name'],rating=r['rating'],text=r['text'] or '',date=r['date'][:10]))
json.dump(R,open('all_reviews.json','w'))
def kind(n):
    n=n.lower()
    if 'driver' in n and 'via driver' in n: return 'driver'
    if 'school' in n or 'field trip' in n: return 'school'
    if any(k in n for k in ['para','access','ada','mataplus','bcare','kako']): return 'paratransit'
    return 'microtransit'
T={
 'wait_late':r'\bwait(ed|ing)?\b|\blate\b|\bhour\b|\bhours\b|\b\d{2,3} ?min|took forever|delay|eta|pick ?up time|never (came|showed|arrived)|no.?show',
 'no_availability':r'no (rides?|vehicles?|drivers?|seats?) (are )?available|not available|unavailable|no availability|fully booked|can\'?t (get|book|find) a ride|couldn\'?t (get|book)|capacity|sold out|try again later',
 'cancel':r'cancel',
 'detour_long_trip':r'detour|picked up (other|more)|went the wrong|long route|around the (city|town)|shared ride|pick up everyone|zig',
 'app_bug':r'crash|bug|glitch|won\'?t (load|open|let)|log ?in|freez|update|error|verification|code',
 'driver_conduct':r'rude|unprofessional|reckless|speed|phone while|unsafe|yell|attitude',
 'service_cut':r'cut|reduced|no longer|discontinu|ended|shut down|hours changed|zone|service area|boundary|removed',
 'payment':r'charg|refund|payment|card|price|fare|expensive',
}
def tag(t):
    t=t.lower(); return [k for k,p in T.items() if re.search(p,t)]
for r in R: r['kind']=kind(r['app']); r['tags']=tag(r['text']); r['year']=r['date'][:4]
rider=[r for r in R if r['kind']!='driver']
print('total',len(R),'rider',len(rider))
for k in ['microtransit','paratransit','school','driver']:
    s=[r['rating'] for r in R if r['kind']==k]
    if s: print(k,len(s),'mean %.2f'%st.mean(s),'1-2 star %.0f%%'%(100*sum(x<=2 for x in s)/len(s)))
print('\nby year (rider)')
by=collections.defaultdict(list)
for r in rider: by[r['year']].append(r['rating'])
for y in sorted(by): print(y,len(by[y]),'%.2f'%st.mean(by[y]),'%.0f%% 1-2'%(100*sum(x<=2 for x in by[y])/len(by[y])))
print('\ntopic share: low (1-2) vs high (4-5), rider reviews')
lo=[r for r in rider if r['rating']<=2]; hi=[r for r in rider if r['rating']>=4]
for k in T: print(f"{k:18s} low {100*sum(k in r['tags'] for r in lo)/len(lo):5.1f}%  high {100*sum(k in r['tags'] for r in hi)/len(hi):5.1f}%")
print('n low',len(lo),'n high',len(hi))
# per-app worst (min 20 reviews)
pa=collections.defaultdict(list)
for r in rider: pa[r['app']].append(r['rating'])
print('\nworst apps by recent-review mean (n>=20)')
for a,s in sorted(pa.items(), key=lambda x: st.mean(x[1])):
    if len(s)>=20: print(f"{a:40s} n={len(s):4d} mean={st.mean(s):.2f} low={100*sum(x<=2 for x in s)/len(s):.0f}%")
