#!/usr/bin/env python
# encoding: utf-8

import json
import os

chunk = None
basePath = os.getcwd() + '/'
data = {}
keyList = None


def getData(fileList):
    chunk = {}
    for f in fileList:
        filePath = basePath+f+'.json'
        if os.path.isfile(filePath):
            data[f] = json.loads(open(filePath, 'r').read())
        else:
            continue
        chunk[f] = {}
        url = data[f].keys()
        for u in url:
            chunk[f][u] = {}
            cocurrency = data[f][u].keys()
            for c in cocurrency:
                keyList = data[f][u][c].keys()
                for k in keyList:
                    dataType = type(data[f][u][c][k])
                    if dataType == int or dataType == float:
                        tmp = []
                        tmp = tmp+[dataType(data[f][u][c][k])]
                    elif dataType == dict:
                        percent = data[f][u][c][k].keys()
                        tmp = dict.fromkeys(percent, [])
                        for p in percent:
                            tmp[p] = tmp[p]+[data[f][u][c][k][p]]

                    elif dataType == list:
                        stas = ['min', 'mean', 'sd', 'median', 'max']
                        tmp = dict.fromkeys(stas, [])
                        for i in range(len(stas)):
                            s = stas[i]
                            tmp[s] = tmp[s]+[data[f][u][c][k][i]]
                    chunk[f][u][k] = tmp
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
