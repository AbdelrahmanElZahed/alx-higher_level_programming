#!/usr/bin/python3
"""square module."""

class Square:
    """Define a square."""
    
    def __init__(self, size=0):
        """Initialize the size of the square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  # Private instance attribute

    def area(self):
        """Return the current square area."""
        return self.__size ** 2  # Area calculation

