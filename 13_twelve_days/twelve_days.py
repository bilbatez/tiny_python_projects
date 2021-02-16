#! /usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Twelve Days - Chapter 13
"""

import sys
import argparse

ORDINAL = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
    7: "seventh",
    8: "eighth",
    9: "ninth",
    10: "tenth",
    11: "eleventh",
    12: "twelfth",
}

GIFTS = [
    "A partridge in a pear tree",
    "Two turtle doves",
    "Three French hens",
    "Four calling birds",
    "Five gold rings",
    "Six geese a laying",
    "Seven swans a swimming",
    "Eight maids a milking",
    "Nine ladies dancing",
    "Ten lords a leaping",
    "Eleven pipers piping",
    "Twelve drummers drumming",
]


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Twelve Days",
    )
    parser.add_argument(
        "-n",
        "--num",
        metavar="number",
        type=int,
        default=12,
        help="Number of days to sing",
    )
    parser.add_argument(
        "-o",
        "--outfile",
        metavar="output_file",
        type=argparse.FileType("wt"),
        help="Outfile",
        default=sys.stdout,
    )
    args = parser.parse_args()
    if args.num < 1 or args.num > 12:
        parser.error(f'--num "{args.num}" must be between 1 and 12')
    return args


def verse(day):
    """ Create a verse """
    day_msg = f"On the {ORDINAL[day]} day of Christmas,"
    selected_gifts = GIFTS[:day]
    selected_gifts.reverse()
    if len(selected_gifts) > 1:
        selected_gifts[-1] = "And " + selected_gifts[-1].lower()
    selected_gifts[-1] = selected_gifts[-1] + ".\n"
    return "\n".join([day_msg, "My true love gave to me,", ",\n".join(selected_gifts)])


def main():
    """ Main Program """
    args = get_args()
    result = [verse(day) for day in range(1, args.num + 1)]
    args.outfile.write("\n".join(result))


if __name__ == "__main__":
    main()
