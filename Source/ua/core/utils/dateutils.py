from datetime import datetime
from datetime import timedelta
import time

DATE_FORMAT = '%Y.%m.%d'
DATE_SEPARATOR = '.'


def datetime_now():
    return datetime.today()

def epoch_seconds_now():
    return time.time()

def is_datetime_within (actual_datetime, test_datetime, test_time_range):
    ''' Determin if the date is within a date range (inclusive check).
    '''
    
    return abs(actual_datetime - test_datetime) <= test_time_range

def to_date_from_string (date_string):
    
    date_string = date_string.replace ('/', DATE_SEPARATOR)
    date_string = date_string.replace ('-', DATE_SEPARATOR)
    
    date_actual = datetime.strptime (date_string, DATE_FORMAT)
    
    return date_actual

def to_date_string (date):
    
    return date.strftime (DATE_FORMAT)


def week_end_date (self, week_start_date):
    ''' Calculate the end date of the week given the start date.
    '''

    timediff = timedelta (days = 6)
    week_end_date = week_start_date + timediff
    
    return week_end_date

def week_number (start_date, end_date):
    ''' Calculates the week number of the given end date from the date
        of the first day of the first week.
    '''
    
    timediff = end_date - start_date
    week_number = 1 + (timediff.days // 7)
    
    return week_number

def week_start_date (self, start_date, week_number):
    ''' Return the start date of the week number given the original
        start date of the first week.
    '''

    timediff = timedelta (days = 7 * (week_number - 1))
    week_start_date = (start_date + timediff).date()
    
    return week_start_date

