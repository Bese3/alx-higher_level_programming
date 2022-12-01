#!/usr/bin/python3
from sys import argv


def main():
    final_sum = 0

    for i in range(len(argv) - 1):
        final_sum += int(argv[i + 1])
    print(final_sum)


if __name__ == '__main__':
    main()
