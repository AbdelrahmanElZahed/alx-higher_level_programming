#!/usr/bin/python3
'''Module for kind oof a list class.'''


def is_kind_of_class(obj, a_class):
    '''Check if an object is an instance of, or if the object is an instance of a class that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare the object against.

    Returns:
        bool: True if obj is an instance of a_class or a class that inherited from a_class; otherwise False.
    '''
    return isinstance(obj, a_class)

