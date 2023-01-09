#!/usr/bin/python3

"""5-save_to_json_file
Contains function save_to_json_file
"""


def save_to_json_file(my_obj, filename):
    """Saves Python object to a JSON file

    Args:
        my_obj (object): object to be serialized
        filename (str): name of file to save object to
    """
    with open(filename, "w") as f:
        f.write(__import__("json").dumps(my_obj))
