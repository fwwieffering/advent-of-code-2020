import pytest
from advent.exercises import ten


def test_ten():
    small_example = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
    small_jolts, small_diffs = ten.get_joltage_diffs(small_example)
    assert small_jolts == [0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22]
    assert small_diffs == [1, 3, 1, 1, 1, 3, 1, 1, 3, 1, 3, 3]
    small_answer = ten.calculate_part1_diffs(small_diffs)
    assert small_answer == 35
    assert ten.get_joltage_combos(small_example) == 8

    example = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]
    jolts, diffs = ten.get_joltage_diffs(example)
    answer = ten.calculate_part1_diffs(diffs)
    assert answer == 220
    assert ten.get_joltage_combos(example) == 19208

