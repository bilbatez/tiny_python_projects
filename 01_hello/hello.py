#!/usr/bin/env python3
"""
Author:     Albert Julian Tannady <albertjulian97@gmail.com>
Purpose:    Say Hello
"""

import argparse


# Python functions are define using def, and use a snake_case naming convention
def get_args():
    """Get the command-line arguments"""
    parser = argparse.ArgumentParser(description="Say Hello")

    # Positional Argument: must be supplied
    # parser.add_argument('name', help='Name to greet')

    # Optional Argument: optional, requires - or -- as a prefix
    parser.add_argument("-n",
                        "--name",
                        metavar="name",
                        default="World",
                        help="Name to greet")
    return parser.parse_args()


def main():
    """Main Program"""
    args = get_args()
    print("Hello, " + args.name + "!")


# Each python module has a name, and it will be set through a special variable called '__name__'
# If it is run as a script, the '__name__' will be automatically set as '__main__'
# which is why the conditional statemet is like this
if __name__ == "__main__":
    main()
