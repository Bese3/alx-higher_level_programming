#!/usr/bin/python3


def uppercase(str):
    if str == "":
        print()
        return

    for i in range(0, len(str)):
        n = '\n' if i == len(str) - 1 else ''
        print("{}{}".format(chr(ord(str[i]) - 32), n)
              if 97 <= ord(str[i]) <= 122 else "{}{}".format(str[i], n),
              end="")
