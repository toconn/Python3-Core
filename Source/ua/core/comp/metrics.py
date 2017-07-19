from datetime import datetime
import time

class MeteredEvent:
    """ 
        Created with CodeCrank.io
    """

    def __init__(self):

        self.id = 0
        self.component_name = ""
        self.component_action = ""
        self.parameters = ""
        self.user_id = 0
        self.start_date_time = datetime.today()
        self.duration_ms = 0        # Duration in milliseconds
        self.result_status = None
        
        self._start_clock_time = time.time()

    def __repr__(self):

        return "MeteredEvent [" + \
            "id=" + (str(self.id) if self.id is not None else "[None]") + \
            ", component_name=" + (self.component_name if self.component_name is not None else "[None]") + \
            ", component_action=" + (self.component_action if self.component_action is not None else "[None]") + \
            ", parameters=" + (self.parameters if self.parameters is not None else "[None]") + \
            ", user_id=" + (str(self.user_id) if self.user_id is not None else "[None]") + \
            ", duration_ms=" + (str(self.duration_ms) if self.duration_ms is not None else "[None]") + \
            "]"
            
    def stop (self, result_status):
        
        stop_clock_time = time.time()
        
        self.result_status = result_status
        self.duration_ms = 