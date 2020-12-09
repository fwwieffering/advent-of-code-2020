import pytest

from advent.exercises import nine


def test_nine():
    xmas = [35,20,15,25,47,40,62,55,65,95,102,117,150,182,127,219,299,277,309,576]

    res = nine.check_validity(xmas, 5)
    assert res
    assert res[1] == 127

    contiguous_sum = nine.find_contiguous_sum(xmas, res[1])
    assert contiguous_sum
    assert contiguous_sum == [15, 25, 47, 40]
