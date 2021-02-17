#!/usr/bin/env python3
"""tests for rhymer.py"""

import os
import random
import string
from subprocess import getoutput, getstatusoutput

prg = './rhymer.py'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['', '-h', '--help']:
        out = getoutput(f'{prg} {flag}')
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_take():
    """leading consonant"""

    out = getoutput(f'{prg} take').splitlines()
    assert len(out) == 56
    assert out[0] == 'bake'
    assert out[-1] == 'zake'


# --------------------------------------------------
def test_chair():
    """consonant cluster"""

    out = getoutput(f'{prg} chair').splitlines()
    assert len(out) == 56
    assert out[1] == 'blair'
    assert out[-2] == 'yair'


# --------------------------------------------------
def test_chair_uppercase():
    """consonant cluster"""

    out = getoutput(f'{prg} CHAIR').splitlines()
    assert len(out) == 56
    assert out[1] == 'blair'
    assert out[-2] == 'yair'


# --------------------------------------------------
def test_apple():
    """leading vowel"""

    out = getoutput(f'{prg} apple').splitlines()
    assert len(out) == 57
    assert out[10] == 'flapple'
    assert out[-10] == 'thwapple'


# --------------------------------------------------
def test_no_vowels():
    """no vowels"""

    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    bad = ''.join(random.sample(consonants, k=random.randint(4, 10)))
    out = getoutput(f'{prg} {bad}')
    assert out == f'Cannot rhyme "{bad}"'


# --------------------------------------------------
def test_output_file():
    """output file"""
    """leading consonant"""

    for flag in ['-o', '--output']:
        try:
            random_file = random_string()
            rv, out = getstatusoutput(f'{prg} take {flag} {random_file}')
            res = open(random_file).read().strip().split('\n')
            assert rv == 0
            assert out == ''
            assert res[0] == 'bake'
            assert res[-1] == 'zake'
        finally:
            if os.path.isfile(random_file):
                os.remove(random_file)
        


# --------------------------------------------------
def random_string():
    """generate a random filename"""

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))