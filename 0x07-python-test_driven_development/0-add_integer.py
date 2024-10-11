#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats.

    Args:
        a: The first number, can be an integer or float.
        b: The second number, can be an integer or float, defaults to 98.

    Raises:
        TypeError: If a or b is not an integer or float.

    Returns:
        The addition of a and b as an integer.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    
    return int(a) + int(b)

