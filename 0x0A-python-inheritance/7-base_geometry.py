#!/usr/bin/python3
'''BaseGeometry class with area and integer validator methods.'''


class BaseGeometry:
    '''BaseGeometry class.'''
    def area(self):
        '''Public instance method that raises an Exception.'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''Validates that value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to be validated.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        '''
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

