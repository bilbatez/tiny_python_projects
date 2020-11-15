#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Captain, {} {} off the {} bow!"


def test_exists():
    """exists"""

    assert os.path.isfile(prg)


def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("a", word, "larboard")


def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("a", word.title(), "larboard")


def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("an", word, "larboard")


def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word.upper()}")
        assert out.strip() == template.format("an", word.upper(), "larboard")


def test_side_larboard():
    """without --starboard -> larboard"""
    out = getoutput(f"{prg} brigatine")
    assert out.strip() == template.format("a", "brigatine", "larboard")


def test_side_starboard():
    """with --starboard -> starboard"""
    out = getoutput(f"{prg} brigatine --starboard=True")
    assert out.strip() == template.format("a", "brigatine", "starboard")
