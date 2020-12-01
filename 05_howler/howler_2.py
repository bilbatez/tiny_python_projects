#!/usr/bin/env python3

import io
import os
import sys
import argparse

def get_args():
    """ Get command-line arguments """
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Howler's Second Program")
    parser.add_argument("input", type=str, nargs="+", metavar="str", help="Input messages or files")
    parser.add_argument("-o", "--outdir", type=str, default="", metavar="outdir", help="Output Directory")
    return parser.parse_args()

def main():
    args = get_args()

    if (args.outdir and not os.path.exists(args.outdir)):
        curr_umask = os.umask(0o000)
        os.mkdir(args.outdir)
        os.umask(curr_umask)

    for arg in args.input:
        in_fh = open(arg) if os.path.isfile(arg) else io.StringIO(arg)
        out_fh = open(os.path.join(args.outdir, os.path.basename(arg)), "wt") if os.path.isfile(arg) and args.outdir else sys.stdout
        for line in in_fh:
            out_fh.write(line.upper())
        out_fh.close()
        in_fh.close()


if __name__ == "__main__":
    main()