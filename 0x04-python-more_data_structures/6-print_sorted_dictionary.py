#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    keys = sorted(list(a_dictionary.keys()))

    for key in keys:
        print("{}: {}".format(key, a_dictionary[key]))
