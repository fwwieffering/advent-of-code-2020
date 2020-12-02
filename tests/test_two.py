import advent.exercises.two
import pytest


def test_valid_pw():
    inputs = [
        ("a", "abcde", 1, 3, True),
        ("b", "cdefg", 1, 3, False),
        ("c", "ccccccccc", 2, 9, True),
    ]

    for t in inputs:
        print(t)
        res = advent.exercises.two.validate_pw_count(t[0], t[2], t[3], t[1])
        assert(res == t[4])