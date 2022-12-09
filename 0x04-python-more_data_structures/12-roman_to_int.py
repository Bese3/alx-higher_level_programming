#!/usr/bin/python3


def roman_to_int(roman_string):
    if roman_string != str(roman_string) or roman_string is None or\
            roman_string == "":
        return 0
    symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    sum_ = 0

    i = 0
    while i < len(roman_string):
        #  If the next two letters are for instance "IX", return "X" - "I"
        if i + 1 < len(roman_string) and\
                symbols[roman_string[i]] < symbols[roman_string[i + 1]]:
            sum_ += symbols[roman_string[i + 1]] - symbols[roman_string[i]]
            i += 2
            continue
        sum_ += symbols[roman_string[i].upper()]
        i += 1
    return sum_
