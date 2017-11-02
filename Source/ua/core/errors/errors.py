class UaException (Exception):

    def __init__(self,*args,**kwargs):
        
        Exception.__init__(self,*args,**kwargs)
        
        # Add messages property:
        
        if args:
    
            if isinstance(args[0], list):
                self.messages = args[0]
                
            elif isinstance (args[0], str):
                self.messages = [args[0]]
                
            else:
                self.messages = []
                
    def messages_as_string(self):
        
        return ' '.join (self.messages)


class AccessDenied (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class FailedValidations (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class InvalidConfig (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class InvalidRequest (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class ItemAlreadyExists (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)
  
  
class ItemNotFound (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class RequestTimedOut (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)


class UserRequestExit (UaException):
    def __init__(self, *args, **kwargs):
        UaException.__init__(self, *args, **kwargs)

