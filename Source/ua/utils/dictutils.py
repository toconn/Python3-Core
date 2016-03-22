from collections import OrderedDict


def max_key_len (dictionary):

    max_len = 0

    if dictionary is not None:
        for key in dictionary.keys():
            if len(key) > max_len:
                max_len = len(key)

    return max_len


def merge(*dicts):
    '''Shallow merge of 2 or more dicts into a new dict.
    '''

    merged_dict = {}

    for item in dicts:
        merged_dict.update(item)

    return merged_dict


def sort(dict1):

    return OrderedDict(sorted(dict1.items(), key=lambda item: item[0].lower()))

