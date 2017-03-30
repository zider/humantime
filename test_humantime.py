# test for basic function

import pytest
import time
import datetime

import humantime

def test_timestamp():
    s = time.time.now()
    h = humantime.HumanTime(s)
    assert h._timeinfo == datetime.datetime.fromtimestamp(s), 'time equal'



