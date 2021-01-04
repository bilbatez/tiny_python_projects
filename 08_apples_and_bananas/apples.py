#!/usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Chapter 8 - Apples and Bananas
"""

import os
import io
import sys
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Apples and bananas",
    )
    parser.add_argument(
        "text",
        default=sys.stdin,
        help="Input text or file",
    )
    parser.add_argument(
        "-v",
        "--vowel",
        metavar="vowel",
        default="a",
        type=str,
        choices=list("aeiou"),
        help="The vowel(s) allowed",
    )
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()

    in_fh = open(args.text) if os.path.isfile(args.text) else io.StringIO(args.text)
    for line in in_fh:
        n_line = ""
        for char in line:
            vowel_substitute = (
                args.vowel.upper() if char.isupper() else args.vowel.lower()
            )
            n_line += vowel_substitute if char in "aeiouAEIOU" else char
        print(n_line)


if __name__ == "__main__":
    main()
