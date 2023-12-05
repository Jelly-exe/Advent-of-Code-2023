from icecream import ic
# import regex as re
import re
from answers import get_answer
from aoc_input import aoc_input


def main(file_input):
    answer = 0

    for line in file_input:
        regex_match = re.match(r'Card *(\d*): ([\d ]*) \| ([\d ]*)', line)
        winning_numbers = set([_ for _ in regex_match.group(2).split(' ') if _ != ''])
        card_numbers = set([_ for _ in regex_match.group(3).split(' ') if _ != ''])

        in_both = winning_numbers & card_numbers

        if len(in_both) > 0:
            answer += (2 ** (len(in_both) - 1))

    return answer


file = aoc_input()
aoc_answer = ic(main(file))

correct_answer = get_answer()
ic(correct_answer)

is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)
