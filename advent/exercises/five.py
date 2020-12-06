import os.path
from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/five'

def get_num(s: str) -> int:
    bit_str = ''
    for c in s:
        if c in ['B', 'R']:
            bit_str += '1'
        else:
            bit_str += '0'
    return int(bit_str, 2)


def get_row_col_id(ticket: str):
    row_str = ticket[0:7]
    seat_str = ticket[7:]
    row = get_num(row_str)
    col = get_num(seat_str)
    return row, col, (row * 8) + col


def main():
    tickets = get_input(INPUT_PATH)
    highest_seat_id = 0
    lowest_seat_id = -1
    sum_seat_id = 0
    seats = []

    for t in tickets:
        row, col, seat_id = get_row_col_id(t)
        sum_seat_id += seat_id
        if seat_id > highest_seat_id:
            highest_seat_id = seat_id
        if seat_id < lowest_seat_id or lowest_seat_id == -1:
            lowest_seat_id = seat_id
        seats.append((row, col, seat_id))

    part2 = (highest_seat_id*(highest_seat_id+1)/2)-(lowest_seat_id*(lowest_seat_id+1)/2) - sum_seat_id
    sorted_seats = sorted(seats, key=lambda x: x[2])
    missing_seat = 0
    for i, s in enumerate(sorted_seats):
        if sorted_seats[i+1][2] - s[2] > 1:
            missing_seat = s[2] + 1
            break

    print(f"Part1: highest seat id: {highest_seat_id}")
    print(f"Part2: your seat id: {missing_seat}")


if __name__ == "__main__":
    main()