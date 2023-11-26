#!/usr/bin/python3
"""Define a function that adds attributes to objects."""


def add_attribute(objt, at, val):
    """Add a new attribute to an object if possible.
    Args:
        objt (any): The object to add an attribute to.
        at (str): The name of the attribute to add to objt.
        val (any): The value of at.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(objt, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(objt, at, val)
