#!/usr/bin/python3
"""Function define Python class-to-JSON functione."""


def class_to_json(obj):
    """Returns the dictionary represntations of a simple data structure."""
    return obj.__dict__
