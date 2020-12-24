import os.path
import itertools
from typing import List, Tuple

from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/eleven'


class SeatLayout(object):
    '''
    holds a ferrys seat layout and does actions on them
    '''

    def __init__(self, layout: List[List[str]]):
        self._seats = layout

    def get_seat(self, xidx: int, yidx: int) -> str:
        return self._seats[yidx][xidx]

    def check_seat_part1(self, xidx: int, yidx: int) -> str:
        '''
        for a given seat determines the next state based on the current state
        '''
        cur_state = self.get_seat(xidx, yidx)
        if cur_state == ".":
            return "."
        neighbors = self.get_neighbors_part1(xidx, yidx)
        occupied_count = neighbors.count('#')
        if occupied_count >= 4 and cur_state == '#':
            return 'L'
        if occupied_count == 0 and cur_state == 'L':
            return '#'
        return cur_state

    def check_seat_part2(self, xidx, yidx) -> str:
        cur = self.get_seat(xidx, yidx)
        if cur == ".":
            return cur
        neighbors = self.get_neighbors_part2(xidx, yidx)
        occupied = neighbors.count('#')
        if occupied >= 5 and cur == '#':
            return 'L'
        if occupied == 0 and cur == 'L':
            return '#'
        return cur

    def get_neighbors_part1(self, xidx: int, yidx: int) -> List[str]:
        '''
        gets all adjacent seat values. adjacent is the 8 surrounding (non-floor) seats in a grid

        i.e. n's for x

        n n n
        n x n
        n n n
        '''
        x_idxs = [i for i in range(xidx-1, xidx+2) if i >= 0 and i <= len(self._seats[yidx]) - 1]
        y_idxs = [i for i in range(yidx-1, yidx+2) if i >= 0 and i <= len(self._seats) - 1]
        # print(f"({xidx}, {yidx}) x indexes {x_idxs} y indexes {y_idxs}")
        neighbor_idxs = [z for z in itertools.product(x_idxs, y_idxs) if z != (xidx, yidx)]

        neighbors = []
        for n in neighbor_idxs:
            val = self.get_seat(n[0], n[1])
            # add if not empty
            if val != ".":
                neighbors.append(val)
        return neighbors

    def get_neighbors_part2(self, xidx: int, yidx: int) -> List[str]:
        vectors = [
            (-1, -1),
            (0, -1),
            (1, -1),
            (-1, 0),
            (1, 0),
            (-1, 1),
            (0, 1),
            (1, 1)
        ]
        xmax = len(self._seats[0]) - 1
        ymax = len(self._seats) - 1

        def _get_neighbor(vec: Tuple[int, int]) -> str:
            '''
            travels along vector from (xidx, yidx) to find the first visible seat or
            None
            '''
            cur_x = xidx + vec[0]
            cur_y = yidx + vec[1]
            while (cur_x >= 0 and cur_x <= xmax) and (cur_y >= 0 and cur_y <= ymax):
                # print(f"vector {vec} - at ({cur_x}, {cur_y})")
                s = self.get_seat(cur_x, cur_y)
                if s != '.':
                    return s
                cur_x += vec[0]
                cur_y += vec[1]
            return None
        # remove None from results
        return [x for x in [_get_neighbor(v) for v in vectors] if x]

    def process_rule(self, part: int) -> List[List[str]]:
        '''
        processes the rules on the current layout and returns
        the new layout
        '''
        y_size = len(self._seats)
        x_size = len(self._seats[0])

        res = [[0 for i in range(x_size)] for i in range(y_size)]
        for y in range(y_size):
            for x in range(x_size):
                if part == 1:
                    new_state = self.check_seat_part1(x, y)
                else:
                    new_state = self.check_seat_part2(x, y)
                res[y][x] = new_state
        return res

    def set_seats(self, new_layout):
        '''
        sets the seats
        '''
        self._seats = new_layout

    def equal(self, other_layout):
        return self._seats == other_layout

    def get_final_layout(self, part: int):
        while True:
            next_layout = self.process_rule(part)
            if self.equal(next_layout):
                break
            self.set_seats(next_layout)
        self.set_seats(next_layout)

        return self._seats

    def occupied_seats(self):
        c = 0
        for row in self._seats:
            c += row.count('#')
        return c


def main():
    initial = get_input(INPUT_PATH)
    seats = SeatLayout(initial)

    seats.get_final_layout(1)
    print(f"part 1: occupied seats in final layout: {seats.occupied_seats()}")
    seats_2 = SeatLayout(initial)
    seats_2.get_final_layout(2)
    print(f"part 2: occupied seats in final_layout: {seats_2.occupied_seats()}")


if __name__ == "__main__":
    main()
