#!/usr/bin/python3

"""1-write_file
Contains function write_file
"""


def write_file(filename="", text=""):
    """
    Writes text on the file filename, overwrites if file exists and creates
    new one if it doesn't exist

    Args:
        filename (str): name of the file to open
        text (str): text to be written on the file
    Returns:
        Number of characters written on file
    """
    with open(filename, "w") as f:
        chars_written = f.write(text)

    return chars_written
