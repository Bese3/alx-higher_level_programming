#!/usr/bin/python3
number = random.randint(-10000, 10000)
x = number % 10
if x > 5:
    print(F"Last digit of {number} is {x} and is greater than 5\n")
elif x == 0:
    print(F"Last digit of {number} is {x} and is 0\n")
elif x < 5:
    print(F"Last digit of {number} is {x} and is less than 6 and not 0\n")
