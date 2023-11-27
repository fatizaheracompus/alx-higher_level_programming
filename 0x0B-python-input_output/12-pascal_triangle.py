#!/usr/bin/python3
"""Function defines the Pascal's Triangle functions."""


def pascal_triangle(n):
    """Representation Pascal's Triangles of the size n.

    Returns  list of lists of integer representing of the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
