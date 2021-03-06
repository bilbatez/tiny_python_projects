#!/usr/bin/env python3
""" test cat program """

import os
import random
import re
import string
from subprocess import getstatusoutput

prg = "./cat.py"
empty = "./inputs/empty.txt"
one_line = "./inputs/one.txt"
two_lines = "./inputs/two.txt"
fox = "../inputs/fox.txt"
sonnet = "../inputs/sonnet-29.txt"


def test_exists():
    """ exists """

    os.path.isfile(prg)


def test_usage():
    """ usage """

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)


def random_string():
    """ generate a random string """
    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


def test_bad_file():
    """ test non existing file """

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {bad}")
    assert rv != 0
    assert re.search(f"No such file or directory: '{bad}'", out)


def test_fox():
    """ test fox file """

    rv, out = getstatusoutput(f"{prg} {fox}")
    assert rv == 0
    assert out.rstrip == "The quick brown fox jumps over the lazy dog."
