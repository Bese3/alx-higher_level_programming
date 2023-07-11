#!/usr/bin/python3
"""
reading text in a file using open method
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to the standard output

    Args:
        filename (str): name of the file to open and read
    """
    if filename == '' or filename is None:
        return
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
