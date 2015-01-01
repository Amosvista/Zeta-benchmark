#!/usr/bin/env python
# encoding: utf-8
import sys
import subprocess as sub
import json
import re
store=open(sys.argv[1],'w')
total=sys.argv[2]
if len(sys.argv)>3:
    hostPath=sys.argv[3]
else:
    hostPath='http://127.0.0.1:3000/'
#url=['index','str','json','read','write','chain']
#cocurrency=[8,16,32,64,128,256]
url=['str'];cocurrency=[8]
result=dict.fromkeys(url,{})
def parseAB(src,dst):
    src=src.split('\n')
    pattern=re.compile(r'\d+\.{0,1}\d{0,10}')
    for i in range(15,len(src)-10):
        if(src[i].count(':')==0):
            continue
        tmp=src[i].split(':')
        key=tmp[0]
        data=pattern.findall(tmp[1])
        if(len(data)>1):
            dst[key]=[]
            for j in data:
                dst[key]=dst[key]+[float(j)]
        else:
            dst[key]=float(data[0])
        dst['percentage']={}
    for i in range(len(src)-10,len(src)):
        tmp=pattern.findall(src[i])
        if(len(tmp)!=2):
            continue
        dst['percentage'][int(tmp[0])]=int(tmp[1])
    return dst

for item in url:
    for c in cocurrency:
        child=sub.check_output('ab -n '+total+' -c '+str(c)+' '+hostPath+item,shell=True)
        result[item][c]={}
        parseAB(child,result[item][c])

store.write(json.dumps(result));
