import platform
from . import UaOsLinux
from . import UaOsOsx
from . import UaOsWindows

from ua.core.utils.os import os_const


def create_ua_os (os_name = None):
    ''' Return the OS utility class for either
            the ua_os name passed in or
            the current ua_os.
    '''
    
    if not os_name:
        os_name = platform.system()
    
    if os_name == os_const.OS_NAME_LINUX:
        ua_os = UaOsLinux()
    elif os_name == os_const.OS_NAME_OSX:
        ua_os = UaOsOsx()
    elif os_name == os_const.OS_NAME_WINDOWS:
        ua_os = UaOsWindows()
    else:
        ua_os = None
    
    return ua_os