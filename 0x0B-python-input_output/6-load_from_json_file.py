#!/usr/bin/python3
"""Function define the JSON file-reading functione."""
import json


def load_from_json_file(filename):
    """Creates a Python object from the JSON file."""
    with open(filename) as f:
        return json.load(f)

