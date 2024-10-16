#!/usr/bin/python3
"""Defines a function that creates an Object from a JSON file."""
import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.
    
    Args:
        filename: The name of the file containing the JSON representation.
        
    Returns:
        The object created from the JSON file.
    """
    with open(filename, 'r') as f:
        return json.load(f)

