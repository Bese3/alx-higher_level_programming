#!/usr/bin/python3
"""
Write a string to a UTF8 text file.
"""


def write_file(filename="", text=""):
    """
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """
    if text == '' or text is None:
        return
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
