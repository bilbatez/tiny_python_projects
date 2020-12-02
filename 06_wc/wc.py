#!/usr/bin/env python3
"""
Author: Albert Julian Tannady <albertjulian97@gmail.com>
Purpose: Chapter 6 - Word Count
"""

import sys
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Emulate wc (word count)",
    )
    parser.add_argument(
        "files",
        metavar="FILE",
        nargs="*",
        type=argparse.FileType("rt"),
        default=[sys.stdin],
        help="Input file(s)",
    )

    parser.add_argument(
        "-c",
        "--bytes",
        action="store_true",
        default=False,
        help="print the byte counts",
    )
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        default=False,
        help="print the word counts",
    )
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        default=False,
        help="print the line counts",
    )
    return parser.parse_args()


def main():
    """ Main Program """
    args = get_args()

    print_bytes, print_words, print_lines = args.bytes, args.words, args.lines
    if not (print_bytes or print_words or print_lines):
        print_bytes, print_words, print_lines = True, True, True

    total_line_count, total_word_count, total_byte_count = 0, 0, 0

    for in_fh in args.files:
        message_col = []
        filename = in_fh.name
        line_count, word_count, byte_count = 0, 0, 0
        for line in in_fh:
            line_count += 1
            word_count += len(line.split())
            byte_count += len(line)

        if print_lines:
            message_col.append(f"{line_count:8}")
        if print_words:
            message_col.append(f"{word_count:8}")
        if print_bytes:
            message_col.append(f"{byte_count:8}")

        message = "".join(message_col)

        total_line_count += line_count
        total_word_count += word_count
        total_byte_count += byte_count
        print(f"{message} {filename:8}")

    if len(args.files) > 1:
        message_col = []
        if print_lines:
            message_col.append(f"{total_line_count:8}")
        if print_words:
            message_col.append(f"{total_word_count:8}")
        if print_bytes:
            message_col.append(f"{total_byte_count:8}")

        message = "".join(message_col)
        print(f"{total_line_count:8}{total_word_count:8}{total_byte_count:8} total")


if __name__ == "__main__":
    main()
