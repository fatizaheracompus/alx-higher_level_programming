#!/usr/bin/python3
"""Function define the text files insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserte text after each lines containing  given string in the file.

    Args:
        filename (str): The name of  file.
        search_string (str): The string to searche for withine  file.
        new_string (str): The string the insert.
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
