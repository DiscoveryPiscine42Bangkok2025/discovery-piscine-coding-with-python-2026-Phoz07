#!/usr/bin/env python

# import sys

# if len(sys.argv) > 1:
#     try:
#         int(sys.argv[1])
#     except ValueError:
#         print("none")
#         sys.exit(0)

i = 0

while i <= 10:
    print(f"Table de {i}:", end="")
    j = 0
    while j <= 10:
        print(f" {j * i}", end="")
        j += 1
    print()
    i += 1
