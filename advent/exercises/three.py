from typing import List
import os.path
import functools
from advent.exercises import get_input


INPUT_PATH = f'{os.path.dirname(__file__)}/input/three'

class Vector(object):

    def __init__(self, coord_x: int, coord_y: int):
        self.current = (0, 0)
        self.x = coord_x
        self.y = coord_y

    def step(self):
        self.current = (self.current[0] + self.x, self.current[1] + self.y)
        return self.current


class TreeCollection(object):

    def __init__(self, input_lines: List[str]):
        self.size_x = len(input_lines[0])
        self.size_y = len(input_lines)

        self.trees = []
        for line in input_lines:
            cur_line = []
            for idx, char in enumerate(line):
                if char == "#":
                    cur_line.append(idx)
            self.trees.append(cur_line)

    def check_intersection(self, x: int, y: int) -> bool:
        cur_line = self.trees[y]
        for tree in cur_line:
            if tree > x: # fast fail
                return False
            else:
                # x = size_x * repeat_number + tree
                # (x - tree) / size_x = repeat_number
                repeat_number = (x - tree) % self.size_x
                if repeat_number == 0: # evenly divides
                    return True

        return False #default


def find_intersections(obstacles: TreeCollection, vec: Vector) -> int:
    collisions = 0
    while vec.current[1] <= obstacles.size_y - 1:
        if obstacles.check_intersection(vec.current[0], vec.current[1]):
            collisions += 1
        vec.step()

    return collisions


def main():
    str_input = get_input(INPUT_PATH)

    trees = TreeCollection(str_input)
    vectors = [Vector(3, 1), Vector(1, 1), Vector(5, 1), Vector(7, 1), Vector(1, 2)]
    collisions = [find_intersections(trees, x) for x in vectors]

    print(f"Part 1: you would hit {collisions[0]} trees")
    print(f"part 2: multiplied all together this is {functools.reduce(lambda a,b: a * b, collisions)}")


if __name__ == "__main__":
    main()