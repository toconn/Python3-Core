from datetime import datetime
from enum import Enum

from ua.core.enums.status import Status

class MeterStatus(Enum):
    STARTED = 0
    STOPPED = 1

class MeteredEvent:
    """ 
        Created with CodeCrank.io
    """

    def __init__(self):

        self.event_id = 0
        self.component_name = ""
        self.component_action = ""
        self.parameters = ""
        self.user_id = 0
        self.result_status = None

        self.reset()
        self.start()

    def __repr__(self):

        return "MeteredEvent [" + \
            "id=" + (str(self.id) if self.id is not None else "[None]") + \
            ", component_name=" + (self.component_name if self.component_name is not None else "[None]") + \
            ", component_action=" + (self.component_action if self.component_action is not None else "[None]") + \
            ", parameters=" + (self.parameters if self.parameters is not None else "[None]") + \
            ", user_id=" + (str(self.user_id) if self.user_id is not None else "[None]") + \
            ", duration_ms=" + (str(self.duration_ms) if self.duration_ms is not None else "[None]") + \
            "]"

    def reset(self):
        
        self.start_date_time = None
        self.duration_delta_time = 0.0
        
        self._status = MeterStatus.STOPPED
        self._start_clock_time = None

    def start(self):
        
        if self._status != MeterStatus.STARTED:

            self.start_date_time = datetime.today()
            # self._start_clock_time = time.time()
            self._status = MeterStatus.STARTED
            
    def stop(self, result_status = Status.OK):
        
        stop_date_time = datetime.today()
        self._status = MeterStatus.STOPPED
        
        self.result_status = result_status
        self.duration_delta_time = stop_date_time - self.start_date_time
