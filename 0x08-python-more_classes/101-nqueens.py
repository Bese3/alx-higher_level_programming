#!/usr/bin/python3
"""
The code is importing the `argv`
variable from the `sys` module,
which allows the script to access
command-line arguments.
"""
from sys import argv


col = set()
neg = set()
pos = set()
possible_solution = []


def backtrack_solution(r, n):
    """
    The function `backtrack_solution` uses backtracking
    to find all possible solutions to the N-Queens
    problem.
    """

    if r == n:
        return
    for c in range(n):
        if c in col or (r - c) in neg or (r + c) in pos:
            continue
        possible_solution.append([])
        col.add(c)
        neg.add(r - c)
        pos.add(r + c)
        possible_solution[-1].append(r)
        possible_solution[-1].append(c)
        if len(possible_solution) == n:
            print(possible_solution)
        backtrack_solution(r + 1, n)
        col.remove(c)
        neg.remove(r - c)
        pos.remove(r + c)
        possible_solution.pop(-1)


"""
The `if __name__ == '__main__':` block is used to ensure
that the code inside it is only executedwhen the script
is run directly, and not when it is imported as a module.
"""


if __name__ == '__main__':
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    n = int(argv[1])
    if type(n) is not int:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)
    backtrack_solution(0, n)
