#!/usr/bin/env python
# encoding: utf-8
# test one frame work each time

import sys
import subprocess as sub
import json
import re
import os
import time


abMethods = {}
abMethods[''] = ''
abMethods['index'] = ''
abMethods['str'] = ''
abMethods['json'] = ''
abMethods['read'] = ''
abMethods['chain'] = ''
abMethods['write'] = ' '

print('Example to use it:' +
      'benchmark.py express 10000 127.0.0.1:3000/ method 8')

if len(sys.argv)-1 < 1:
    store = open(os.getcwd() + '/framework-Name.json', 'w+')
else:
    store = open(sys.argv[1]+'.json', 'w+')  # file to save benchmark result

if len(sys.argv)-1 < 2:
    total = 10000  # iteration number
else:
    total = sys.argv[2]

if len(sys.argv)-1 < 3:
    hostPath = 'http://127.0.0.1:3000/'  # request url
else:
    hostPath = sys.argv[3]

if len(sys.argv)-1 < 4:
    url = ['', 'str', 'json', 'read', 'write', 'chain']  # methods to test
else:
    if sys.argv[4] in abMethods:
        url = [sys.argv[4]]
    else:
        url = ['', 'str', 'json', 'read', 'write', 'chain']  # methods to test

if len(sys.argv) < 5:
    cocurrency = [8, 16, 32, 64, 128, 256]  # currency level
else:
    cocurrency = [sys.argv[5]]


result = {u: {} for u in url}  # each method a dict


def parseAB(src, dst):  # parse the ab result into dst
    src = src.split('\n')
    pattern = re.compile(r'\d+\.{0,1}\d{0,10}')
    for i in range(15, len(src)-10):
        if(src[i].count(':') == 0):
            continue
        tmp = src[i].split(':')
        key = tmp[0]
        data = pattern.findall(tmp[1])
        if not data:
            continue
        elif(len(data) > 1):
            dst[key] = []
            for j in data:
                dst[key] = dst[key]+[float(j)]
        else:
            dst[key] = float(data[0])
        dst['percentage'] = {}
    for i in range(len(src)-10, len(src)):
        tmp = pattern.findall(src[i])
        if(len(tmp) != 2):
            continue
        dst['percentage'][int(tmp[0])] = int(tmp[1])
    return dst

for item in url:
    for c in cocurrency:
        print('Now we are testing on Url: ' + hostPath + item
              + ', with cocurrency:' + str(c))
        child = sub.check_output(
            'ab -k -n ' + str(total) + ' -c ' + str(c) + abMethods[item] + ' '
            + hostPath + item, shell=True, close_fds=True)

        result[item][c] = {}
        parseAB(child, result[item][c])
        time.sleep(5)

print('Writing result into file')
store.write(json.dumps(result))
store.close()
print('Done')
