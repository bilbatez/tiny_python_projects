#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com>
Purpose: Chapter 5 - CAT
"""

import sys
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="cat program",
    )
    parser.add_argument(
        "file",
        metavar="FILE",
        nargs="?",
        type=argparse.FileType("rt"),
        default=sys.stdin,
        help="Input file(s)",
    )
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()

    if args.file is sys.stdin:
        for line in sys.stdin:
            if line.rstrip() == "q":
                break
            print(line)
    else:
        in_fh = args.file
        for line in in_fh:
            print(line)


if __name__ == "__main__":
    main()
