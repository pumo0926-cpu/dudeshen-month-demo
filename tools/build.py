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
print('index.html %d bytes ｜ 选文 %d ｜ 题目 %d = 三层追问 %d + 第7题 %d + 晨读 %d'
      % (len(out), len(d['items']), n+len(d['items'])+len(d['morning']), n, len(d['items']), len(d['morning'])))
