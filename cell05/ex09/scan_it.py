#!/usr/bin/env python

import re
import sys


def scan_it(txt_to_search, sentence):
    words = re.findall(txt_to_search, sentence)
    return len(words)


if len(sys.argv) != 3:
    print("none")
else:
    word_count = scan_it(sys.argv[1], sys.argv[2])
    if word_count > 0:
        print(word_count)
    else:
        print("none")
