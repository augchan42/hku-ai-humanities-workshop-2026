"""Archive album images at readable resolution; retain Google Photos IDs and URLs."""
import json, pathlib, urllib.request, concurrent.futures
root=pathlib.Path(__file__).resolve().parent.parent
photos=json.loads((root/'sources/slides/manifest.json').read_text())
def fetch(p):
 target=root/p['image']
 if not target.exists():
  req=urllib.request.Request(p['image_url']+'=w2000-h2000',headers={'User-Agent':'Mozilla/5.0'})
  with urllib.request.urlopen(req,timeout=60) as r: target.write_bytes(r.read())
 return p['id']
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
 for i,result in enumerate(pool.map(fetch,photos),1):
  if i%25==0 or i==len(photos):print(f'{i}/{len(photos)} archived',flush=True)
