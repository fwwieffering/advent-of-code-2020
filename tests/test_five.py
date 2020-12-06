import pytest
from advent.exercises import five


def test_seat_row():
    cases = [
        {
            'ticket': 'FBFBBFFRLR',
            'row': 44,
            'col': 5,
            'seat_id': 357
        },
        {
            'ticket': 'BFFFBBFRRR',
            'row': 70,
            'col': 7,
            'seat_id': 567
        },
        {
            'ticket': 'BBFBBBBLLL',
            'row': 102,
            'col': 4,
            'seat_id': 820
        },
    ]
    for c in cases:
        row, col, seat_id = five.get_row_col_id(c['ticket'])

        assert c['row'] == row
        assert c['col'] == col
        assert c['seat_id'] == seat_id
