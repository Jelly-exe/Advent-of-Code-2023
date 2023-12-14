import math
import re
import time
from itertools import cycle

import numpy
from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):
    instructions, letter_map = file_input.split("\n\n")

    maps = {
        key: (left, right)
        for key, left, right
        in re.findall(r'(?P<key>\w{3}) = \((?P<L>\w{3}), (?P<R>\w{3})\)', letter_map)
    }
    current_keys = [key for key in maps if key[2] == 'A']

    iterations = []
    for key in current_keys:
        for count, inst in enumerate(cycle(instructions), start=1):
            key = maps[key][0 if inst == "L" else 1]
            if key[2] == 'Z':
                iterations.append(count)
                break

    return math.lcm(*iterations)


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