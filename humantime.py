# /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ : uzjY
# __time__ : 16-12-18
# __version__ : 0.0.2

'''
先把简单的完成，流程走一遍，再实现更多api之类的吧
'''

import time
import datetime
import dateparser
import dateutil

from dateutil.relativedelta import relativedelta

from .util import is_timestamp, is_str
from .factory import TimeFactory

WEEKDAY = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
ABS_KEYS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
REL_KEYS = ['years', 'months', 'days', 'hours', 'minutes', 'seconds', 'weeks', 'quarters']

_factory = TimeFactory()

class HumanTime(object):
    # in arrow, they used factory method to create Arrow class.
    def __init__(self, year, month=1, day=1, hour=0, minute=0, second=0, microsecond=0, tzinfo=None):
        # progress the tzinfo

        self._timeinfo = datetime.datetime(year, month, day, hour, minute, second, microsecond, tzinfo)
        self._timestamp = self._timeinfo.timestamp()
    
    def between(self, value):
        if isinstance(value, (HumanTime, datetime.datetime)):
            return self.__sub__(value)
        elif isinstance(value, (float, int)):
            return self.__sub__(datetime.datetime.fromtimestamp(value))
        elif isinstance(value, str):
            pass
    
    # Firstly, I think i can not get a better replace() than Arrow.replace
    # Now, there is a better way...still need test
    # The Arrow's author is know this way.
    def replace(self, **kw):
        tmp_kw = {}
        for key, value in kw.items():
            if key in ABS_KEYS or key in REL_KEYS:
                tmp_kw[key] = value
        tmp_kw.setdefault('months', 0)
        tmp_kw['months'] += tmp_kw.pop('quarters', 0) * 3
        self._timeinfo += relativedelta(**tmp_kw)

    def __str__(self):
        return '< H-Time {}>'.format(str(self._timeinfo).split('.')[0])

    def __repr__(self):
        return self.__str__()

    def __sub__(self, other):
        if isinstance(other, HumanTime):
            tmp = self._timeinfo - other._timeinfo
        elif isinstance(other, datetime.datetime):
            tmp = self._timeinfo - other

        if tmp.total_seconds() > 0:
            gt = '+'
        elif tmp.total_seconds() < 0:
            gt = '-'
        elif int(tmp.total_seconds()) == 0:
            return '<H-time Two time is equal>'
        seconds = abs(tmp.total_seconds())
        return '<H-time {}{} days, {} hours, {} minutes, {} seconds>'.format(gt, \
            seconds // 86400, \
            seconds % 86400 // 3600, \
            seconds % 86400 % 3600 // 60, \
            seconds % 86400 % 3600 % 60)

        raise TypeError()

    def __hash__(self):
        return self._timeinfo.__hash__()
    
    # the list of cmp functions is learn from arrow
    def _cmperror(self, other):
        raise TypeError('can not compare the type between {} and {}'.format(type(self), type(other)))

    def __eq__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return False
        if isinstance(other, datetime.datetime):
            return self._timeinfo == other
        if isinstance(other, HumanTime):
            return self._timeinfo == other._timeinfo

    def __ne__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return True
        if isinstance(other, datetime.datetime):
            return self._timeinfo != other
        if isinstance(other, HumanTime):
            return self._timeinfo != other._timeinfo

    def __lt__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return self._cmperror(other)
        if isinstance(other, datetime.datetime):
            return self._timeinfo < other
        if isinstance(other, HumanTime):
            return self._timeinfo < other._timeinfo

    def __le__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return self._cmperror(other)
        if isinstance(other, datetime.datetime):
            return self._timeinfo <= other
        if isinstance(other, HumanTime):
            return self._timeinfo <= other._timeinfo

    def __gt__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return self._cmperror(other)
        if isinstance(other, datetime.datetime):
            return self._timeinfo > other
        if isinstance(other, HumanTime):
            return self._timeinfo > other._timeinfo

    def __ge__(self, other):
        if not isinstance(other, (datetime.datetime, HumanTime)):
            return self._cmperror(other)
        if isinstance(other, datetime.datetime):
            return self._timeinfo >= other
        if isinstance(other, HumanTime):
            return self._timeinfo >= other._timeinfo

    @property
    def timestamp(self):
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if not isinstance(value, (float, int)):
            raise ValueError('The timestamp must be a integer!')
        if value < 0 :
            raise ValueError('The timestamp must large than zero!')
        self._timestamp = value
        self._timeinfo = datetime.datetime.fromtimestamp(self._timestamp)

    # not need?
    @property
    def time(self):
        return self._now_time()

    @time.setter
    def time(self, *args, **kw):
        ''' 
        用factorymethod来做的话
        这里应该通过向factory传入相关数据
        然后返回一个HumanTime类，再将这个类的数据传入
        '''
        date = datetime.fromtimestamp(_factory.get(*args, **kw)._timestamp)
        self._timeinfo = date
        self._timestamp = date.timestamp()

    @property
    def weekday(self):
        return WEEKDAY[self._timeinfo.weekday()]

    # 这里直接修改了对象时间
    # 不应该这么改 回头用api返回吧
    @property
    def yesterday(self):
        tmp = self._timeinfo
        return HumanTime(tmp.year, tmp.month, tmp.day-1, tmp.hour, tmp.minute, tmp.second, tmp.microsecond)

    @property
    def tomorrow(self):
        tmp = self._timeinfo
        return HumanTime(tmp.year, tmp.month, tmp.day+1, tmp.hour, tmp.minute, tmp.second, tmp.microsecond)

    def _now_time(self):
        print(str(self._timeinfo).split('.')[0])

    @classmethod
    def now(cls, tzinfo=None):
        utc = datetime.datetime.utcnow()
        dt = utc.astimezone(dateutil_tz.tzlocal() if tzinfo is None else tzinfo)
        return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.microsecond, dt.tzinfo)

    @classmethod
    def when(cls, value, tzinfo='UTC'):
        if is_str(value):
            dt = dateparser.parse(value, settings={})
        if dt is not None:
            return cls(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, dt.microsecond)
        else:
            raise ValueError('Your input datetime is invalid.')
