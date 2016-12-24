# /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ : uzjY
# __time__ : 16-12-18
# __version__ : 0.0.1

'''
先把简单的完成，流程走一遍，再实现更多api之类的吧
'''

import time
import datetime
import dateutil

WEEKDAY = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']
ABS_KEYS = ['year', 'month', 'day', 'hour', 'minute', 'second', 'microsecond']
REL_KEYS = ['years', 'months', 'days', 'hours', 'minutes', 'seconds', 'weeks', 'quarters']

class HumanTime(object):
    def __init__(self, value=0, **kw):
        if value == 0:
            self._timeinfo = datetime.datetime.now()
            self._timestamp = time.time()
            self.tzinfo = time.timezone
            self.tzname = time.tzname
        elif isinstance(value, str):
            try:
                if 'tformat' in kw.keys():
                    self._timeinfo = datetime.datetime.strptime(value, kw['tformat'])
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
        self.weekday = self._timeinfo.weekday()
    
    def when(self, day):
        if isinstance(day, str):
            if day == 'yesterday'：
                self.yesterday()
            elif day == 'tomorrow':
                self.tomorrow()
            '''
            # more info example
            elif day == '1 months age':
                pass
            '''
    def between(self, value):
        if isinstance(value, (HumanTime, datetime.datetime)):
            return self.__sub__(value)
        elif isinstance(value, (float, int)):
            return self.__sub__(datetime.datetime.fromtimestamp(value))
        elif isinstance(value, str)
            pass
    
    # Firstly, I think i can not get a better replace() than Arrow.replace
    # Now, there is a better way...still need test
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

    def __sub__(self, other):
        if isinstance(other, HumanTime):
            return self._timeinfo - other._timeinfo
        elif isinstance(other, datetime.datetime):
            return self._timeinfo - other

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

    def _now_time(self):
        print(str(self._timeinfo).split('.')[0])

    @property
    def time(self):
        return self._now_time()

    @time.setter
    def time(self, value, tformat=''):
        if tformat == '':
            self.__init__(value=value)
        else:
            self.__init__(value=value, tformat=tformat)

    @property
    def weekday(self):
        return WEEKDAY[self._timeinfo.weekday()]

    @property
    def yesterday(self):
        tmp = self._timeinfo
        self._timeinfo = datetime.datetime(tmp.year, tmp.month, tmp.day-1, tmp.hour, tmp.minute, tmp.second, t.microsecond)
        return self._now_time()

    @property
    def tomorrow(self):
        tmp = self._timeinfo
        self._timeinfo = datetime.datetime(tmp.year, tmp.month, tmp.day+1, tmp.hour, tmp.minute, tmp.second, t.microsecond)
        return self._now_time()

def now():
    return HumanTime()
