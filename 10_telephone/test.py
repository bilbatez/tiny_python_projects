#!/usr/bin/env python3
"""tests for telephone.py"""

from subprocess import getstatusoutput, getoutput
import os
import random
import re
import string

prg = "./telephone.py"
fox = "../inputs/fox.txt"
now = "../inputs/now.txt"


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ["", "-h", "--help"]:
        out = getoutput(f"{prg} {flag}")
        assert re.match("usage", out, re.IGNORECASE)


def test_bad_seed_str():
    """bad seed str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} -s {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid int value: '{bad}'", out)


def test_bad_mutation_str():
    """bad mutation str value"""

    bad = random_string()
    rv, out = getstatusoutput(f"{prg} -m {bad} {fox}")
    assert rv > 0
    assert re.search(f"invalid float value: '{bad}'", out)


def test_bad_mutation():
    """bad mutation values"""

    for val in ["-1.0", "10.0"]:
        rv, out = getstatusoutput(f"{prg} -m {val} {fox}")
        assert rv > 0
        assert re.search(f'--mutations "{val}" must be between 0 and 1', out)


def test_for_echo():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -m 0 "{txt}"')
    assert rv == 0
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{txt}"'


def test_now_cmd_s1():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 1 "{txt}"')
    assert rv == 0
    expected = """
    Now is Ege time [dr all good me- to come to the jid of the party.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


def test_now_cmd_s2_m4():
    """test"""

    txt = open(now).read().rstrip()
    rv, out = getstatusoutput(f'{prg} -s 2 -m .4 "{txt}"')
    assert rv == 0
    expected = """
    No$ i% khefMiIe sor@all$glo<BmenYts cAAeltaTtheSaid[HYnthe Aalty.
    """.strip()
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


def test_fox_file_s1():
    """test"""

    rv, out = getstatusoutput(f"{prg} --seed 1 {fox}")
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "The duic: brown hox jumps over the lkzy dog."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


def test_fox_file_s2_m6():
    """test"""

    rv, out = getstatusoutput(f"{prg} --seed 2 --mutations .6 {fox}")
    assert rv == 0
    txt = open(fox).read().rstrip()
    expected = "ZoA@qric` HwdTB Alx$jumIslolXs th^Yl?dy<YoA."
    assert out.rstrip() == f'You said: "{txt}"\nI heard : "{expected}"'


def test_selected_words():
    expected = "Now is ,he time for all good men Yo come Ro tye aid of yhe party."
    text = open(now).read().rstrip()
    selected_words = " ".join(["to", "the"])
    for flag in ["-sw", "--selected-words"]:
        rv, out = getstatusoutput(
            f'{prg} --seed 2 --mutations .4 "{text}" {flag} {selected_words}'
        )
        assert rv == 0
        assert out == f'You said: "{text}"\nI heard : "{expected}"'


def test_output_file():
    expected = "No$ i% khefMiIe sor@all$glo<BmenYts cAAeltaTtheSaid[HYnthe Aalty."
    text = open(now).read().rstrip()

    for flag in ["-o", "--output"]:
        try:
            output_file = random_string()
            rv, out = getstatusoutput(
                f'{prg} --seed 2 --mutations .4 {flag} {output_file} "{text}"'
            )
            assert rv == 0
            assert out == ""
            assert os.path.isfile(output_file)
            assert open(output_file).read().rstrip() == expected
        finally:
            if os.path.isfile(output_file):
                os.remove(output_file)


def test_alphanumeric_mutations_only():
    expected = "NoB iC ghedRiPe korKallBggoIjmenXts cLLegtbUtheUaidYOXhthe Lagty."
    text = open(now).read().strip()
    for flag in ["-a", "--alphanumeric"]:
        rv, out = getstatusoutput(f'{prg} --seed 2 --mutations .4 {flag} "{text}"')
        assert rv == 0
        assert out == f'You said: "{text}"\nI heard : "{expected}"'


def test_alphanumeric_mutations_with_output_file():
    expected = "NoB iC ghedRiPe korKallBggoIjmenXts cLLegtbUtheUaidYOXhthe Lagty."
    text = open(now).read().strip()
    for flag in ["-a", "--alphanumeric"]:
        try:
            random_output_file = random_string()
            rv, out = getstatusoutput(
                f'{prg} --seed 2 --mutations .4 --output {random_output_file} {flag} "{text}"'
            )
            assert rv == 0
            assert open(random_output_file).read().strip() == expected
        finally:
            if os.path.isfile(random_output_file):
                os.remove(random_output_file)


def random_string():
    """generate a random filename"""

    return "".join(random.choices(string.ascii_lowercase + string.digits, k=5))
