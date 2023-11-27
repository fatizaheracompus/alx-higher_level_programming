#!/usr/bin/python3
"""Define  file-writing function."""


def write_file(filename="", text=""):
    """Writes  string to the  UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to writes to the file.
    Returns:
        The numbers of characters writene.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
