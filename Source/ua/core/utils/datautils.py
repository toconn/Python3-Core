'''
Created on Oct 30, 2017
@author: Tadhg
'''

def is_int (text):
    
    try:
        
        int(text)
        return True
    
    except ValueError:
        
        return False
