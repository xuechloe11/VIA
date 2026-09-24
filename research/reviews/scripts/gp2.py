import json, concurrent.futures as cf, re
from google_play_scraper import app, reviews, Sort, search
have={r['app_id'] for r in json.load(open('gp.json'))}
ids=set(re.findall(r'details\?id=([A-Za-z0-9_.]+)',open('dev.html').read()))
names=[m['name'] for m in json.load(open('ios_apps.json'))]
def s(n):
    try: return [r['appId'] for r in search(n,n_hits=5,lang='en',country='us') if 'Via Transportation' in (r.get('developer') or '')]
    except: return []
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(s,names): ids|=set(r)
ids-=have
print('new ids',len(ids))
def pull(aid):
    try:
        a=app(aid,lang='en',country='us')
        if 'Via Transportation' not in (a.get('developer') or ''): return None
        rv,_=reviews(aid,lang='en',country='us',sort=Sort.NEWEST,count=1000)
        return dict(app_id=aid,name=a['title'],avg=a.get('score'),n=a.get('ratings'),installs=a.get('realInstalls'),
          reviews=[dict(rating=r['score'],text=r['content'],date=str(r['at']),reply=bool(r.get('replyContent'))) for r in rv])
    except Exception: return None
res=json.load(open('gp.json'))
with cf.ThreadPoolExecutor(8) as ex:
    for r in ex.map(pull, ids):
        if r: res.append(r)
json.dump(res,open('gp.json','w'))
print('apps',len(res),'reviews',sum(len(r['reviews']) for r in res))
