import re
import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):
    instructions, letter_map = file_input.split("\n\n")
    letter_map = letter_map.split("\n")
    maps = {}
    for x in letter_map:
        regex_search = re.search(r'(?P<key>[A-Z]{3}) = \((?P<L>[A-Z]{3}), (?P<R>[A-Z]{3})\)', x)

        maps[regex_search.group('key')] = (regex_search.group('L'), regex_search.group('R'))

    current_key = 'AAA'
    count = 0
    while current_key != 'ZZZ':
        for inst in instructions:
            count += 1
            current_key = maps[current_key][0 if inst == "L" else 1]
            if current_key == "ZZZ":
                break

    return count


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