#!/usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Rhymer - Chapter 14
"""

import re
import sys
import string
import argparse

VOWELS = "aeiou"
CONSONANTS = "".join([c for c in string.ascii_lowercase if c not in VOWELS])
PREFIXES = sorted(
    list(CONSONANTS)
    + (
        "bl br ch cl cr dr fl fr gl gr pl pr sc "
        "sh sk sl sm sn sp st sw th tr tw thw wh wr "
        "sch scr shr sph spl spr squ str thr"
    ).split(" ")
)
PATTERNS = f"([{CONSONANTS}]+)?([{VOWELS}])(.*)"


def get_args():
    """ Get command-line argument """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Make rhyming "words"',
    )
    parser.add_argument('word', help='A word to rhyme')
    parser.add_argument(
        '-o',
        '--output',
        type=argparse.FileType('wt'),
        metavar='output',
        help='Output file',
        default=sys.stdout
    )
    return parser.parse_args()


def stemmer(word):
    """ Stem word """
    word = word.lower()
    match = re.match(PATTERNS, word)
    return (
        (match.group(1) or "", (match.group(2) or "") + (match.group(3) or ""))
        if match
        else (word, "")
    )


def main():
    """ Main Program """
    args = get_args()
    word = stemmer(args.word)
    args.output.write(
        "\n".join([prefix + word[1] for prefix in PREFIXES if word[0] != prefix])
    ) if word[1] else print(f'Cannot rhyme "{args.word}"')


if __name__ == "__main__":
    main()
