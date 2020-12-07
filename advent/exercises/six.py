import os.path
from typing import List

INPUT_PATH = f'{os.path.dirname(__file__)}/input/six'

# 26 len mask
MASK = 0b11111111111111111111111111

def char_to_bitmask(c: str) -> int:
    idx = ord(c[0]) - ord('a')
    return 0b1 << (26 - idx)


def load_groups() -> List[List[str]]:
    with open(INPUT_PATH, 'r') as f:
        content = f.read()

    return [x.split('\n') for x in content.split('\n\n')]


# def count_questions_group(group: List[str]):
#     chars = {}
#     for member in group:
#         for q in member:
#             chars[q] = True

#     return len(chars.keys())


def count_questions_or(group: List[str]):
    count = 0b0
    for member in group:
        for q in member:
            count = count | char_to_bitmask(q)

    # count the positive bits... a little hacky
    return bin(count).count("1")


def count_questions_and(group: List[str]):
    count = 0b111111111111111111111111111
    for member in group:
        cur_member = 0b0
        for q in member:
            cur_member = cur_member | char_to_bitmask(q)
        count = count & cur_member

    # count the positive bits... a little hacky
    return bin(count).count("1")


def main():
    groups = load_groups()

    sum_and = 0
    sum_or = 0
    for g in groups:
        count = count_questions_or(g)
        sum_or += count
        count_and = count_questions_and(g)
        sum_and += count_and

    print(f"Part1: sum of each groups answered questiosn: {sum_or}")
    print(f"Part2: sum of each groups questions that everyone answered: {sum_and}")


if __name__ == "__main__":
    main()