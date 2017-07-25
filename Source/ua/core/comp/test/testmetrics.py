import unittest
from datetime import datetime, timedelta
from ua.core.comp.metrics import Meter
from ua.core.enums.status import Status
from time import sleep
from ua.core.utils import dateutils

TEST_TIME_1_SECOND = 1

ACCEPTABLE_TIME_DIFF_SHORT_MILLISECONDS = 10
ACCEPTABLE_TIME_DIFF_SHORT_DELTATIME = timedelta (milliseconds = ACCEPTABLE_TIME_DIFF_SHORT_MILLISECONDS)
ACCEPTABLE_TIME_DIFF_ONE_SECOND_DELTATIME = timedelta (seconds = TEST_TIME_1_SECOND, milliseconds = ACCEPTABLE_TIME_DIFF_SHORT_MILLISECONDS)


class TestMetrics (unittest.TestCase):

    # def setUp(self):
        
        # Nothing to do here

    def test_1_second_start_stop (self):
        
        meter = Meter()
        sleep (1.0)
        meter.stop(Status.OK)
        
        print ("1 seconds Start/Stop Duration: " + str (meter.duration_delta_time))

        self.assertTrue(meter.duration_delta_time <= ACCEPTABLE_TIME_DIFF_ONE_SECOND_DELTATIME, "Metered event took too long.")

    def test_instant_start_stop (self):
        
        meter = Meter()
        meter.stop(Status.OK)
        
        print ("Instant Start/Stop Duration: " + str (meter.duration_delta_time))
        
        self.assertTrue(meter.duration_delta_time <= ACCEPTABLE_TIME_DIFF_SHORT_DELTATIME, "Instant Metered event took too long.")

    def test_start_time (self):
        
        now_date_time = datetime.today()       
        meter = Meter()
        
        self.assertTrue(dateutils.is_datetime_within (meter.start_date_time, now_date_time, ACCEPTABLE_TIME_DIFF_SHORT_DELTATIME))
        
        print ("Start Time: " + str (meter.start_date_time))
