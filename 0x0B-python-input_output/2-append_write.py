#!/usr/bin/python3
"""
appending to an existing file
"""


def append_write(filename="", text=""):
    """
    Arg:
      filename: name or path of the file
      text: text to append in the file
    """
    if filename == '' or filename is None:
        return
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
