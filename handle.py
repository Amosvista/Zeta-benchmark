#!/usr/bin/env python
# encoding: utf-8

import sys
import json

basePath=''
frame=['express']
data={}

for f in frame:
    data[f]=json.loads(open(basePath+f+'.json','r').read())
url=data[frame[0]].keys()
cocurrency=data[frame[0]][url[0]].keys()
keyList=data[frame[0]][url[0]][cocurrency[0]].keys()
print 'you can get these key:   '+str(keyList)
compare=dict.fromkeys(frame,dict.fromkeys(url,{}))
for f in frame:
    for u in url:
        for k in keyList:
            dataType=type(data[f][u][cocurrency[0]][k])
            if dataType==int or dataType==float:
                tmp=[]
                for c in cocurrency:
                    tmp=tmp+[dataType(data[f][u][c][k])]
                compare[f][u][k]=tmp
            elif dataType==dict:
                percent=data[f][u][cocurrency[0]][k].keys()
                tmp=dict.fromkeys(percent,[])
                for p in percent:
                    for c in cocurrency:
                        tmp[p]=tmp[p]+[data[f][u][c][k][p]]
                compare[f][u][k]=tmp
            elif dataType==list:
                sta=['min','mean','sd','median','max']
                tmp=dict.fromkeys(sta,[])
                for i in range(len(sta)):
                    for c in cocurrency:
                        s=sta[i]
                        tmp[s]=tmp[s]+[data[f][u][c][k][i]]
                compare[f][u][k]=tmp

def get(f,u,k,index=None):
    if k=='percentage':
        if not index:
            return compare[f][u][k]['95']
        else:
            return compare[f][u][k][str(index)]
    elif type(compare[f][u][k])==dict:
        if not index:
            return compare[f][u][k]['mean']
        else:
            return compare[f][u][k][index]
    else:
        return compare[f][u][k]





