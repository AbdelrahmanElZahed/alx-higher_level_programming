#!/usr/bin/python3
"""Module that returns an object (Python data structure) represented by a JSON string."""

import json

def from_json_string(my_str):
    """Returns an object represented by a JSON string.
    
    Args:
        my_str: The JSON string to be deserialized.
    
    Returns:
        object: The Python data structure corresponding to the JSON string.
    """
    return json.loads(my_str)

