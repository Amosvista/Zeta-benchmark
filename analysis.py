#!/usr/bin/env python
# encoding: utf-8
from plot import *
import os
ext = '.png'
path = os.getcwd()+'/img/'


def encap(x):
    return '['+x+']'

url = ['', 'str', 'json', 'read', 'write']
keys = ['percentage',  # 'Time per request',
        'Processing', 'Write errors']
title = {}
label = {}
title['percentage'] = '95% percent latency bound on'
# title['Time per request'] = 'Time taken for each request'
title['Processing'] = 'Mean Processing Time For each request'
title['Write errors'] = 'Error Number'
label['percentage'] = 'Time(s)'
# label['Time per request'] = 'Time(s)'
label['Processing'] = 'Time(s)'
label['Write errors'] = 'Number'

fileName = {}
fileName['percentage'] = '95plb'
fileName['Processing'] = 'mtimeEachReq'
fileName['Write errors'] = 'enun'


def analysis():
    for u in url:
        for k in keys:
            if u == '':
                x = 'sendFile'
            else:
                x = u
            graph = plot(title[k]+encap(x),
                         label[k], u, k)
            graph.savefig(path + fileName[k] + encap(x) + ext)
    raw_input('Press any key to close all the figures')

analysis()
