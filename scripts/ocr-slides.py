"""Search OCR for photographed slides, using local contrast to recover faint text.
Machine output is not a verified transcription. Video items are preview frames only.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from PIL import Image,ImageOps,ImageFilter,ImageChops
import subprocess,tempfile
root=Path(__file__).resolve().parent.parent
out=root/'sources/slides/ocr-enhanced';out.mkdir(exist_ok=True)
def ocr(p):
 target=out/p.stem
 if not target.with_suffix('.txt').exists():
  im=Image.open(p).convert('L'); im=im.resize((im.width*2,im.height*2))
  bg=im.filter(ImageFilter.GaussianBlur(14))
  diff=ImageChops.subtract(bg,im,offset=128)
  binary=diff.point(lambda v:0 if v>138 else 255)
  with tempfile.NamedTemporaryFile(suffix='.png') as temp:
   binary.save(temp.name)
   subprocess.run(['tesseract',temp.name,str(target),'-l','eng','--psm','11'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
 return p.stem
with ThreadPoolExecutor(max_workers=4) as pool:
 for i,_ in enumerate(pool.map(ocr,sorted((root/'sources/slides/images').glob('*.jpg'))),1):
  if i%25==0:print(f'{i} photos OCR processed',flush=True)
