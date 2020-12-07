#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com>
Purpose: Chapter 7 - Gashlycrumb
"""

import argparse

dictionary = dict()


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Gashlycrumb",
    )
    parser.add_argument(
        "letters", metavar="LETTER", type=str, nargs="+", help="Letter(s)"
    )
    parser.add_argument(
        "-f",
        "--file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default="gashlycrumb.txt",
        help="Input file (default: gashlycrumb.txt)",
    )
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()
    for line in args.file:
        key = line[0].upper()
        dictionary[key] = line

    for letter in args.letters:
        letter = letter.upper()
        print(dictionary.get(letter, f"I do not know \"{letter}\".\n"), end="")


if __name__ == "__main__":
    main()
