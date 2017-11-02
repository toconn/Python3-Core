from datetime import datetime
import time

def datetime_now():
    return datetime.today()

def epoch_seconds_now():
    return time.time()

def is_datetime_within (actual_datetime, test_datetime, test_time_range):
    return abs(actual_datetime - test_datetime) <= test_time_range
