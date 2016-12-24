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
    if isinstance(t1, HumanTime):
        if isinstance(t2, HumanTime):
            delta = t1._timeinfo - t2._timeinfo
        elif isinstance(t2, datetime.datetime):
            delta = t1._timeinfo - t2
        elif isinstance(t2, (float, int)):
            delta = t1._timeinfo - datetime.datetime.fromtimestamp(t2)

        return '<HumanTime {} days, {} Seconds>'.format(delta.days, delta.seconds)

def now():
    return _htime.now()
    
