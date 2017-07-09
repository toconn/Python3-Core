import os
from ua.core.utils import strutils

'''
Created on Jul 4, 2017
@author: Tadhg
'''

def andConditions (*conditions):
    ''' all match conditions must return true to pass this condition.
    '''
    return lambda test_object : all (condition (test_object) for condition in conditions)

def containsDir (field_name, dir_name):
    ''' A condition checker that checks the object field as a path contains a file called file_name in it.
    ''' 
    return lambda test_object : os.path.isdir (os.path.join (getattr(test_object, field_name), dir_name))

def containsFile (field_name, file_name):
    ''' A condition checker that checks the object field as a path contains a file called file_name in it.
    ''' 
    return lambda test_object : os.path.exists (os.path.join (getattr(test_object, field_name), file_name))

def containsText (field_name, match_text):
    ''' A condition checker that checks the object field name contains match_value in it.
    ''' 
    return lambda test_object : strutils.contains (getattr(test_object, field_name), match_text)

