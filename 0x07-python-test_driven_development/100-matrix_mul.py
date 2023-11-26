#!/usr/bin/python3
"""Module for matrix_mul methode."""


def matrix_mul(m_a, m_b):
    """Multiplie one matrix by another.
    Args:
        m_a: the first matrix
        m_b: the second matrix
    Returns:
        matrix: the product
    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a or m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    m_a_empty = False
    m_b_empty = False
    m_a_notrecte = False
    m_b_notrecte = False
    m_a_notnume = False
    m_b_notnume = False
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) != len(m_a[0]):
            m_a_notrecte = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_a_notnume = True

    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) != len(m_b[0]):
            m_b_notrecte = True
        for num in row:
            if not isinstance(num, (int, float)):
                m_b_notnume = True

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    if m_a_notnume:
        raise TypeError("m_a should contain only integers or floats")

    if m_b_notnume:
        raise TypeError("m_b should contain only integers or floats")

    if m_a_notrecte:
        raise TypeError("each row of m_a must should be of the same size")

    if m_b_notrecte:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    rest = [[] for i in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            d = 0
            for k in range(len(m_b)):
                d += m_a[i][k] * m_b[k][j]
            rest[i].append(d)

    return rest

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
