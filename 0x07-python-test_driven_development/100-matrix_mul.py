def matrix_mul(m_a, m_b):
    """Multiply two matrices.
    
    Args:
        m_a: First matrix (list of lists of integers or floats).
        m_b: Second matrix (list of lists of integers or floats).
    
    Returns:
        A new matrix that is the product of m_a and m_b.
    
    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                    if they are empty, or if they contain non-integer/float values.
        ValueError: If m_a and m_b can't be multiplied.
    """
    
    # Validate m_a
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(all(isinstance(element, (int, float)) for element in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # Validate m_b
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not all(all(isinstance(element, (int, float)) for element in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    
    # Validate if m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    
    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row_result = []
        for j in range(len(m_b[0])):
            element_sum = sum(m_a[i][k] * m_b[k][j] for k in range(len(m_b)))
            row_result.append(element_sum)
        result.append(row_result)
    
    return result

