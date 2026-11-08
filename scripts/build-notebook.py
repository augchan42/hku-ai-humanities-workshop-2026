"""Generate portable static editions and human-readable Markdown from source data.
The hosted edition NEVER includes private/. The local edition includes Hawthorne.
"""
import json,re,shutil,hashlib
from pathlib import Path
root=Path(__file__).resolve().parent.parent
site=root/'site'
notes=json.loads((root/'content/notes.json').read_text())
guide=json.loads((root/'content/guide.json').read_text())
slides=json.loads((root/'sources/slides/manifest.json').read_text())
for n in notes:
 text=(root/f'transcripts/notes/page-{n["page"]:02}.md').read_text()
 n['transcript']=text.split('\n\n',2)[-1]
for s in slides:
 s['day']=1 if s['captured_at'].startswith('2026-11-05') else 2
 s['time']=s['captured_at'][11:16]
 session=next((x for x in guide['sessions'] if x['range'][0]<=s['album_index']<=x['range'][1]),None)
 s['session']=session['id'] if session else 'snapshots'
 s['session_title']=session['title'] if session else 'Workshop snapshots & transitions'
 s['speaker']=session['speaker'] if session else 'Workshop album'
 s['title']=f'{s["speaker"]} · photo {s["album_index"]:03}' if session else f'Workshop photo {s["album_index"]:03}'
 path=root/f'sources/slides/ocr-enhanced/{s["id"]}.txt'
 if not path.exists():path=root/f'sources/slides/ocr/{s["id"]}.txt'
 s['ocr']=path.read_text().replace('\x0c','').strip()
titles={2:'Workshop welcome',3:'Artificial Intelligence, Subjectivity, and Silence',4:'Artificial Intelligence, Subjectivity, and Silence',5:'Dualism: The Primordial Cleft',6:'Wittgenstein and Nagarjuna',7:'Consciousness: Not a something, Not a Nothing',8:'Post-reflective Silence',9:'The Space of Possible Minds',10:'The Unimaginable',12:'What is AI Consciousness?',13:'Belief First and Belief-in',14:'Cultural Pluralism',17:'Closing the Circle',18:'Commentary: plan',21:'Why should criticism end in silence?',32:'Murray on Minds, Wittgenstein on Meaning',33:'Murray on Minds, Wittgenstein on Meaning',39:'Wittgenstein: machines and possible movement',40:'Wittgenstein: following a rule',50:'Boghossian handout photograph',61:'Radical AI Interpretability',62:'Radical AI Interpretability',65:'Plan: radical interpretation adapted for AI',73:'Internal evidence and interpretation',87:'Chuck, Wilson & the Emergence of Artificial Minds',88:'Chuck, Wilson & the Emergence of Artificial Minds',89:'Chuck, Wilson & the Emergence of Artificial Minds',90:'Models and characters',99:'Could fictional characters be minded?',102:'User–LLM conversations and role-playing',105:'Is the character simulated by the user?',112:'Thank you · Winnie Street',113:'Boltzmann Badger and the Relational View of Moral Standing',114:'Boltzmann Badger and the Relational View of Moral Standing',115:'What is moral standing?',117:'What makes it the case that something has moral standing?',120:'The shared assumption',123:'Argument against the first-order relational view',126:'Boltzmann Badger is in pain',129:'Mixed disjunctive views',133:'Peter N. Salib · coauthor slide',138:'What determines an agent’s stake?',141:'Copying: the survival problem',144:'The general framework',146:'Law without survival',153:'Understanding in LLMs · handout photograph',155:'Servants, Parents, or Angels?',165:'A menu of models',171:'Four grades of autonomy',172:'Four grades of autonomy',187:'Bottom up and top down',221:'Thanks for listening'}
for s in slides:
 if s['album_index'] in titles:s['title']=titles[s['album_index']]
# Editorial assets and source transcriptions remain separately editable.
reading='# The notes, explained\n\nEditorial study guide, not a transcript. Each number refers to a PDF page.\n\n'
for n in notes:
 reading+=f'## PDF page {n["page"]}: {n["title"]}\n\nAuthor: {n["author"]}. Theme: {n["theme"]}.\n\n### Summary\n\n{n["summary"]}\n\n'
 for item in n['notes']:reading+=f'### Source {item["ref"]}: {item["title"]}\n\n{item["explanation"]}\n\n'
 reading+=f'### Everyday example (editorial)\n\n{n["example"]}\n\n### Open question\n\n{n["question"]}\n\n'
(root/'content/reading-guide.md').write_text(reading.rstrip()+'\n')
summary='# Workshop synthesis\n\n'+guide['intro']+'\n\n'
for t in guide['takeaways']:summary+=f'## {t["title"]}\n\n{t["text"]} Sources: PDF pages '+', '.join(map(str,t['pages']))+'.\n\n'
summary+='## A real disagreement, not a consensus\n\nBoghossian’s response defends a factual question about sensations. Sharadin’s response asks what our language does and how decisions can be guided by practical reasons. Their objections pull in different directions. The longer Boghossian handout examines understanding rather than simply asking whether an AI is conscious. The source packet does not give a complete record of the workshop or establish that its participants agreed.\n\n## What is checked\n\nAll twelve PDF scans were visually inspected and obvious OCR errors corrected. Pages 3–4 have clipped text. The product 5,647 × 8,911 was independently checked as 50,320,417. Reported model outputs and model labels are preserved as source claims, without a new model experiment.\n'
(root/'content/summary.md').write_text(summary.rstrip()+'\n')
glossary='# Words, unpacked\n\nEditorial definitions for this workshop.\n\n'+''.join(f'## {t}\n\n{x}\n\nPDF pages: '+', '.join(map(str,p))+'.\n\n' for t,x,p in guide['glossary'])
(root/'content/glossary.md').write_text(glossary.rstrip()+'\n')
session_text='# Across two days\n\nSource-linked reading orientations, not full spoken transcripts.\n\n'
for s in guide['sessions']:session_text+=f'## Day {s["day"]}: {s["title"]}\n\n{s["speaker"]} · Album {s["range"][0]}–{s["range"][1]}\n\n{s["summary"]}\n\nSource basis: {s["basis"]}\n\n'
(root/'content/sessions.md').write_text(session_text.rstrip()+'\n')
index='# Shared album: 222-item inventory\n\nRetrieved 2026-11-08 from https://photos.app.goo.gl/u8Toc2MdmTSncuYq6\n\nImages are reduced-resolution study copies. Includes duplicate slides, handouts, snapshots, and still preview images of video items. OCR below is UNVERIFIED machine text; no spoken audio is transcribed here. Index labels are editorial.\n\n'
for s in slides:
 text=f'# Album {s["album_index"]:03}: {s["title"]}\n\nTime: {s["captured_at"]}\nSession: {s["session_title"]}\nPhoto ID: {s["photo_id"]}\nImage: {s["image"]}\nSource image: {s["image_url"]}\n\nStatus: UNVERIFIED machine text from photographed material or a video preview. Inspect source image.\n\n```text\n{s["ocr"]}\n```\n'
 (root/f'transcripts/slides/{s["id"]}.md').write_text(text)
 index+=text+'\n---\n\n'
(root/'transcripts/slides-index.md').write_text(index)
# Public-data source tree for Sites: private content is never copied here.
assets=site/'assets';(assets/'notes').mkdir(parents=True,exist_ok=True);(assets/'slides').mkdir(exist_ok=True)
for p in (root/'sources/notes/pages').glob('*.jpg'):shutil.copy2(p,assets/'notes'/p.name)
for p in (root/'sources/slides/images').glob('*.jpg'):shutil.copy2(p,assets/'slides'/p.name)
shutil.copy2(root/'sources/workshop/programme.jpg',assets/'programme.jpg')
downloads=site/'downloads';downloads.mkdir(exist_ok=True)
shutil.copy2(root/'sources/notes/CCF11082026.pdf',downloads/'workshop-notes.pdf')
for p in (root/'transcripts/notes').glob('*.md'):shutil.copy2(p,downloads/p.name)
for slug in ['boghossian-on-shanahan','sharadin-on-shanahan','boghossian-understanding','slides-index']:shutil.copy2(root/f'transcripts/{slug}.md',downloads/f'{slug}.md')
for file in ['reading-guide','summary','glossary','sessions']:shutil.copy2(root/f'content/{file}.md',downloads/f'{file}.md')
shutil.copy2(root/'sources/slides/manifest.json',downloads/'manifest.json')
# Attach visually reviewed slide transcriptions without overwriting raw OCR.
review_dir=root/'content/slide-review'
for review in sorted(review_dir.glob('*.md')) if review_dir.exists() else []:
 review_text=review.read_text()
 for match in re.finditer(r'^## (\d{3}) — ([^\n]+)\n(.*?)(?=^## \d{3} — |\Z)',review_text,re.M|re.S):
  number=int(match.group(1)); section=match.group(3)
  transcription=re.search(r'### Visible text\n(.*?)(?=\n### In everyday language)',section,re.S)
  explanation=re.search(r'### In everyday language\n(.*)',section,re.S)
  if transcription and explanation:
   slides[number-1]['review']={'transcription':transcription.group(1).strip(),'explanation':explanation.group(1).strip(),'source':review.name,'model':'GPT-6.1 Terra high'}
# Publish the independently maintained, clearly marked review documents.
for review in sorted(review_dir.glob('*.md')) if review_dir.exists() else []:
 shutil.copy2(review,downloads/review.name)
data=dict(notes=notes,guide=guide,slides=slides)
(site/'data.js').write_text('window.NOTEBOOK = '+json.dumps(data,ensure_ascii=False).replace('</','<\\/')+';\n')
for output in ['dist','dist-local']:
 target=site/output;target.mkdir(exist_ok=True)
 (target/'.nojekyll').touch()
 for name in ['index.html','styles.css','app.js','data.js']:shutil.copy2(site/name,target/name)
 for name in ['assets','downloads']:shutil.copytree(site/name,target/name,dirs_exist_ok=True)
if (root/'private/hawthorne/guide.json').exists():
 h=json.loads((root/'private/hawthorne/guide.json').read_text());data['hawthorne']=h;data['hawthorneTranscript']=(root/'private/hawthorne/transcript.md').read_text()
 local=site/'dist-local';(local/'data.js').write_text('window.NOTEBOOK = '+json.dumps(data,ensure_ascii=False).replace('</','<\\/')+';\n')
 hg=f'# {h["title"]}\n\n{h["restriction"]}\n\n{h["source"]}\n\n## Summary\n\n{h["summary"]}\n\n'
 for x in h['sections']:hg+=f'## {x["time"]}: {x["title"]}\n\n{x["explanation"]}\n\nIllustration (editorial): {x["example"]}\n\nOpen question: {x["question"]}\n\n'
 hg+='## Connections\n\n'+'\n\n'.join(h['connections'])+'\n'
 (root/'private/hawthorne/reading-guide.md').write_text(hg)
 shutil.copytree(root/'private/hawthorne',local/'private/hawthorne',dirs_exist_ok=True)
# Machine-readable audit summary without private transcript contents.
report={'pdf_pages':len(notes),'handouts':3,'album_items':len(slides),'plain_language_notes':sum(len(n['notes']) for n in notes),'glossary_terms':len(guide['glossary']),'source_pdf_sha256':hashlib.sha256((root/'sources/notes/CCF11082026.pdf').read_bytes()).hexdigest(),'private_material_in_hosted_build':False,'slide_ocr_status':'unverified machine extraction; photos and preview frames only'}
(root/'sources/processing-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2));print('Built site/dist (hosted) and site/dist-local (local with private talk).')
