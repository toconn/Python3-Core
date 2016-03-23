import os

def expand_list(strings):
    
    return [ os.path.expandvars(string) for string in strings]
