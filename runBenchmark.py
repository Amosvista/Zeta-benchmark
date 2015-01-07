#!/usr/bin/env python
# encoding: utf-8


import draw
import parseData as d

data = d.bmData()


def plt(title, ylabel, edata, zdata):
    draw.draw(title, 'concurrency', data.concurrency, ylabel, edata, zdata)


plt('95% percent latency bound on [db write]', 'Time(ms)',
    data.get('express', 'write', 'percentage'),
    data.get('zeta', 'write', 'percentage'))
