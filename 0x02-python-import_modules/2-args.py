#!/usr/bin/python3
from sys import argv

if len(argv) - 1 == 0:
   print(F"{len(argv) - 1} arguments.")
elif len(argv) - 1 == 1:
    print(F"{len(argv) - 1} arguments:\n1: {argv[1]}")
else:
    print(F"{len(argv) } arguments:")
    for i in range(len(argv) ):
        print(F"{i+1}: {argv[i+1]}")
