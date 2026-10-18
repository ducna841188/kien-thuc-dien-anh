"""Local keyword lookup. No external model or network."""
from pathlib import Path
import json,sys,re,unicodedata,argparse
ROOT=Path(__file__).resolve().parents[1]
def norm(s):
 s=unicodedata.normalize('NFD',s.lower()).replace('đ','d')
 return ''.join(c for c in s if unicodedata.category(c)!='Mn')
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('query',nargs='?',default='');p.add_argument('--id');p.add_argument('--limit',type=int,default=8)
 a=p.parse_args()
 if a.id:
  target=ROOT/'kien-thuc'/f'{a.id.upper()}.json'
  if not target.exists():raise SystemExit('Không có mã '+a.id)
  print(target.read_text());raise SystemExit
 words=set(re.findall(r'[a-z0-9]+',norm(a.query)))
 words-={'toi','muon','ban','cho','la','va','cua','mot','nhung','can','hay','gi'}
 scores={}
 routes=json.loads((ROOT/'tuyen-tra-cuu.json').read_text())['routes']
 for route in routes:
  count=sum(w in norm(route['query_hint']) for w in words)
  for ident in route['core_ids']:scores[ident]=scores.get(ident,0)+count*3
 result=[]
 for path in (ROOT/'kien-thuc').glob('*.json'):
  c=json.loads(path.read_text());text=norm(json.dumps(c,ensure_ascii=False))
  score=scores.get(c['id'],0)+sum(w in text for w in words)
  if score:result.append({'id':c['id'],'title':c['title'],'score':score,'path':str(path.relative_to(ROOT))})
 result.sort(key=lambda x:(-x['score'],x['id']))
 print(json.dumps(result[:max(1,a.limit)],ensure_ascii=False,indent=2))
