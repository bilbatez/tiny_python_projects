#!/usr/bin/env python3

from rhymer import stemmer


def test_stemmer():
    """ Test stemmer """
    assert stemmer("") == ("", "")
    assert stemmer("cake") == ("c", "ake")
    assert stemmer("chair") == ("ch", "air")
    assert stemmer("APPLE") == ("", "apple")
    assert stemmer("RDNZL") == ("rdnzl", "")
    assert stemmer("123") == ("123", "")
