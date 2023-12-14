import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input
import regex as re

def main(file_input):
    total = 0
    number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in file_input:
        digits = re.findall(r'\d|one|two|three|four|five|six|seven|eight|nine', line, overlapped=True)
        total += int(str(digits[0] if digits[0].isdigit() else number_dict[digits[0]]) +
                     str(digits[-1] if digits[-1].isdigit() else number_dict[digits[-1]]))

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

