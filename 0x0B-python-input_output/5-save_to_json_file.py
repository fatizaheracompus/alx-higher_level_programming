#!/usr/bin/python3
"""Function define a JSON file-writing functione."""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to the text file using JSON representations."""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
