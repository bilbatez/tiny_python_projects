#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com>
Purpose: Chapter 5 - Head Program
"""

import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Head Program",
    )
    parser.add_argument(
        "file", metavar="FILE", type=argparse.FileType("rt"), help="Input file(s)"
    )
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()
    for line in args.file:
        print(line)
        break


if __name__ == "__main__":
    main()
