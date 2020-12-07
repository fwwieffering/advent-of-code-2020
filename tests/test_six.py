import pytest

from advent.exercises import six


def test_count_questions_or():
    cases = [
        {'input': ['abc'], 'count': 3},
        {'input': ['a', 'b', 'c'], 'count': 3},
        {'input': ['a', 'a', 'a', 'a'], 'count': 1},
        {'input': ['b'], 'count': 1},
        {'input': ['ia','ai','ia','ai'], 'count': 2}
    ]

    for c in cases:
        count = six.count_questions_or(c['input'])
        assert count == c['count']


def test_count_questions_and():
    cases = [
        {'input': ['abc'], 'count': 3},
        {'input': ['a', 'b', 'c'], 'count': 0},
        {'input': ['a', 'a', 'a', 'a'], 'count': 1},
        {'input': ['b'], 'count': 1},
        {'input': ['ia','ai','ia','ai'], 'count': 2}
    ]

    for c in cases:
        count = six.count_questions_and(c['input'])
        assert count == c['count']