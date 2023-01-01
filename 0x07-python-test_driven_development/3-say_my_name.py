#!/usr/bin/python3

"""3-say_my_name.py
Holds the function say_my_name and used to test the function using
tests/3-say_my_name.txt
"""


def say_my_name(first_name, last_name=""):
    """Prints the first_name followed by the last_name
    If either first_name or last_name is not a string, a TypeError is raised
    with message "first_name must be a string" or "first_name must be a string"

    Args:
        first_name (str): first name of the user
        last_name (str): last name of the user
    Returns:
        void
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")

    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
