import os.path
import math
from typing import List, Tuple
from collections import defaultdict

from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/ten'


def get_joltage_diffs(jolts: List[int]) -> Tuple[List[int], List[int]]:
    final_jolts = []
    diffs = []
    sorted_jolts = sorted(jolts)
    # wall joltage is 0
    final_jolts.append(0)

    for idx, j in enumerate(sorted_jolts):
        prev_jolt = final_jolts[-1]
        diff = j - prev_jolt

        if diff <= 3:
            diffs.append(diff)
            final_jolts.append(j)

    # laptop joltage is 3 + final
    final_jolts.append(final_jolts[-1] + 3)
    diffs.append(3)
    return final_jolts, diffs


def get_joltage_combos(jolts: List[int]) -> int:
    '''
    "inspired" by https://github.com/wilkotom/AoC2020/blob/master/10/main.py
    '''
    jolts = sorted(jolts)
    paths_to_point = defaultdict(int)
    paths_to_point[0] = 1
    for j in jolts:
        paths_to_point[j] = paths_to_point[j-1] + paths_to_point[j-2] + paths_to_point[j-3]
    return paths_to_point[max(jolts)]


def calculate_part1_diffs(diffs: List[int]) -> int:
    return diffs.count(1) * diffs.count(3)


def main():
    jolts = [int(x) for x in get_input(INPUT_PATH)]

    used_jolts, diffs = get_joltage_diffs(jolts)
    part1 = calculate_part1_diffs(diffs)

    print(f"part1: # of 1 volt diffs * # of 3 volt diffs: {part1}")

    combos = get_joltage_combos(jolts)
    print(f"part2: # of different combinations: {combos}")


if __name__ == "__main__":
    main()
