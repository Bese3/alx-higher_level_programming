#!/usr/bin/python3

for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print("{}, ".format(str(i)) if i >= 10 else "0{}, ".format(i), end="")
