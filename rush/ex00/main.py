#!/usr/bin/env python
import sys

from checkmate import checkmate


def main():
    board = """\
.R.
.P.
.KQ\
"""
    if len(sys.argv) > 1:
        for i in sys.argv[1:]:
            board = i
            checkmate(board)
    else:
        checkmate(board)


if __name__ == "__main__":
    main()
