#!/usr/bin/python3


def main():
    clear_path_for_queen = __import__('101-nqueens').clear_path_for_queen

    n = 6
    chessboard = []
    for i in range(n):
        chessboard.append([])
        for j in range(n):
            chessboard[i].append(1)

    cleared = clear_path_for_queen(chessboard, [0, 1])
    cleared = clear_path_for_queen(chessboard, [1, 3])

    for i in cleared:
        print(i)


main()