#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    # Holds boolean values that correspond to each value in my_list
    mul_of_2 = []

    for i in my_list:
        mul_of_2.append(True) if i % 2 == 0 else mul_of_2.append(False)

    return mul_of_2
