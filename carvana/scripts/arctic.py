import json, subprocess, time, sys, urllib.parse
def fetch(params, maxn=50000, sleep=0.4, kind='posts'):
    out=[]; before=None
    while len(out)<maxn:
        p=dict(params); p['limit']=100; p['sort']='desc'
        if before: p['before']=before
        u=f'https://arctic-shift.photon-reddit.com/api/{kind}/search?'+urllib.parse.urlencode(p)
        d=None
        for attempt in range(7):
            o=subprocess.run(['curl','-sS','-A','Mozilla/5.0 research-script/0.1',u],capture_output=True,text=True).stdout
            try:
                d=json.loads(o)
                if d.get('error'): d=None; raise ValueError
                break
            except Exception: time.sleep(4*(attempt+1))
        if not d or not d.get('data'): break
        batch=d['data']
        out+=[{k:x.get(k) for k in ['id','subreddit','title','selftext','body','created_utc','score','num_comments','link_flair_text','author','link_id']} for x in batch]
        nb=min(x['created_utc'] for x in batch)
        if before is not None and nb>=before: break
        before=nb
        if len(batch)<100: break
        time.sleep(sleep)
    return out
if __name__=='__main__':
    params=json.loads(sys.argv[1]); outp=sys.argv[2]
    kind=sys.argv[3] if len(sys.argv)>3 else 'posts'
    r=fetch(params,kind=kind)
    json.dump(r,open(outp,'w'))
    print(outp,len(r), time.strftime('%Y-%m-%d',time.gmtime(min(x['created_utc'] for x in r))) if r else '')
