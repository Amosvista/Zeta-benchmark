#!/usr/bin/env python
# encoding: utf-8

import subprocess as sub
from draw import *
import parseData as d


sub.call('./benchmark.py express 10000')
sub.call('./benchmark.py zeta 10000')
data = d.bmData()


def plt(title, ylabel, edata, zdata):
    draw(title, 'concurrency', data.concurrency, ylabel, edata, zdata)


plt('95% percent latency bound on [db write]', 'Time(ms)',
    data.get('express', 'write', 'percentage'),
    data.get('zeta', 'write', 'percentage'))
