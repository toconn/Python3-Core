import os

def file_exists(file_path):
    
    exists = os.path.exists(file_path)  
    return exists