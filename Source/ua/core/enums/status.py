from enum import Enum

class Status (Enum):
    OK = 0
    EXCEPTION = 1
    ACCESS_DENIED = 2
    INVALID_CONFIGURATION = 4
    INVALID_REQUEST = 3
    ITEM_NOT_FOUND = 5
    ITEM_ALREADY_EXISTS = 6
    REQUEST_TIMED_OUT = 7
