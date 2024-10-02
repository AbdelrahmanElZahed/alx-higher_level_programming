#!/usr/bin/python3
"""square module."""


class Square:
    """Define a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
            position (tuple): The position of the square in 2D space.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Property for the length of a side of this square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
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
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                any(num < 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.size == 0:
            print("")
            return

        # Print the vertical position (spaces)
        for _ in range(self.position[1]):
            print("")
        
        for _ in range(self.size):
            print(" " * self.position[0] + "#" * self.size)

    def __str__(self):
        """Return the string representation of the square."""
        output = []
        if self.size == 0:
            return ""
        
        # Print the vertical position (spaces)
        for _ in range(self.position[1]):
            output.append("")
        
        for _ in range(self.size):
            output.append(" " * self.position[0] + "#" * self.size)

        return "\n".join(output)

