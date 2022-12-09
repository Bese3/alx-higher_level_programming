#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    commons = set(filter(lambda x: x in set_2, set_1))
    return (set_1 | set_2) - commons
