import os

def file_extension (file_name):
    
    file_bare_name, file_ext = os.path.splitext(file_name)
    return file_ext