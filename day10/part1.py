import re
import time
from collections import namedtuple

import numpy
from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw

Point = namedtuple("Point", "x y symbol direction")


def main(file_input):
    answer = None
    regex_search = re.search(r'S', file_input.replace('\n', ''))
    file_input_split = file_input.split('\n')

    grid = numpy.array([list(_) for _ in file_input_split])
    width = len(file_input_split[0])
    y = regex_search.start() // width
    x = regex_search.start() % width

    current_pos = None

    if str(grid[y - 1][x]) in '|7F':
        current_pos = Point(x, y, 'S', 'N')
    elif str(grid[y][x + 1]) == '-J7':
        current_pos = Point(x, y, 'S', 'E')
    elif str(grid[y + 1][x]) == '|LJ':
        current_pos = Point(x, y, 'S', 'S')
    elif str(grid[y][x - 1]) == '-LF':
        current_pos = Point(x, y, 'S', 'W')

    previous_position = current_pos

    symbols = {
        '|': 'NS',
        '-': 'EW',
        'L': 'NE',
        'J': 'NW',
        '7': 'SW',
        'F': 'SE',
        'S': 'NESW'
    }
    directions = {
        'N': 'S',
        'E': 'W',
        'S': 'N',
        'W': 'E'
    }

    def get_point(p_grid, p_current_pos):
        if p_current_pos.direction == 'N':
            symbol = p_grid[p_current_pos.y - 1][p_current_pos.x]
            return Point(p_current_pos.x, p_current_pos.y - 1, symbol, symbols[symbol].replace(directions[p_current_pos.direction], ''))

        if p_current_pos.direction == 'E':
            symbol = p_grid[p_current_pos.y][p_current_pos.x + 1]
            return Point(p_current_pos.x + 1, p_current_pos.y, symbol, symbols[symbol].replace(directions[p_current_pos.direction], ''))

        if p_current_pos.direction == 'S':
            symbol = p_grid[p_current_pos.y + 1][p_current_pos.x]
            return Point(p_current_pos.x, p_current_pos.y + 1, symbol, symbols[symbol].replace(directions[p_current_pos.direction], ''))

        if p_current_pos.direction == 'W':
            symbol = p_grid[p_current_pos.y][p_current_pos.x - 1]
            return Point(p_current_pos.x - 1, p_current_pos.y, symbol, symbols[symbol].replace(directions[p_current_pos.direction], ''))

    def is_inside(p_points, p_x, p_y):
        N = (p_x, p_y - 1) in p_points
        S = (p_x, p_y + 1) in p_points
        W = (p_x - 1, p_y) in p_points
        E = (p_x + 1, p_y) in p_points

        return N and S and W and E

    length = 0
    points = []
    while current_pos.symbol != 'S' or current_pos == previous_position:
        previous_position = current_pos
        points.append((current_pos.x, current_pos.y))
        current_pos = get_point(grid, previous_position)
        length += 1

    return int(length / 2)


startTime = time.time()
file = aoc_input_raw()
aoc_answer = ic(main(file))
endTime = time.time()

correct_answer = get_answer()
ic(correct_answer)

is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)

run_time = endTime - startTime
ic(run_time)
