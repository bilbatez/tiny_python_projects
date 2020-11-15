#!/usr/bin/env python3
"""
Author : albertjtan <albertjtan@localhost>
Date   : 2020-11-15
Purpose: Chapter 2 - Crowsnest
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crowsnest", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument("word", help="A word")
    parser.add_argument(
        "-s",
        "--starboard",
        metavar="starboard",
        default=False,
        type=bool,
        help="Change the side of the board to starboard",
    )

    return parser.parse_args()


def main():
    """Run Crowsnest Program"""

    args = get_args()
    char = args.word[0].lower()
    article = "an" if char in "aeiou" else "a"
    side = "starboard" if args.starboard else "larboard"
    output = f"Ahoy, Captain, {article} {args.word} off the {side} bow!"
    print(output)


if __name__ == "__main__":
    main()
