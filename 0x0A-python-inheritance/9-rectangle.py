#!/usr/bin/python3
'''Module that defines a Rectangle class inheriting from BaseGeometry.'''

from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    '''A class representing a rectangle that inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Initialize the Rectangle with width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than or equal to zero.
        '''
        self.integer_validator("width", width)
        self.__width = width  # Private attribute
        self.integer_validator("height", height)
        self.__height = height  # Private attribute

    def area(self):
        '''Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle (width * height).
        '''
        return self.__width * self.__height

    def __str__(self):
        '''Return a string representation of the rectangle.'''
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

