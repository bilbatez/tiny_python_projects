#!/usr/bin/env python3
""" test for howler_2.py """

import os
import re
import random
import string
import shutil
from subprocess import getstatusoutput, getoutput

prg = './howler_2.py'

def random_string():
    """ generate a random string """

    k = random.randint(5, 10)
    return ''.join(random.choices(string.ascii_letters + string.digits, k=k))


def out_flag():
    """Either -o or --outdir"""

    return '-o' if random.randint(0, 1) else '--outdir'

def test_exists():
    """ exists """

    assert os.path.isfile(prg)

def test_text_stdout():
    """ Test STDIN/STDOUT """
    out = getoutput(f'{prg} "foo bar baz"')
    assert out.strip() == "FOO BAR BAZ"    

def test_outdir():
    """Test file in/out"""

    try:
        out_dir = random_string()
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)

        for expected_file in os.listdir('test-outs'):
            basename = os.path.basename(expected_file)
            in_file = os.path.join('../inputs', basename)
            out = getoutput(f'{prg} {out_flag()} {out_dir} {in_file}')
            assert out.strip() == ''
            produced = open(os.path.join(out_dir, expected_file)).read().rstrip()
            expected = open(os.path.join('test-outs',
                                            expected_file)).read().strip()
            assert expected == produced
    finally:
        if os.path.isdir(out_dir):
            shutil.rmtree(out_dir)
