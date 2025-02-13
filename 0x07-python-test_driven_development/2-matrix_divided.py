#!/usr/bin/python3
"""Module for matrix division."""

def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a given divisor.
    
    Args:
        matrix (list): A list of lists of integers or floats.
        div (int/float): The number by which to divide the matrix elements.

    Returns:
        list: A new matrix with each element divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a matrix (list of lists) of integers/floats.
        TypeError: If rows of the matrix are not all the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows in the matrix have the same size
    row_length = len(matrix[0])
    if any(len(row) != row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if all elements in the matrix are integers or floats
    for row in matrix:
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Create a new matrix with the results
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return new_matrix

