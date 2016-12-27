#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

'''
在arrow里，他的util是用来一些用来judge的函数api
例如isstr, is_timestamp, total_seconds
'''
from __future__ import absolute_import

import sys

version = '{}.{}.{}'.format(*sys.version_info[:3])

def is_timestamp(value):
    # True, False 可以被float() 转化为1.0， 0.0
    if type(value) == bool:
        return False
    try:
        float(value)
        return True
    except:
        return False

# 2.7 中有basestring, 包含了str和unicode
# 3.+ 中只有str
try:
    basestring
    def is_str(value):
        return isinstance(value, basestring)
except NameError:
    def is_str(value):
        return isinstance(value, str)
        

__all__ = ['is_timestamp', 'is_str']
