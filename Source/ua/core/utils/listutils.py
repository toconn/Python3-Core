def count (list1):
    
    if list1 is not None:
        return len(list1)
    else:
        return 0

def is_empty(list1):
    
    return count(list1) == 0

def is_equal(list1, list2):
    
    is_match = False
    
    if list1 is not None and list2 is not None:
        if count(list1) == count(list2):
            is_match = True
            for item1, item2 in zip (list1, list2):
                if item1 != item2:
                    # found mismatch. Break with match = false.
                    is_match = False
                    break
    elif list1 is None and list2 is None:
        # Both are None, therefore equal
        is_match = True
    # else:
        # one is none, the other is not none
        # therefore not a match.
    
    return is_match

def is_not_empty(list1):
    
    return not is_empty(list1)

def sort(list1):

    return list1.sort (key=str.lower)
