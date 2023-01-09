#!/usr/bin/python3

"""2-append_write
Contains function append_write"""


def append_write(filename="", text=""):
    """Appends text to end of file

    Args:
        filename (str): name of file to open
        text (str): text to be appended to the file

    Returns:
        Number of characters written in file
    """
    with open(filename, "a") as f:
        chars_written = f.write(text)

    return chars_written
