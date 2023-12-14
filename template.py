import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):
    answer = None

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