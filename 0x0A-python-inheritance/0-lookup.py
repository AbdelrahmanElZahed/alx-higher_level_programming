#!/usr/bin/python3
'''Module for lookup method.'''


def lookup(obj):
    '''Looks up objects attributes and methods.
    Args:
        obj (object): The object to list.
    Returns:
        list: the list of attributes.
    '''
    return dir(obj)
