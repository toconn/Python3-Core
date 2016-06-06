import glob
import os
import shutil

def add_cwd_to_file_name(file_name):
    
    return os.getcwd() + os.path.sep + file_name

def copy (source_path, destination_path):
    
    shutil.copyfile(source_path, destination_path)

def delete (file_path):
    ''' No fuss file / dir delete command.
        Wouldn't throw an error if it does not exist.
        Will delete it no matter what it is.
    '''

    if is_file_exists (file_path):
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        else:
            os.remove(file_path)

def file_base_name (file_name):
    ''' returns the base name of a file name (filename.ext = filename).
    '''
    
    file_base_name, file_ext = os.path.splitext(file_name)
    return file_base_name

def file_extension (file_name):
    ''' Returns the file extension (dir/filename.ext = ext)
    '''
    
    file_base_name, file_ext = os.path.splitext(file_name)
    return file_ext

def get_dir_file_names (dir_path, file_filter=None):
    ''' Returns a list of files in a directory. The file list can be filtered (ex: *.txt).
    '''
    
    if file_filter:
        file_names = [os.path.basename(file_name) for file_name in glob.glob (os.path.join (dir_path, file_filter))]
    else:
        file_names = os.listdir(dir_path)
        
    return file_names

def get_dir_file_paths (dir_path, file_filter=None):
    ''' Returns a list of files in a directory. The file list can be filtered (ex: *.txt).
    '''

    return glob.glob (os.path.join (dir_path, file_filter))

def is_dir_and_file_exists (dir_path, file_name):
    
    return is_file_exists (os.path.join(dir_path, file_name))

def is_dir_exists(dir_path):
    ''' Tests if the directory exists and is in fact a directory
    '''
    
    exists = os.path.isdir(dir_path)  
    return exists

def is_file_exists(file_path):
    
    exists = os.path.exists(file_path)  
    return exists

def has_dir_in_path(file_path):
    ''' Returns true if the file path contains a direcory component.
        dir1/filename = True
        filename = False
    '''
    
    return file_path != path_file_name(file_path)

def path_file_name (file_path):
    ''' Returns the full file name from the path (dir/filename.ext = filename.ext)
    '''

    file_name = os.path.basename(file_path)
    return file_name
