#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    The function "say_my_name" takes in a first
    name and an optional last name as parameters and prints
    out a statement with the provided names.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(F"My name is {first_name} {last_name}")
