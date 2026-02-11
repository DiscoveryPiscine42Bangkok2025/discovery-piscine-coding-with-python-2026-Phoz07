#!/usr/bin/env python

str = input().strip()

for c in str:
    if c.isupper():
        print(c.lower(), end="")
    elif c.islower():
        print(c.upper(), end="")
    else:
        print(c, end="")
