#!/usr/bin/env python

import sys


def check_ism(string):
    if (
        string[len(string) - 3] == "i"
        and string[len(string) - 2] == "s"
        and string[len(string) - 1] == "m"
    ):
        return True
    return False


def append_it(string):
    return string + "ism"


if len(sys.argv) < 2:
    print("none")
else:
    for arg in sys.argv[1:]:
        if check_ism(arg):
            continue
        else:
            print(append_it(arg))
