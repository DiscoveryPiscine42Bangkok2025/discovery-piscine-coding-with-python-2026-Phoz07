#!/usr/bin/env python
import sys


def shrink(text):
    return text[:8]


def enlarge(text):
    for _ in range(len(text), 8, 1):
        text += "Z"
    return text


if len(sys.argv) < 2:
    print("none")
else:
    for text in sys.argv[1:]:
        if len(text) > 8:
            print(shrink(text))
        else:
            print(enlarge(text))
