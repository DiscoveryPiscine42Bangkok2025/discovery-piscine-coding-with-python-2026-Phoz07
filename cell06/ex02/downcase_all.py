#!/usr/bin/env python

import sys


def downcase_all(text):
    return text.lower()


if len(sys.argv) < 2:
    print("none")
else:
    for text in sys.argv[1:]:
        print(downcase_all(text))
