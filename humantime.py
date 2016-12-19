# /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ : uzjY
# __time__ : 16-12-18
# __version__ : 0.0.1

import time
import datetime
import dateutil

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
    def now(self):
        return self._now_time()
