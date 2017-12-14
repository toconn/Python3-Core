import unittest
from datetime import datetime, timedelta
from ua.core.utils import dateutils


TEST_DATE_1 = datetime(2001, 1, 1, 1, 1, 1)         # 1 second
TEST_DATE_1_5 = datetime(2001, 1, 1, 1, 1, 1, 500)  # 1.5 seconds
TEST_DATE_2 = datetime(2001, 1, 1, 1, 1, 2)         # 2 seconds
TEST_DATE_3 = datetime(2001, 1, 1, 1, 1, 3)         # 3 seconds

TEST_DELTA_1_SECOND = timedelta (seconds = 1)


class Test_DateUtils(unittest.TestCase):

    def test_date_outside_range(self):
        self.assertFalse(dateutils.is_datetime_within(TEST_DATE_1, TEST_DATE_3, TEST_DELTA_1_SECOND))

    def test_date_within_range(self):
        self.assertTrue(dateutils.is_datetime_within(TEST_DATE_1, TEST_DATE_1_5, TEST_DELTA_1_SECOND))

    def test_date_self_within_range(self):
        self.assertTrue(dateutils.is_datetime_within(TEST_DATE_1, TEST_DATE_1, TEST_DELTA_1_SECOND))

    def test_date_border_time_within_range(self):
        self.assertTrue(dateutils.is_datetime_within(TEST_DATE_1, TEST_DATE_2, TEST_DELTA_1_SECOND))
        
    def test_week_number_same_date(self):
        self._call_and_test_week_number('2001-01-01', '2001-01-01', 1)

    def test_week_number_next_week(self):
        self._call_and_test_week_number('2001-01-01', '2001-01-08', 2)

    def test_week_number_next_week_2(self):
        self._call_and_test_week_number('2001-01-01', '2001-01-14', 2)

    def _call_and_test_week_number (self, start_date_string, end_date_string, expected):
        actual = dateutils.week_number (dateutils.to_date_from_string (start_date_string), dateutils.to_date_from_string (end_date_string))
        self.assertEquals (expected, actual)


