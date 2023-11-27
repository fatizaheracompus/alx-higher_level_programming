#!/usr/bin/python3
"""Function define a text file-reading function."""


def read_file(filename=""):
    """Print the content of  UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
