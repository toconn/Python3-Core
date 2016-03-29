from . import strutils

def contains_ignore_case (strings, match):
    
    if match:
        return match.lower() in (item.lower() for item in strings)
    else:
        return False

def find_index_containing (strings, match):
    
    found = False
    index = 0

    if strings is not None and match is not None:

        for string in strings:
            if strutils.contains(string, match):
                found = True
                break
            index +=1

    if found:
        return index
    else:
        return -1
    return index

def find_index_containing_ignore_case (strings, match):
    
    found = False
    index = 0

    if strings is not None and match is not None:

        for string in strings:
            if strutils.contains_ignore_case(string, match):
                found = True
                break
            index +=1

    if found:
        return index
    else:
        return -1
    return index

