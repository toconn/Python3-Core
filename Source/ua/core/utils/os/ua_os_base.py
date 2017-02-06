import abc
from ua.core.utils import strutils

class UaOsBase:
    ''' Base class for OS utilities.
        Defines basic methods.
        Comments after 'Constants' list expected constants.
    '''

    __metaclass__ = abc.ABCMeta
    
    # Constants
    
    # FILE_SEPARATOR
    # NEWLINE
    # OS_NAME
    # PATH_SEPARATOR

    @abc.abstractmethod
    def file_separator(self):
        pass
    
    @abc.abstractmethod
    def is_linux(self):
        pass
    
    @abc.abstractmethod
    def is_osx(self):
        pass
    
    @abc.abstractmethod
    def is_windows(self):
        pass
    
    def join_path (self, root_dir, file):

        if strutils.ends_with (root_dir, self.file_separator()):
            return root_dir + file
        else:
            return root_dir + self.file_separator() + file

    @abc.abstractmethod
    def newline(self):
        pass
    
    @abc.abstractmethod
    def open_document (self, file_name):
        '''
            Open document in the applicable program.
        '''
        pass

    @abc.abstractmethod
    def os_name(self):
        pass

    @abc.abstractmethod
    def normalize_path(self, path):
        pass

    @abc.abstractmethod
    def normalize_paths(self, paths):
        pass

    @abc.abstractmethod
    def path_separator(self):
        pass
    
    @abc.abstractmethod
    def user_app_dir(self):
        pass

    @abc.abstractmethod
    def user_dir(self):
        pass

