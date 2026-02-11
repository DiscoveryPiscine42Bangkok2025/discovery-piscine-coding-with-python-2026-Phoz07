#!/usr/bin/env python

import sys

if len(sys.argv) < 2:
    print("none")
else:
    words_arr = sys.argv[1:]
    for word in words_arr:
        print(f"{word}: {len(word)}")
