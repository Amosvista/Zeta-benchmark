#!/usr/bin/env python
# encoding: utf-8

import sys
import json
src=open(sys.argv[1],'r')
record=json.loads(src.read())
tmp=record['str']['8']
for key in tmp:
    print key+': '+str(tmp[key])
