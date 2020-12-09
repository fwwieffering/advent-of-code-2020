import os.path
from typing import List

from advent.exercises import get_input
from advent.exercises.one import find_sum_two


INPUT_PATH = f'{os.path.dirname(__file__)}/input/nine'


def check_validity(xmas_input: List[int], preamble_size: int = 25) -> (int, int):
    '''
    returns the first item in the list that does not pass the xMas validation
     -> (idx, val)
    '''
    for i in range(preamble_size, len(xmas_input)):
        sum_possibilities = sorted(xmas_input[i-preamble_size:i])
        result = find_sum_two(sum_possibilities, xmas_input[i])
        if not result:
            return (i, xmas_input[i])


def find_contiguous_sum(xmas_input: List[int], goal: int):
    current_sum = 0
    current_range = []

    for i in xmas_input:
        current_range.append(i)
        current_sum += i

        if current_sum == goal:
            return current_range
        elif current_sum > goal:
            # remove items from the front of the current range if we've overshot it
            while current_sum > goal and len(current_range) > 1:
                current_sum -= current_range.pop(0)
                # its possible we find the answer here
                if current_sum == goal:
                    return current_range

    return None


def main():
    xmas_input = [int(x) for x in get_input(INPUT_PATH)]
    part1_res = check_validity(xmas_input)
    print(f"Part 1: first number that is not sum of 2 of 25 precursors: {part1_res[1]}")
    part2_res = sorted(find_contiguous_sum(xmas_input, part1_res[1]))
    print(f"Part 2: min {part2_res[0]} + max {part2_res[-1]} of contiguous sum - {part2_res[0] + part2_res[-1]}")


if __name__ == "__main__":
    main()