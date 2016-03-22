from . import os_const
from .uaos_base import UaOsBase

class UaOsWindows (UaOsBase):
    
    FILE_SEPARATOR = os_const.FILE_SEPARATOR_WINDOWS
    NEWLINE = os_const.NEWLINE_WINDOWS
    OS_NAME = 'Windows'
    PATH_SEPARATOR = os_const.PATH_SEPARATOR_WINDOWS

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

    def path_separator(self):
        return UaOsWindows.PATH_SEPARATOR