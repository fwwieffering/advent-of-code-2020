from typing import Tuple
import os.path
import re
from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/two'

pw_policy_regex = re.compile(r'^(?P<lower_bound>\d+)-(?P<upper_bound>\d+) (?P<char>[a-z]): (?P<pw>[a-z]+)$')

# example password input: '1-3 a: abcde'
# returns [lower_bound_repitition, upper_bound_repitition, repeating_char, pw]
def parse_pw_and_policy(ipt: str) -> Tuple[int, int, str, str]:
    match = pw_policy_regex.match(ipt)
    if not match:
        raise ValueError(f"{ipt} did not match regex")
    return (int(match.group('lower_bound')), int(match.group('upper_bound')), match.group('char'), match.group('pw'))


def _count_chars(ipt: str, char: str, count: int) -> int:
    if len(ipt) == 0:
        return count

    if char == ipt[0]:
        count += 1

    return _count_chars(ipt[1:], char, count)


def validate_pw_count(char: str, lower_bound: int, upper_bound: int, pw: str) -> bool:
    char_count = _count_chars(pw, char, 0)
    return lower_bound <= char_count <= upper_bound


def validate_pw_index(char: str, idx1: int, idx2: int, pw: str) -> bool:
    idx1Valid = len(pw) >= idx1 and pw[idx1-1] == char
    idx2Valid = len(pw) >= idx2 and pw[idx2-1] == char
    return xor(idx1Valid, idx2Valid)


def xor(a: bool, b: bool) -> bool:
    return (a or b) and not (a and b)


def main():
    day2Input = get_input(INPUT_PATH)

    valid_count_1 = 0
    valid_count_2 = 0
    for item in day2Input:
        lower_bound, upper_bound, char, pw = parse_pw_and_policy(item)
        is_valid_1 = validate_pw_count(char, lower_bound, upper_bound, pw)
        is_valid_2 = validate_pw_index(char, lower_bound, upper_bound, pw)
        if is_valid_1:
            valid_count_1 += 1
        if is_valid_2:
            valid_count_2 += 1

    print(f"Part 1: valid password count: {valid_count_1}")
    print(f"Part 2: valid password count: {valid_count_2}")

if __name__ == "__main__":
    main()