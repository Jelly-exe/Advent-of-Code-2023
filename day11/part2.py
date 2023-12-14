import re
import time
from collections import namedtuple

import numpy
from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw

Point = namedtuple("Point", "x y")


def main(file_input):
    temp = file_input.split("\n")
    starmap = numpy.array([_ for _ in file_input if _ != "\n"]).reshape((len(temp), len(temp[0])))

    for y, row in enumerate(starmap):
        if numpy.all((row == '.') | (row == '*')):
            starmap[y, :] = '*'

    starmap = starmap.T
    for y, col in enumerate(starmap):
        if numpy.all((col == '.') | (col == '*')):
            starmap[y, :] = '*'
    starmap = starmap.T

    answer = 0
    flat_starmap = ''.join(''.join(_ for _ in __) for __ in starmap)
    galaxies_done = []

    for galaxy1 in re.finditer('#', flat_starmap):
        for galaxy2 in re.finditer('#', flat_starmap):
            if galaxy1.start() == galaxy2.start() or galaxy2.start() in galaxies_done:
                continue

            galaxy1_pos, galaxy2_pos = Point(galaxy1.start() % starmap.shape[1], galaxy1.start() // starmap.shape[1]), Point(galaxy2.start() % starmap.shape[1], galaxy2.start() // starmap.shape[1])
            x_distance, y_distance = galaxy2_pos.x - galaxy1_pos.x, galaxy2_pos.y - galaxy1_pos.y

            answer += abs(x_distance) + abs(y_distance)
            for y in range(0, y_distance, -1 if y_distance < 0 else 1):
                if starmap[galaxy1_pos.y + y][galaxy1_pos.x] == '*':
                    answer += 999999

            for x in range(0, x_distance, -1 if x_distance < 0 else 1):
                if starmap[galaxy1_pos.y][galaxy1_pos.x + x] == '*':
                    answer += 999999

        galaxies_done.append(galaxy1.start())

    return answer


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
