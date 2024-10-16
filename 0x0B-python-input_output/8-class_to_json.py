#!/usr/bin/python3
"""Function that returns the dictionary description with simple data structure
   for JSON serialization of an object.
"""

def class_to_json(obj):
    """Returns the dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a class.

    Returns:
        A dictionary containing all serializable attributes of the object.
    """
    return obj.__dict__

