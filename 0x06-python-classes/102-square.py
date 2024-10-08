#!/usr/bin/python3
"""square module."""


class Square:
    """Define a square with size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (float|int): The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not a number (float or int).
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Compare if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Compare if this square is less than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Compare if this square is less than or equal to another based on area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Compare if this square is greater than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Compare if this square is greater than or equal to another based on area."""
        return self.area() >= other.area()

