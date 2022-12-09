#!/usr/bin/python3


def weight_average(my_list=[]):
    if my_list is None or my_list == []:
        return 0

    sum_ = 0
    denominator_sum = 0

    for i in my_list:
        sum_ += i[0] * i[1]

    for i in my_list:
        denominator_sum += i[1]

    return float(sum_) / denominator_sum
