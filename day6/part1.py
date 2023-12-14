import re
import time

import numpy
from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):
    regex_search = re.match(r'Time: (?P<time>[\d ]*)\nDistance: (?P<distance>[\d ]*)', file_input)
    
    times = numpy.array(regex_search.group('time').split()).astype(int)
    distances = numpy.array(regex_search.group('distance').split()).astype(int)

    return numpy.prod([numpy.count_nonzero((numpy.arange(1, times[i]) * (times[i] - numpy.arange(1, times[i]))) >= distances[i]) for i in range(len(times))])


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
