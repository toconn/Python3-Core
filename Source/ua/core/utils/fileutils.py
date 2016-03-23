import os

def is_dir_and_file_exists (dir, file_name):
    
    return is_file_exists (os.path.join(dir, file_name))

def is_file_exists(file_path):
    
    exists = os.path.exists(file_path)  
    return exists

def file_extension (file_name):
    
    file_bare_name, file_ext = os.path.splitext(file_name)
    return file_ext