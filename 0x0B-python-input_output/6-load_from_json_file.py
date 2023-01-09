#!/usr/bin/python3

"""6-load_from_json
Contains function load_from_json_file
"""


def load_from_json_file(filename):
    """Creates a Python object from JSON file

    Args:
        filename (str): name of JSON file

    Returns:
        Deserialized Python object
    """
    with open(filename) as f:
        return __import__("json").loads(f.read())
