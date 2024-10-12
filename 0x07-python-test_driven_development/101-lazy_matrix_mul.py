import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy."""
    # Check if m_a is a list of lists (matrix)
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    
    # Check if m_b is a list of lists (matrix)
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    
    # Convert matrices to NumPy arrays
    try:
        np_m_a = np.array(m_a)
        np_m_b = np.array(m_b)
    except Exception as e:
        raise ValueError("Invalid input") from e
    
    # Check if matrix dimensions are compatible for multiplication
    if np_m_a.shape[1] != np_m_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = np.matmul(np_m_a, np_m_b)

    return result.tolist()  # Convert result back to list of lists

