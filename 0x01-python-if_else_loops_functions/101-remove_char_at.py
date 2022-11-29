#!/usr/bin/python3


def remove_char_at(str, n):
    removed_str = ""
    if n >= 0:
        for i in range(len(str)):
            if i != n:
                removed_str += str[i]
        return removed_str
    return str
