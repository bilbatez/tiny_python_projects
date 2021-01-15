#! /usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Chapter 9 - Abuse
"""

import random
import argparse

ADJ = """
    bankrupt base caterwauling corrupt cullionly detestable dishonest false filthsome 
    filthy foolish foul gross heedless indistinguishable infected insatiate irksome 
    lascivious lecherous loathsome lubbery old peevish rascaly rotten ruinous scurilous 
    scurvy slanderous sodden-witted thin-faced toad-spotted unmannered vile wall-eyed
    """.split()
NOUNS = """
    Judas Satan ape ass barbermonger beggar block boy braggart butt carbuncle coward 
    coxcomb cur dandy degenerate fiend fishmonger fool gull harpy jack jolthead knave 
    liar lunatic maw milksop minion ratcatcher recreant rogue scold slave swine traitor 
    varlet villain worm
    """.split()


def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Abuse"
    )
    parser.add_argument(
        "-a",
        "--adjectives",
        metavar="adjectives",
        help="Number of adjectives",
        default=2,
        type=int,
    )
    parser.add_argument(
        "-n",
        "--number",
        metavar="insults",
        help="Number of insults",
        default=3,
        type=int,
    )
    parser.add_argument(
        "-s",
        "--seed",
        metavar="seed",
        help="Random seed",
        default=None,
        type=int,
    )
    parser.add_argument(
        "-af",
        "--adjectives-file",
        metavar="adjective file",
        type=argparse.FileType("rt"),
        default=None,
        help="File containing adjectives",
    )
    parser.add_argument(
        "-nf",
        "--nouns-file",
        metavar="noun file",
        type=argparse.FileType("rt"),
        default=None,
        help="File containing nouns",
    )
    args = parser.parse_args()
    if args.adjectives <= 0:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')
    if args.number <= 0:
        parser.error(f'--number "{args.number}" must be > 0')
    return args


def main():
    args = get_args()
    random.seed(args.seed)
    adjectives_list = (
        ADJ if args.adjectives_file is None else [line.strip() for line in args.adjectives_file]
    )
    nouns_list = (
        NOUNS if args.nouns_file is None else [line.strip() for line in args.nouns_file]
    )
    for _ in range(args.number):
        selected_adj = ", ".join(random.sample(adjectives_list, args.adjectives))
        selected_noun = random.choice(nouns_list)
        print(f"You {selected_adj} {selected_noun}!")


if __name__ == "__main__":
    main()
