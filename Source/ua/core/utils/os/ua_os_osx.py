import os
from . import os_const
from ua.core.utils.os.ua_os_base import UaOsBase

class UaOsOsx (UaOsBase):
    
    FILE_SEPARATOR = os_const.FILE_SEPARATOR_LINUX
    NEWLINE = os_const.NEWLINE_LINUX
    OS_NAME = 'OS X'
    PATH_SEPARATOR = os_const.PATH_SEPARATOR_LINUX
    USER_DIR_VAR = 'HOME'
    USER_APP_SUBDIR = 'Library/Application Support'

    def file_separator(self):
        return UaOsOsx.FILE_SEPARATOR

    def is_linux(self):
        return False

    def is_osx(self):
        return True

    def is_windows(self):
        return False

    def newline(self):
        return UaOsOsx.NEWLINE

    def os_name(self):
        return UaOsOsx.OS_NAME

    def normalize_path(self, path):
        
        if path:
            path = path \
                .replace (os_const.FILE_SEPARATOR_WINDOWS, UaOsOsx.FILE_SEPARATOR) \
                .replace (os_const.PATH_SEPARATOR_WINDOWS, UaOsOsx.PATH_SEPARATOR)
            
        return path
    
    def normalize_paths(self, paths):
        return [self.normalize_path(path) for path in paths]

    def path_separator(self):
        return UaOsOsx.PATH_SEPARATOR

    def user_app_dir(self):
        return os.path.join(self.user_dir(), UaOsOsx.USER_APP_SUBDIR)

    def user_dir(self):
        return os.getenv(UaOsOsx.USER_DIR_VAR)
