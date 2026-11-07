"""Apply scan-checked OCR corrections while preserving source wording and errors."""
from pathlib import Path
import re,json
root=Path(__file__).resolve().parent.parent
fixes={
1:{'\n. What exactly':'\n2. What exactly','3. Ian say:':'3. I can say:','has ¢hat.':'has that.','it’s /ike':'it’s like','se/-intimating':'self-intimating','ii, You':'ii. You','tii, You':'iii. You','6.—Given-this':'6. Given this','\ni That is':'\ni. That is'},
2:{'iii, Witt':'iii. Witt','a. Ihave':'a. I have','by *':'by','\nSs.':'\nS.','ii, A week':'ii. A week','epistemological claim.—':'epistemological claim –','ii, No one':'ii. No one','\n*\n':''},
3:{'« ':'• ','¢ ':'• ','+ ':'• ','* —':'—','of a very strange sort, utterly -':'of a very strange sort, utterly','~ When':'— When'},
4:{'everything as it is.”s”':'everything as it is”','« ':'* ','Quast-Realism':'Quasi-Realism','more than his':'more than this','|...|':'[...]','everything as it i\n':'everything as it is.”\n','not lacical hint not hevond reaenn either':'not logical, but not beyond reason either.'},
5:{'NYU :':'NYU','The Question _ 5':'The Question','super-sophisticated, _':'super-sophisticated,','it, Desire':'ii. Desire','infend':'intend','iti. Reason':'iii. Reason','Alton':'Act on','‘e/ling':'telling','answet':'answer','fu//':'full','Als instantiate':'AIs instantiate','wnderstanding':'understanding','LLMs ate':'LLMs are','and /':'and','zmpressive':'impressive','i, LLMs':'i. LLMs'},
6:{'ii. Therefore':'ii. Therefore [source numbering; follows i–ii on preceding page]','wnderstand':'understand','exp/ained':'explained','s/rongest':'strongest'},
7:{'of understanding i is':'of understanding is','sure hey believe':'sure they believe','\n* some fact':'\nsome fact','just ove utterance':'just one utterance','éuference fo the best explanation':'inference to the best explanation'},
8:{'stare cortectly':'state correctly','a// possible':'all possible','70°?':'70%?','\n: But':'\nBut','We\nate full':'We\nare full','ru/e':'rule','doing. ,':'doing.','p/us':'plus','general\ntule':'general\nrule','exp/ained':'explained','‘green.’ :':'‘green.’','ra/iona/':'rational'},
9:{'Thete':'There','IT assume':'I assume','“consciousness.':'consciousness.','easy Cases':'easy cases','\n“\n':'\n',r'\ (6647 \times 8911 = \boxed {50,322,417}\)':r'\(5647 \times 8911 = \boxed{50,322,417}\)'},
11:{'@ understanding':'■ understanding','™@ being':'■ being','\n: it does':'\nit does','Iam doubtful':'I am doubtful','ouslier':'outlier','errors #s eliminated':'errors is eliminated','cases. ss':'cases.'},
12:{'‘The usual':'The usual','\ni networks.':'\nnetworks.','assessabilty':'assessability','as a treason':'as a reason',"That's S. till Adequate?":"That’s Still Adequate?"}}
# Page 10 has text boxes missed by OCR; transcribed directly from the scan.
page10='''This answer is incorrect.

I asked whether it was using a dedicated calculator or generating answers using the model itself?
– No.

It added:

    I can use external computational tools. In this environment, I have access to Python, which can perform exact integer arithmetic. Had I used Python to multiply 5,647 by 8,911, that would have involved an actual arithmetic computation executed outside the language model.

    Without such a tool, accuracy is not guaranteed. Language models can make arithmetic mistakes, especially with large numbers, because their learned computational procedures aren't necessarily as systematic or reliable as conventional algorithms.

Interestingly, in the course of answering this question about method, it discovered that it had given the wrong answer.

    There's also a revealing detail: my previous answer was incorrect.

    The correct result is:
    5647 × 8911 = 50,319,417

    I had given 50,322,417.

Interestingly, this answer, too, is incorrect. It continued:

    This raises precisely the philosophical question you've been exploring: whether a neural network that develops an internal procedure for multiplication should count as grasping the rule of multiplication, even if its implementation is less reliable than that of a classical computer.

I said: actually, the correct answer is 50,320,417. ChatGPT6 responded:

    You're quite right.

    5647 × 8911 = 50,320,417

    My first answer was wrong, and so was my attempted correction. Your answer is correct.
    This is a particularly striking illustration of the difference between generating plausible arithmetic answers and reliably executing an arithmetic algorithm.

It’s very plausible that if these models really had an understanding of what they’re being asked, there would be no mistakes of this type.

Saying 9.11 is greater than 9.9 on the grounds that 11 is bigger than 9, if said by a child, would show that grasp of the concept of decimal notation had not yet snapped into place.

And the same goes for the multiplication case.
'''
for n in range(1,13):
 t=(root/f'sources/notes/ocr/page-{n:02}.txt').read_text().replace('\x0c','').strip()
 for a,b in fixes.get(n,{}).items():t=t.replace(a,b)
 if n==10:t=page10
 if n==3:t+='\n\n[Source text is clipped at the bottom edge; the next scan begins mid-sentence. Missing words have not been reconstructed.]'
 if n==4:t=t.replace('not logical, but not beyond reason either.','not logical, but not beyond reason either. [Bottom line partly clipped in scan; reading uncertain.]')
 title='Comments on Shanahan — Paul Boghossian' if n<3 else ('Comments on Shanahan — Nate Sharadin' if n<5 else 'Understanding in Large Language Models — Paul Boghossian')
 header=f'# PDF page {n}: {title}\n\nSource: `CCF11082026.pdf`, PDF page {n}.\nStatus: OCR-assisted transcription checked against the scan; layout and emphasis simplified. Original wording and errors retained. Refer to scan for quotation.\n\n'
 (root/f'transcripts/notes/page-{n:02}.md').write_text(header+t+'\n')
for slug,a,b,title in [('boghossian-on-shanahan',1,2,'Comments on Shanahan — Paul Boghossian'),('sharadin-on-shanahan',3,4,'Comments on Shanahan — Nate Sharadin'),('boghossian-understanding',5,12,'Understanding in Large Language Models — Paul Boghossian')]:
 text='# '+title+'\n\n'+ '\n\n---\n\n'.join((root/f'transcripts/notes/page-{i:02}.md').read_text() for i in range(a,b+1))
 (root/f'transcripts/{slug}.md').write_text(text)
print('Prepared 12 page transcripts and 3 handout transcripts. Arithmetic check:',5647*8911)
