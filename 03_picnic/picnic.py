#!/usr/bin/env python3
"""
Author:     Albert Julian Tannady <albertjulian97@gmail.com
Purpose:    Chapter 3 - Picnic
"""

import argparse


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Picnic", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "items", nargs="+", help="Brought Items"
    )
    parser.add_argument("-s", "--sorted", action="store_true", help="Sort input")
    parser.add_argument("-noc", "--no-oxford-comma", action="store_true", help="Disable oxford comma")
    parser.add_argument("-d", "--delimiter", default=",", help="Customize delimiter")
    return parser.parse_args()


def main():
    """Run Picnic Program"""
    args = get_args()
    items = args.items
    output = items[0]
    if len(items) > 1:
        if args.sorted:
            items.sort()

        if (args.no_oxford_comma):
            items[-2] = items[-2] + " and " + items[-1]
            items.pop()
        else:
            items[-1] = "and " + items[-1]

        if len(items) > 2:
            delimiter = args.delimiter + " " 
            output = delimiter.join(items)
        else:
            output = " ".join(items)

    print(f"You are bringing {output}.")


if __name__ == "__main__":
    main()
