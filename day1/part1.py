import re

from icecream import ic
from aoc_input import aoc_input
from answers import get_answer


def main(file_input):
    total = 0

    for line in file_input:
        digits = re.findall(r'\d', line)
        total += int(digits[0] + digits[-1])

    return total


file = aoc_input()
aoc_answer = ic(main(file))
correct_answer = get_answer()
is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)
