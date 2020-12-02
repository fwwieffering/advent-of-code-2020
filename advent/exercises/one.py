from typing import List, Tuple
import os.path
from advent.exercises import get_input

INPUT_PATH = f'{os.path.dirname(__file__)}/input/one'


# expects items to be in ascending order
def _find_sum_recurse(idxA, idxB, items, goal):
    # no hits
    if idxA == idxB:
        return None
    a = items[idxA]
    b = items[idxB]
    # hit
    if a + b == goal:
        return a, b
    elif a + b > goal:
        # too much. move b down
        return _find_sum_recurse(idxA, idxB -1, items, goal)
    else: # less than goal
        return _find_sum_recurse(idxA+1, idxB, items, goal)


# expects a sorted input
def find_sum_two(items: List[int], goal: int) -> Tuple[int, int]:
    return _find_sum_recurse(0, len(items) - 1, items, goal)


def find_sum_three(items: List[int], goal: int) -> Tuple[int, int, int]:
    for idx, item in enumerate(items):
        itemsCopy = [ x for (i, x) in enumerate(items) if i != idx]
        potential_answer = find_sum_two(itemsCopy, goal - item)
        if potential_answer:
            return item, potential_answer[0], potential_answer[1]


def main():
    dayOneInput = [int(x) for x in get_input(INPUT_PATH)]
    # sort array. then we can know if we've gone too far
    sortedInput = sorted(dayOneInput)

    answer = find_sum_two(sortedInput, 2020)
    if answer:
        print(f"Two entries that sum to 2020: {answer[0], answer[1]}")
        print(f"Part 1 answer: {answer[0] * answer[1]}")
    else:
        print("couldnt find a match")
    part2 = find_sum_three(sortedInput, 2020)
    if part2:
        print(f"three entries that sum to {part2}")
        print(f"part two answer: {part2[0] * part2[1] * part2[2]}")


if __name__ == "__main__":
    main()