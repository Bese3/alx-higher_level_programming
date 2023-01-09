#!/usr/bin/python3

"""4-from_json_string
Contains function from_json_string
"""


def from_json_string(my_str):
    """Constructs Python object from JSON string

    Args:
        my_str (str): JSON object string

    Returns:
        Python object, if deserialized successfully
    """
    return __import__("json").loads(my_str)
