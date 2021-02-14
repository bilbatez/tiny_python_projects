#! /usr/bin/env python3
"""
Author: Albert Julian Tannady
Purpose: Bottles of Beer - Chapter 11
"""

import argparse

def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Bottles",
    )
    parser.add_argument("-n", "--num", type=int, default=10)
    parser.add_argument("-s", "--step", type=int, default=1)
    parser.add_argument("-r", "--reverse", action="store_true", default=False)
    args = parser.parse_args()
    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')
    if args.step < 1:
        parser.error(f'--s "{args.step}" must be greater than 0')
    return args


def main():
    """ Main Program """
    args = get_args()
    lst_range = range(args.num, 0, -args.step)
    lst_range = reversed(lst_range) if args.reverse else lst_range 
    results = [verse(i, args) for i in lst_range]
    print("\n\n".join(results))


def get_bottle_message(num_of_bottles):
    """ Parse Bottle Message """
    return (
        "No more bottles"
        if num_of_bottles == 0
        else f"{num_of_bottles} bottle"
        if num_of_bottles == 1
        else f"{num_of_bottles} bottles"
    )


def verse(bottles, args):
    """Sing a verse"""

    bottle_msg = get_bottle_message(bottles)

    next_bottle_count = (bottles + args.step 
        if args.reverse else 0 
        if bottles - args.step < 0 
        else bottles - args.step)

    return "\n".join(
        [
            f"{bottle_msg} of beer on the wall,",
            f"{bottle_msg} of beer,",
            f"Take {args.step} down, pass it around,",
            f"{get_bottle_message(next_bottle_count)} of beer on the wall!",
        ]
    )


if __name__ == "__main__":
    main()
