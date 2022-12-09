#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    if value is None:
        return a_dictionary
    if a_dictionary is None or len(list(a_dictionary.keys())) == 0:
        return None

    if value not in list(a_dictionary.values()):
        return a_dictionary

    a_list = list(a_dictionary.items())

    for i in a_list:
        if value == i[1]:
            del a_dictionary[i[0]]
            continue

    return a_dictionary
