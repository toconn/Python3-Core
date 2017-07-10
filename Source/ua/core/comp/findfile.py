import os
from ua.core.utils import fileutils

class FindFile:

    ''' Search a list of config / user directories to find a file
    
        Priority:

            Current Dir
            App Environment Variable
            User_App_Data_Dir Environment Variable / Subdirectory
            Standard User Data Dir / Subdirectory
            Standard User App Data Dir / Subdirectory
            
        Uses builder pattern to set up.
    '''

    ENV_VAR_USER_APP_DIR = 'User_App_Data_Dir'
    
    def __init__(self, ua_os, debug = False):
        
        self._ua_os = ua_os
        
        self._debug = debug
        self._path_env_var = None
        self._search_current_dir = True
        self._search_user_app_dir = True
        self._search_user_app_dir_env_var = True
        self._search_user_dir = True
        self._subdir_name = None
   
    def path_env_var (self, path_env_var):
        
        self._path_env_var = path_env_var
        return self
    
    def search_current_dir (self, search_current_dir):
        ''' Set whether to search the current directory (true | false).
        '''
        
        self._search_current_dir = search_current_dir
        return self

    def search_user_app_dir (self, search_user_app_dir):
        ''' Set whether to search the standard user app directory (true | false).
        '''
        
        self._search_user_app_dir = search_user_app_dir
        return self

    def search_user_app_dir_env_var (self, search_user_app_dir_env_var):
        ''' Set whether to search the directory set by the user app directory environment variable (true | false).
        '''
        
        self._search_user_app_dir_env_var = search_user_app_dir_env_var
        return self

    def search_user_dir (self, search_user_dir):
        ''' Set whether to search the user directory (true | false).
        '''
        
        self._search_user_dir = search_user_dir
        return self

    def subdir_name (self, subdir_name):
        ''' Set the subdirectory name.
        '''
        
        self._subdir_name = subdir_name
        return self

    def findFirst (self, file_name, subdir_name = None):
        ''' Return the directory containing the file.
            Returns None if not found.
        '''
        actual_dir = None
        
        for dir_name in self._get_search_dirs():
            
            self._print (dir_name)
            
            if fileutils.is_dir_and_file_exists(dir_name, file_name):
                
                self._print ('Found')
                actual_dir = dir_name
                break
            
        return actual_dir
    
    def findAll (self, file_name, subdir_name = None):
        ''' Return the directories containing the file.
            Returns an empty if not found.
        '''
        actual_dir_list = []
        
        for dir_name in self._get_search_dirs():
            
            self._print (dir_name)
            
            if fileutils.is_dir_and_file_exists(dir_name, file_name):
                
                self._print ('Found')
                actual_dir_list.append (dir_name)
            
        return actual_dir_list
    
    def _get_dir_subdir (self, dir_name):
        ''' Correctly concatenates the pre-set subdirectory name to the directory.
        '''
        
        if self._subdir_name is not None:
            dir_name = os.path.join (dir, self._subdir_name)
        #else:
            # No subdirectory
            # Return the directory as is.
        
        return dir_name
    
    def _get_search_dirs(self):
        
        dirs = []
        
        # Current Directory:
        if self._search_current_dir:

            dirs.append (os.getcwd())
            
        # App Environment Variable:
        if self._path_env_var is not None:

            path_value = os.getenv(self._path_env_var)
            if path_value is not None:
                dirs.append(path_value)
        
        # User_App_Data_Dir:
        if self._search_user_app_dir_env_var:

            user_app_data_dirs_value = os.getenv(self.ENV_VAR_USER_APP_DIR)
            
            if user_app_data_dirs_value is not None:
                
                user_app_data_dirs_value = self._ua_os.normalize_path (user_app_data_dirs_value)
                user_app_data_dirs = user_app_data_dirs_value.split (self._ua_os.PATH_SEPARATOR)
                
                for dir in user_app_data_dirs:
                    if dir: # Check for empty strings caused by starting or ending path separator.
                        dirs.append (self._get_dir_subdir(dir))
                    
        # Standard User Dir:
        if self._search_user_dir:
            
            dir = self._ua_os.user_dir()
            if dir: 
                dirs.append(self._get_dir_subdir(dir))
        
        # Standard User App Dir:
        if self._search_user_app_dir:
            
            dir = self._ua_os.user_app_dir()
            if dir: 
                dirs.append(self._get_dir_subdir(dir))
            
        return dirs   
         
    def _print (self, text):
        
        if self._debug:
            print (text)