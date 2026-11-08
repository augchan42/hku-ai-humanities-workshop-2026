"""Check content coverage, local links, and separation of private material."""
from pathlib import Path
import json,re
root=Path(__file__).resolve().parent.parent
notes=json.loads((root/'content/notes.json').read_text())
assert [n['page'] for n in notes]==list(range(1,13))
assert sum(len(n['notes']) for n in notes)==66
slides=json.loads((root/'sources/slides/manifest.json').read_text())
assert len(slides)==222 and len(set(s['photo_id'] for s in slides))==222
for s in slides:
 assert (root/s['image']).is_file(),s['image']
 assert (root/f'transcripts/slides/{s["id"]}.md').is_file()
 assert (root/f'sources/slides/ocr-enhanced/{s["id"]}.txt').is_file()
for n in notes:
 p=n['page'];text=(root/f'transcripts/notes/page-{p:02}.md').read_text()
 assert len(text)>500
 if p in [3,4]:assert 'clipped' in text
 assert (root/f'sources/notes/pages/page-{p:02}.jpg').is_file()
for folder in ['dist','dist-local']:
 base=root/'site'/folder
 for f in ['index.html','app.js','styles.css','data.js','downloads/workshop-notes.pdf']:
  assert (base/f).is_file(),f
 data=(base/'data.js').read_text()
 assert data.startswith('window.NOTEBOOK = ')
 parsed=json.loads(data.removeprefix('window.NOTEBOOK = ').strip().removesuffix(';'))
 assert len(parsed['notes'])==12 and len(parsed['slides'])==222
 assert parsed['guide']['generation']['model']=='GPT 6.1 Sol high'
 assert 'generation-disclosure' in (base/'app.js').read_text()
 assert 'Generation disclosure' in (base/'index.html').read_text()
 assert 'GPT 6.1 Sol high' in parsed['guide']['generation']['statement']
 assert all(set_['slides'] for set_ in parsed['reviewSets'])
 if folder=='dist':
  assert 'hawthorne' not in parsed and 'hawthorneTranscript' not in parsed
  assert not (base/'private').exists()
  for secret_phrase in ['Paul is in a red room','team of amnesiacs','Self-indication','self-indication','87:38']:
   assert secret_phrase not in data,secret_phrase
 else:
  if (root/'private/hawthorne/guide.json').exists():
   assert len(parsed['hawthorne']['sections'])==10
   assert (base/'private/hawthorne/transcript.md').is_file()
 print(folder,'coverage and private-material separation checked')
assert 'dist-local/' in (root/'site/.gitignore').read_text()
assert 5647*8911==50320417
print('12 PDF pages; 66 explanations; 222 photos, OCR records, and transcript records checked.')
