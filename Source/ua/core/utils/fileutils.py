import glob
import os
import shutil

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

def get_dir_file_names (dir_path, file_filter=None):
    ''' Returns a list of files. The file list can be filtered (ex: *.txt).
    '''
    
    if file_filter:
        file_names = [os.path.basename(file_name) for file_name in glob.glob (os.path.join (dir_path, file_filter))]
    else:
        file_names = os.listdir(dir_path)
        
    return file_names

def get_dir_file_paths (dir_path, file_filter=None):
    ''' Returns a list of files. The file list can be filtered (ex: *.txt).
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

def file_base_name (file_name):
    
    file_base_name, file_ext = os.path.splitext(file_name)
    return file_base_name

def file_extension (file_name):
    
    file_base_name, file_ext = os.path.splitext(file_name)
    return file_ext