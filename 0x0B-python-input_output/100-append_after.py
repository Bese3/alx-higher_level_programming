#!/usr/bin/python3

"""100-append_after
Contains function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends text after each specific string
    Args:
        filename (str): name of the file to be modified
        search_string (str): string where new_string will be appended to in
        the file
        new_string (str): string to be appended to after each instance of
        search_string in the file
    """

    with open(filename) as f:
        file_contents = f.read()

    for i in range(len(file_contents)):
        if file_contents[i: i + len(search_string) - 1] == search_string:
            file_contents = file_contents[:i + len(search_string)] + \
                            new_string +\
                            file_contents[i + len(search_string) + len(
                                new_string):]

    with open(filename, "w") as f:
        f.write(file_contents)
