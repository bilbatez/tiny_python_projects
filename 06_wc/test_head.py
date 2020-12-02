#!/usr/bin/env python3
""" head program test """

import os
import re
import random
import string
from subprocess import getstatusoutput

prg = "./head.py"

def test_exists():
    """ test program exists """

    assert os.path.isfile(prg)

def test_usage():
    """ test program usage """

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert re.match("usage", out, re.IGNORECASE)

def random_string():
    """ random string """

    k = random.randint(5, 10)
    return "".join(random.choices(string.ascii_letters + string.digits, k=k))


def test_bad_file():
    """ test bad file """
    bad = random_string()
    rv, out = getstatusoutput(f"{prg} {bad}")
    assert rv !=0
    assert re.search(f"No such file or directory: '{bad}'", out)


def test_singleline_file():
    """ test singleline file """
    input_file = "../inputs/fox.txt"
    rv, out = getstatusoutput(f"{prg} {input_file}")
    assert rv == 0
    assert out.rstrip() == "The quick brown fox jumps over the lazy dog."


def test_multiline_file():
    """ test multiline_file """
    input_file = "../inputs/gettysburg.txt"
    rv, out = getstatusoutput(f"{prg} {input_file}") 
    assert rv == 0
    assert out.rstrip() == "Four score and seven years ago our fathers brought forth on this"   
