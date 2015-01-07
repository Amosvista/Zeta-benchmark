#!/usr/bin/env python
# encoding: utf-8

import json
import os

basePath = os.getcwd() + '/'
data = {}


def getData(fileList):
    for f in fileList:
        filePath = basePath+f+'.json'
        if os.path.isfile(filePath):
            data[f] = json.loads(open(filePath, 'r').read())
            url=data[f].keys()
            cocurrency=data[f][url[0]].keys()
            keyList=data[f][url[0]][cocurrency[0]].keys()
            frame = data.keys()
            chunk=dict.fromkeys(frame,dict.fromkeys(url,{}))
        else:
            continue
    for f in frame:
        for u in url:
            for k in keyList:
                dataType=type(data[f][u][cocurrency[0]][k])
                if dataType==int or dataType==float:
                    tmp=[]
                    for c in cocurrency:
                        tmp=tmp+[dataType(data[f][u][c][k])]
                    chunk[f][u][k]=tmp
                elif dataType==dict:
                    percent=data[f][u][cocurrency[0]][k].keys()
                    tmp=dict.fromkeys(percent,[])
                    for p in percent:
                        for c in cocurrency:
                            tmp[p]=tmp[p]+[data[f][u][c][k][p]]
                    chunk[f][u][k]=tmp
                elif dataType==list:
                    sta=['min','mean','sd','median','max']
                    tmp=dict.fromkeys(sta,[])
                    for i in range(len(sta)):
                        for c in cocurrency:
                            s=sta[i]
                            tmp[s]=tmp[s]+[data[f][u][c][k][i]]
                    chunk[f][u][k]=tmp
    return chunk





def get(chunk, framework, url, abFeature, index=None):
    try:
        if abFeature == 'percentage':
            if not index:
                return chunk[framework][url][abFeature]['95']
            else:
                return chunk[framework][url][abFeature][str(index)]
        elif type(chunk[framework][url][abFeature]) == dict:
            if not index:
                return chunk[framework][url][abFeature]['mean']
            else:
                return chunk[framework][url][abFeature][index]
        else:
            return chunk[framework][url][abFeature]
    except KeyError:
        return 'Not Exist'


class bmData:
    def __init__(self, fileList=['express', 'zeta']):
        """
        parse data
        """
        self.chunk = getData(fileList)

    def get(self, framework, url, abFeature, index=None):
        return get(self.chunk, framework, url, abFeature, index)
