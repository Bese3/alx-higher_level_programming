#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    quotient_list = []
    try:
        for i in range(list_length):
            try:
                quotient = my_list_1[i] / my_list_2[i]
                quotient_list.append(quotient)
            except TypeError:
                print("wrong type")
                quotient_list.append(0)
            except ZeroDivisionError:
                print("division by 0")
                quotient_list.append(0)
            except IndexError:
                print("out of range")
                quotient_list.append(0)
    finally:
        return quotient_list
