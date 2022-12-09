#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    updated_values = list(map(lambda x: x * 2, a_dictionary.values()))
    for key, new_value in zip(a_dictionary.keys(), updated_values):
        new_dict[key] = new_value
    return new_dict
