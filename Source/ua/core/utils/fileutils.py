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

def is_dir_and_file_exists (dir, file_name):
    
    return is_file_exists (os.path.join(dir, file_name))

def is_file_exists(file_path):
    
    exists = os.path.exists(file_path)  
    return exists

def file_extension (file_name):
    
    file_bare_name, file_ext = os.path.splitext(file_name)
    return file_ext