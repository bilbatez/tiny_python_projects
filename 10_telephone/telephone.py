#! /usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Chapter 10 - Telephone
"""

import os
import sys
import random
import string
import argparse


def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Telephone",
    )
    parser.add_argument("text", metavar="text", help="Input text or file", type=str)
    parser.add_argument(
        "-s", "--seed", metavar="seed", help="Random seed", default=None, type=int
    )
    parser.add_argument(
        "-m",
        "--mutations",
        metavar="mutations",
        help="Percent mutations",
        type=float,
        default=0.1,
    )
    parser.add_argument(
        "-sw", "--selected-words", metavar="selected_words", nargs="*", type=str
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="output",
        help="Output",
    )
    parser.add_argument(
        "-a",
        "--alphanumeric",
        action="store_true",
        help="Limit mutations to alphanumeric",
        default=False,
    )
    args = parser.parse_args()
    if not (args.mutations <= 1 and args.mutations >= 0):
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')
    args.text = (
        open(args.text).read().strip()
        if os.path.isfile(args.text)
        else args.text.strip()
    )
    return args


def main():
    """ Main Program """
    args = get_args()

    random_str = (
        "".join(sorted(string.ascii_letters + string.punctuation))
        if not args.alphanumeric
        else "".join(sorted(string.ascii_letters))
    )

    random.seed(args.seed)
    out_fh = open(args.output, "wt") if args.output else sys.stdout

    def mutate(word):
        num_mutations = round(len(word) * args.mutations)
        for i in random.sample(range(len(word)), num_mutations):
            substitute = random.choice(random_str.replace(word[i], ""))
            word = word[:i] + substitute + word[i + 1 :]
        return word

    new_text = ""
    if args.selected_words:
        split_words = args.text.split()
        for i in range(len(split_words)):
            if split_words[i] in args.selected_words:
                split_words[i] = mutate(split_words[i])
        new_text = " ".join(split_words)
    else:
        new_text = mutate(args.text)

    result = (
        f'You said: "{args.text}"\nI heard : "{new_text}"'
        if not args.output
        else new_text
    )
    out_fh.write(result)


if __name__ == "__main__":
    main()
