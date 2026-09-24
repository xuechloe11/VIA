import json, re, urllib.request, concurrent.futures as cf
from google_play_scraper import app, reviews, Sort, search
# developer page listing
ids=set()
for q in ["via transportation","powered by via","on demand transit via","microtransit","paratransit app","Via Transportation, Inc."]:
    try:
        for r in search(q, n_hits=30, lang='en', country='us'):
            if 'Via Transportation' in (r.get('developer') or ''): ids.add(r['appId'])
    except Exception as e: print('search err',q,e)
try:
    html=urllib.request.urlopen(urllib.request.Request("https://play.google.com/store/apps/developer?id=Via+Transportation,+Inc.&hl=en",headers={'User-Agent':'Mozilla/5.0'}),timeout=30).read().decode()
    ids|=set(re.findall(r'/store/apps/details\?id=([\w.]+)',html))
except Exception as e: print('dev page err',e)
print('candidate ids',len(ids))
def pull(aid):
    try:
        a=app(aid,lang='en',country='us')
        if 'Via Transportation' not in (a.get('developer') or ''): return None
        rv,_=reviews(aid,lang='en',country='us',sort=Sort.NEWEST,count=1000)
        return dict(app_id=aid,name=a['title'],avg=a.get('score'),n=a.get('ratings'),installs=a.get('realInstalls'),
          reviews=[dict(rating=r['score'],text=r['content'],date=str(r['at']),reply=bool(r.get('replyContent'))) for r in rv])
    except Exception as e: return None
res=[]
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(pull, ids):
        if r: res.append(r)
json.dump(res,open('gp.json','w'))
print('apps',len(res),'reviews',sum(len(r['reviews']) for r in res))
