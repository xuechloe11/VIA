import json,urllib.request,urllib.parse,time,concurrent.futures as cf,statistics as st
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u,timeout=30))
        except: time.sleep(1+i)
apps={}
for t in ["spare labs","powered by spare","rideco","on demand transit","microtransit","dial a ride","uber","lyft","transit app"]:
    for r in (get(f"https://itunes.apple.com/search?term={urllib.parse.quote(t)}&entity=software&limit=200&country=us") or {}).get('results',[]):
        s=r['sellerName']
        g='Spare' if 'Spare Labs' in s else 'RideCo' if 'RideCo' in s else 'Uber/Lyft' if r['trackId'] in (368677368,529379082) else None
        if g: apps[r['trackId']]=(g,r['trackName'],r.get('averageUserRating'),r.get('userRatingCount'))
def rv(tid):
    out=[]
    for p in range(1,11):
        e=(get(f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={tid}/sortby=mostrecent/json") or {}).get('feed',{}).get('entry')
        if not e: break
        if isinstance(e,dict): e=[e]
        out+=[int(x['im:rating']['label']) for x in e if 'im:rating' in x]
    return tid,out
res={}
with cf.ThreadPoolExecutor(8) as ex:
    for tid,o in ex.map(rv,list(apps)): res[tid]=o
# Via iOS only for apples-to-apples
via=json.load(open('ios_reviews.json')); vm={m['app_id']:m for m in json.load(open('ios_apps.json'))}
out={}
def summ(name,headline_pairs,written):
    tot=sum(n for a,n in headline_pairs if a and n); hw=sum(a*n for a,n in headline_pairs if a and n)/tot if tot else None
    out[name]=dict(n_apps=len(headline_pairs),star_ratings=tot,headline_avg=hw,written_n=len(written),written_avg=st.mean(written) if written else None,written_low=sum(x<=2 for x in written)/len(written) if written else None)
viarider=[m for m in vm.values() if 'Driver' not in m['name']]
summ('Via (agency rider apps)',[(m['avg'],m['n']) for m in viarider],[r['rating'] for r in via if 'Driver' not in vm[r['app_id']]['name']])
for g in ['Spare','RideCo','Uber/Lyft']:
    ids=[k for k,v in apps.items() if v[0]==g]
    summ(g,[(apps[k][2],apps[k][3]) for k in ids],[x for k in ids for x in res[k]])
for k,v in out.items(): print(k,{a:(round(b,3) if isinstance(b,float) else b) for a,b in v.items()})
json.dump(out,open('bench.json','w'),indent=1)
