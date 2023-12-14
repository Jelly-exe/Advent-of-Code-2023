import time

from icecream import ic
import re
from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw
import regex_spm


def main(file_input):
    cards_dict = {'A': 14, 'K': 13, 'Q': 12, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'J': 1}

    five_of_a_kind = re.compile(r'([2-9TJQKA])\1{4}')  # 6
    four_of_a_kind = re.compile(r'([2-9TJQKA])\1{3}')  # 5
    full_house = re.compile(r'([2-9TJQKA])\1{2}([2-9TJQKA])\2|([2-9TJQKA])\3([2-9TJQKA])\4{2}')  # 4
    three_of_a_kind = re.compile(r'([2-9TJQKA])\1{2}')  # 3
    two_pairs = re.compile(r'([2-9TJQKA])\1([2-9TJQKA])\2|([2-9TJQKA])\3[2-9TJQKA]([2-9TJQKA])\4')  # 2
    one_pair = re.compile(r'([2-9TJQKA])\1')  # 1

    def regex_check(thing):

        regex_cards = ''.join(sorted(thing, key=lambda x: cards_dict[x], reverse=True))

        if five_of_a_kind.search(regex_cards):
            return 7

        if four_of_a_kind.search(regex_cards):
            return 6

        if full_house.search(regex_cards):
            return 5

        if three_of_a_kind.search(regex_cards):
            return 4

        if two_pairs.search(regex_cards):
            return 3

        if one_pair.search(regex_cards):
            return 2

        return 1

    return sum([_[2] * (i + 1) for i, _ in enumerate(reversed(sorted([(max([regex_check(line.split(' ')[0].replace("J", _)) for _ in cards_dict]), tuple(cards_dict[_] for _ in line.split(' ')[0]), int(line.split(' ')[1])) for line in file_input], reverse=True, key=lambda x: (x[0], x[1]))))])


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
