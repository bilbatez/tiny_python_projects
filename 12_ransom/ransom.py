#! /usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Ransom - Chapter 12
"""

import os
import random
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Ransom",
    )
    parser.add_argument("text", type=str, metavar="text", help="Input text or file")
    parser.add_argument(
        "-s", "--seed", type=int, metavar="seed", help="seed", default=None
    )
    args = parser.parse_args()

    args.text = (
        open(args.text).read().strip()
        if os.path.isfile(args.text)
        else args.text.strip()
    )
    return args


def choose(char):
    """ Randomly choose upper or lower case to return """
    return char.upper() if random.choice([0, 1]) else char.lower()


def main():
    """ Main Program """
    args = get_args()
    random.seed(args.seed)
    result = [choose(i) for i in args.text]
    print("".join(result))


if __name__ == "__main__":
    main()
