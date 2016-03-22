'''
Standard functions to be used across the board.
'''

def iif (test, true_value, false_value = None):
    '''This is a more readable replacement for python's built in inline
       if statement.
    '''
    
    if test:
        return true_value
    else:
        return false_value
