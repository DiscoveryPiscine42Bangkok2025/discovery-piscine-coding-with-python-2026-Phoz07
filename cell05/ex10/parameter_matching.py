#!/usr/bin/env python

import sys


def parameter_matching(param1, param2):
    if param1 == param2:
        return True
    else:
        return False


if len(sys.argv) != 2:
    print("none")
else:
    str = input("What was the parameter? ")
    if parameter_matching(str, sys.argv[1]):
        print("Good job!")
    else:
        print("Nope, sorry...")
