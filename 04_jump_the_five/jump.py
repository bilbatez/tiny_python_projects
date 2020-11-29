#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com
Purpose: Chapter 4 - Jump the Five
"""

import argparse

jtf_dict = {
    "0": "5",
    "1": "9",
    "2": "8",
    "3": "7",
    "4": "6",
    "5": "0",
    "6": "4",
    "7": "3",
    "8": "2",
    "9": "1",
}


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        description="Jump the Five",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("text", metavar="str", help="Input text")
    return parser.parse_args()


def jtf_algo(text):
    """ Jump The Five Algorithm """
    for char in text:
        print(jtf_dict.get(char, char), end="")
    print()


def main():
    """ Main Program """
    args = get_args()
    jtf_algo(args.text)


if __name__ == "__main__":
    main()
