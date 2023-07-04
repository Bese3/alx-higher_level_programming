#!/usr/bin/python3

def Nqueen(size):
    if type(size) is not int:
        raise TypeError("N must be a number")
    if size < 4:
        raise ValueError("N must be at least 4")
    queens = []
    iterate = range(size)
    for i in iterate:
        for j in iterate:
            queens.append([])
            queens[-1].append(i)
            queens[-1].append(j)
    d
    print(queens)


if __name__ == "__main__":
    Nqueen(4)
