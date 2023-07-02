#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    The function "say_my_name" takes in a first name and an optional last name as parameters and prints
    out a statement with the provided names.
    
    :param first_name: The `first_name` parameter is a required parameter that should be a string
    representing the first name of a person
    :param last_name: The `last_name` parameter is an optional parameter that represents the last name
    of a person. If no value is provided for `last_name`, it will default to an empty string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print(F"My name is {first_name} {last_name}")