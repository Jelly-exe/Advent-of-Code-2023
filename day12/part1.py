import fileinput
import itertools
import re
import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):

    answer = 0
    for line in file_input:
        springs, correct = re.match(r'([.#?]+) ([\d,?]+)', line).groups()
        correct = [int(_) for _ in correct.split(',')]

        for combo in itertools.product(['.', '#'], repeat=springs.count('?')):
            if [len(_) for _ in springs.replace('?', '{}').format(*combo).split('.') if _ != ''] == correct:
                answer += 1

    return answer


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