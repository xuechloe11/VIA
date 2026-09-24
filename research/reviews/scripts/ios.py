import json, urllib.request, time, concurrent.futures as cf
def get(u):
    for i in range(3):
        try: return json.load(urllib.request.urlopen(u, timeout=30))
        except Exception as e: time.sleep(1+i)
    return None
apps={}
d=get("https://itunes.apple.com/lookup?id=657777018&entity=software&limit=500&country=us")
for r in d['results'][1:]: apps[r['trackId']]=r
for t in ["via transportation","on demand transit","microtransit","paratransit","powered by via","via","flex on demand","transit connect","shuttle on demand"]:
    d=get(f"https://itunes.apple.com/search?term={urllib.parse.quote(t)}&entity=software&limit=200&country=us")
    for r in (d or {}).get('results',[]):
        if r.get('artistId')==657777018: apps[r['trackId']]=r
print("apps",len(apps))
def reviews(tid):
    out=[]
    for p in range(1,11):
        d=get(f"https://itunes.apple.com/us/rss/customerreviews/page={p}/id={tid}/sortby=mostrecent/json")
        e=(d or {}).get('feed',{}).get('entry')
        if not e: break
        if isinstance(e,dict): e=[e]
        for x in e:
            if 'im:rating' not in x: continue
            out.append(dict(app_id=tid,rating=int(x['im:rating']['label']),title=x['title']['label'],text=x['content']['label'],date=x['updated']['label'],version=x.get('im:version',{}).get('label')))
    return out
import urllib.parse
allr=[]
with cf.ThreadPoolExecutor(8) as ex:
    for res in ex.map(reviews, list(apps)): allr+=res
meta=[dict(app_id=k,name=v['trackName'],avg=v.get('averageUserRating'),n=v.get('userRatingCount'),released=v.get('releaseDate'),desc=v.get('description','')[:300]) for k,v in apps.items()]
json.dump(meta,open('ios_apps.json','w'),indent=1); json.dump(allr,open('ios_reviews.json','w'))
print("reviews",len(allr))
