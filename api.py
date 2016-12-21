# /usr/bin/env python3
# -*- coding:utf-8 -*-

from . import HumanTime
import datetime
import time

'''
Some api for HumanTime module
In fact, this module could help user use the HumanTime directly, avoid create the HumanTime class.
'''

_htime = HumanTime()

def between(t1, t2):
    pass

def now():
    return _htime.now()
    

