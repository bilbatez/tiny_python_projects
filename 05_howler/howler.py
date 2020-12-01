#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com>
Purpose: Chapter 5 - Howler
"""

import io
import os
import sys
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Howler Program",
    )
    parser.add_argument("input", type=str, metavar="text", help="Input string or file")
    parser.add_argument("-o", "--outfile", type=str, metavar="str", help="Output filename")
    parser.add_argument("--ee", action="store_true", help="Lowercase")
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()
    in_fh = open(args.input) if os.path.isfile(args.input) else io.StringIO(args.input)
    out_fh = open(args.outfile, "wt") if args.outfile else sys.stdout
    for line in in_fh: 
        out_fh.write((line.upper() if not args.ee else line.lower()))
    out_fh.close()


if __name__ == "__main__":
    main()
