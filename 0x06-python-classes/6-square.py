#!/usr/bin/python3
"""square module."""


class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The size of the square, default is 0.
            position (tuple): The position of the square, default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The size of the square.

        Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Property for the position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
                not all(isinstance(i, int) for i in value) or \
                not all(i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints this square with the character #.

        If size is equal to 0, print an empty line.
        """
        if self.size == 0:
            print()
            return
        
        for _ in range(self.position[1]):
            print()

        for i in range(self.size):
            print(" " * self.position[0], end="")
            print("#" * self.size)

