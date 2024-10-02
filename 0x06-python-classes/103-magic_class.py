#!/usr/bin/python3
import math

class MagicClass:
    def __init__(self, radius=0):
        self.__radius = 0  # Initialize __radius to 0

        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")

        self.__radius = radius  # Assign the radius if valid

    def area(self):
        return (self.__radius ** 2) * math.pi  # Calculate the area (πr^2)

    def circumference(self):
        return 2 * math.pi * self.__radius  # Calculate the circumference (2πr)

