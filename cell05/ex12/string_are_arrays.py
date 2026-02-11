#!/usr/bin/env python

import sys

if len(sys.argv) != 2:
    print("none")
else:
    str = sys.argv[1]
    isFound = False
    for char in str:
        if char == "z":
            print("z", end="")
            isFound = True
    if not isFound:
        print("none")
