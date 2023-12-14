import re
import time

from icecream import ic
from aoc_input import aoc_input
from answers import get_answer


def main(file_input):
    total = 0

    for line in file_input:
        digits = re.findall(r'\d', line)
        total += int(digits[0] + digits[-1])

    return total


startTime = time.time()
file = aoc_input()
aoc_answer = ic(main(file))
endTime = time.time()

correct_answer = get_answer()
ic(correct_answer)

is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)

run_time = endTime - startTime
ic(run_time)
