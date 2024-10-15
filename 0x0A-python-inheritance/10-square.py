#!/usr/bin/python3
'''Module that defines a Square class inheriting from Rectangle.'''


from 9-rectangle import Rectangle

class Square(Rectangle):
    '''A class representing a square that inherits from Rectangle.'''

    def __init__(self, size):
        '''Initialize the Square with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than or equal to zero.
        '''
        self.integer_validator("size", size)
        self.__size = size  # Private attribute
        super().__init__(size, size)  # Initialize the parent class with width and height

    def area(self):
        '''Calculate the area of the square.

        Returns:
            int: The area of the square (size * size).
        '''
        return self.__size * self.__size

    def __str__(self):
        '''Return a string representation of the square.'''
        return "[Square] {}/{}".format(self.__size, self.__size)

