#! /usr/bin/env python3
#! -*- coding:utf-8 -*-

'''
factory mothod

'''

from .humantime import HumanTime
from .util import is_timestamp, is_str


'''
In here, create and return HumanTime class
And arrow.api create instance of all function in this class
So the module of arrow could use those function directly.
'''
class TimeFactory(object):
    # this __init__ function actually almost not input another type except HumanTime maybe.
    def __init__(self, type=HumanTime):
        self.type = type

    '''
    In arrow, this function is main function to create and return arrow.
    Is this factory method?
    Based the *arg and **kw, return different Arrow class.
    In this way, the Arrow's __init__ could get certain parameter
    Other function want call Arrow's __init__ is easier.
    '''
    def get(self, *args, **kw):
        if len(arg) == 0:
            self._timeinfo = datetime.datetime.now()
            self._timestamp = time.time()
            self.tzinfo = time.timezone
            self.tzname = time.tzname
            return self.type.now()

        if len(arg) == 1:
            value = arg[0]
            if isinstance(value, str):
                # time.strftime 根据传入的format，输出用这个format表示的当前时间
                try:
                    if 'tformat' in kw.keys():
                        self._timeinfo = datetime.datetime.strptime(value, kw['tformat'])
                    else:
                        if '%' in value:
                            self._timeinfo = datetime.datetime.strptime(time.strftime(value), value)
                        else:
                            self._timeinfo = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                    self._timestamp = self._timeinfo.timestamp()
                except e:
                    raise ValueError('Please enter the right time format!')
            elif isinstance(value, (float, int)):
                try:
                    self._timeinfo = datetime.datetime.fromtimestamp(value)
                    self._timestamp = value
                except:
                   pass
            elif isinstance(value, datetime.datetime):
                self._timeinfo = value
                self._timestamp = value.timestamp()
        else:
            try:
                self._timeinfo = datetime.datetime(*arg)
                self._timestamp = self._timeinfo.timestamp()
            except:
                raise ValueError('tuple of arg is error.')

    def utcnow():
        pass

    def now():
        pass
