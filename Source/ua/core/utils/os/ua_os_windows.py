import os
from . import os_const
from ua.core.utils.os.ua_os_base import UaOsBase

class UaOsWindows (UaOsBase):
    
    FILE_SEPARATOR = os_const.FILE_SEPARATOR_WINDOWS
    NEWLINE = os_const.NEWLINE_WINDOWS
    OS_NAME = 'Windows'
    PATH_SEPARATOR = os_const.PATH_SEPARATOR_WINDOWS
    USER_DIR_VAR = 'HOMEPATH'
    USER_APP_SUBDIR_VAR = 'APPDATA'

    def file_separator(self):
        return UaOsWindows.FILE_SEPARATOR

    def is_linux(self):
        return False

    def is_osx(self):
        return True

    def is_windows(self):
        return False

    def newline(self):
        return UaOsWindows.NEWLINE

    def os_name(self):
        return UaOsWindows.OS_NAME

    def normalize_path(self, path):
        
        if path:
            path = path \
                .replace (os_const.FILE_SEPARATOR_LINUX, UaOsWindows.FILE_SEPARATOR) \
                .replace (os_const.PATH_SEPARATOR_LINUX, UaOsWindows.PATH_SEPARATOR)
            
        return path
    
    def normalize_paths(self, paths):
        return [self.normalize_path(path) for path in paths]

    def path_separator(self):
        return UaOsWindows.PATH_SEPARATOR


    def user_app_dir(self):
        return os.getenv(UaOsWindows.USER_APP_SUBDIR_VAR)

    def user_dir(self):
        return os.getenv(UaOsWindows.USER_DIR_VAR)