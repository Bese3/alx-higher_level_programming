#!/usr/bin/python3

for i in range(1, 101):
    if i < 10:
        print("0{}, ".format(str(i)), end="")
    else:
        if i < int(str(i % 10) + str(i // 10)):
            print("{}, ".format(str(i)) if i != 89 else "89\n", end="")
