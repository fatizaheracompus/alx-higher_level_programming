#!/usr/bin/python3
"""Module for add_integer methode."""


def add_integer(a, b=98):
    """Adds two integer.

    Args:
        a: the first integere.
        b: the second integere, defaulte 98.

    Raises:
        TypeError: if a, b are not int, float.

    Return:
        The sum of the two integeres.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
