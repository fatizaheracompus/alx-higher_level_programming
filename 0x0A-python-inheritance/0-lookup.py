#!/usr/bin/python3
'''Module for lookup methode.'''


def lookup(obj):
    '''Look up object attribute and method.
    Args:
        obj (object): the object to list.

    Returns:
        list: the list of the  attribute.
    '''
    return dir(obj)
