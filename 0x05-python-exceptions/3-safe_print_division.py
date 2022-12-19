#!/usr/bin/python3


def safe_print_division(a, b):
    quotient = 0
    div_by_zero = False

    try:
        quotient = a / b
    except ZeroDivisionError:
        div_by_zero = True
    finally:
        if div_by_zero:
            print("{}{}".format("Inside result: ", None))
            return None

        print("{}{}".format("Inside result: ", quotient))
        return quotient
