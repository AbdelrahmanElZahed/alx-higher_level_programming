#!/usr/bin/python3
"""square module."""

class Square:
    """Define a square."""
    
    def __init__(self, size=0):
        """Initialize the size of the square."""
        self.size = size  # Use the setter for initialization

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value  # Private instance attribute

    def area(self):
        """Return the current square area."""
        return self.__size ** 2  # Area calculation

