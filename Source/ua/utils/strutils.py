def lower(string):
    ''' None safe string to lowercase function.
    '''
    
    if string is not None:
        string = string.lower()
    
    return string

def replace(string, search_string, replace_string):
    ''' None safe replace function.
        None returns None
        Also handles integers.
    '''
    
    if string is not None:

        # Change int to string:
        if isinstance(replace_string, int):    
            replace_string = str(replace_string)

        # Replace:
        string = string.replace(search_string, replace_string)

    # Else
        # Return as is (None).
    
    return string

def strip (string):
    '''None safe string strip function.
       None returns None.
    '''

    if string:
        return string.strip()
    else:
        return string

