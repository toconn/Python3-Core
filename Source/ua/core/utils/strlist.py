from ua.core.utils import listutils
from ua.core.utils import strutils

class StrList:
    
    def __init__(self, strings):
        
        self._strings = strings
        
    def __repr__(self):
        
        return ", ".join(self._strings)

    def bool(self, index, default=False):
        
        value = self.value(index)
        
        if value is None:
            value = default
        elif strutils.startswith_ignore_case(value, 'y'):
            return True
        elif strutils.startswith_ignore_case(value, 't'):
            return True
        else:
            return False

    def value(self, index):
        
        if self._is_inbounds(index):
            return self._strings[index]
        else:
            return None
    
    def _is_inbounds(self, index):
        
        return index < listutils.count(self._strings)