#!/usr/bin/env python3
"""由 tools/tpl.html + ../content/month01.json 生成 index.html，并同步 month01.json。"""
import json, os, shutil
HERE=os.path.dirname(os.path.abspath(__file__)); REPO=os.path.dirname(HERE)
SRC=os.path.join(os.path.dirname(REPO),'content','month01.json')
d=json.load(open(SRC,encoding='utf-8'))
tpl=open(os.path.join(HERE,'tpl.html'),encoding='utf-8').read()
out=tpl.replace('__DATA__', json.dumps(d,ensure_ascii=False).replace('</','<\\/'))
open(os.path.join(REPO,'index.html'),'w',encoding='utf-8').write(out)
shutil.copy(SRC, os.path.join(REPO,'month01.json'))
n=sum(len(i['questions']['L1'])+len(i['questions']['L2'])+1 for i in d['items'])
qz=sum(q['nq'] for q in d.get('quizzes',[]))
empty=[i['id'] for i in d['items'] if not i['text'] and i['source']!='none']
print('index.html %d bytes ｜ 选文 %d（空正文 %s）｜ 周测 %d 套'
      % (len(out), len(d['items']), empty or '无', len(d.get('quizzes',[]))))
print('题目 %d = 三层追问 %d + 第7题 %d + 晨读 %d + 周测 %d'
      % (n+len(d['items'])+len(d['morning'])+qz, n, len(d['items']), len(d['morning']), qz))
