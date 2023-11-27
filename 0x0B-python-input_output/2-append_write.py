#!/usr/bin/python3
"""Define a file-appending function."""


def append_write(filename="", text=""):
    """Append string to the end of a UTF8 text file.

    Args:
        filename (str): The name of  file to be appende .
        text (str): The string to appende to the file.
    Returns:
        The numbers of characters appende.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)

