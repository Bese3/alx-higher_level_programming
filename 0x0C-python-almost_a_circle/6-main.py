#!/usr/bin/python3
""" 6-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    r1 = Rectangle(2, 3, 2, 2)
    ds = r1.display()
    print("-")
    print(ds)

    print("---")

    r2 = Rectangle(3, 2, 1, 0)
    r2.display()