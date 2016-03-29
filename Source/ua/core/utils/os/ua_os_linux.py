import os
from . import os_const
from ua.core.utils.os.ua_os_base import UaOsBase

class UaOsLinux (UaOsBase):
    
    FILE_SEPARATOR = os_const.FILE_SEPARATOR_LINUX
    NEWLINE = os_const.NEWLINE_LINUX
    OS_NAME = 'Linux'
    PATH_SEPARATOR = os_const.PATH_SEPARATOR_LINUX
    USER_DIR_VAR = 'HOME'
    USER_APP_SUBDIR = '.config'

    def file_separator(self):
        return UaOsLinux.FILE_SEPARATOR

    def is_linux(self):
        return False

    def is_osx(self):
        return True

    def is_windows(self):
        return False

    def newline(self):
        return UaOsLinux.NEWLINE

    def os_name(self):
        return UaOsLinux.OS_NAME

    def normalize_path(self, path):
        
        if path:
            path = path \
                .replace (os_const.FILE_SEPARATOR_WINDOWS, UaOsLinux.FILE_SEPARATOR) \
                .replace (os_const.PATH_SEPARATOR_WINDOWS, UaOsLinux.PATH_SEPARATOR)
            
        return path
    
    def normalize_paths(self, paths):
        return [self.normalize_path(path) for path in paths]

    def path_separator(self):
        return UaOsLinux.PATH_SEPARATOR

    def user_app_dir(self):
        return os.path.join(self.user_dir(), UaOsLinux.USER_APP_SUBDIR)

    def user_dir(self):
        return os.getenv(UaOsLinux.USER_DIR_VAR)
