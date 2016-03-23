def count (list1):
    
    if list1 is not None:
        return len(list1)
    else:
        return 0

def sort(list1):

    return list1.sort (key=str.lower)
