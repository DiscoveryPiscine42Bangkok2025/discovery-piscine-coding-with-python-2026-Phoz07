#!/usr/bin/env python

import sys


def construct_array(start, end, step=1):
    return list(range(start, end, step))


if len(sys.argv) != 3:
    print("none")
else:
    if int(sys.argv[1]) > int(sys.argv[2]):
        arr = construct_array(int(sys.argv[1]), int(sys.argv[2]) - 1, -1)
    else:
        arr = construct_array(int(sys.argv[1]), int(sys.argv[2]) + 1)
    print(arr)
