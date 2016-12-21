# /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ : uzjY
# __time__ : 16-12-18
# __version__ : 0.0.1

import time
import datetime
import dateutil

WEEKDAY = ['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun']

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
        if 'week' in kw.keys():
            self.week = kw['week']
    
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
    return HumanTime().time
