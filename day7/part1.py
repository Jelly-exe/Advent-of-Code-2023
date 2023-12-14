import time

from icecream import ic
import re
from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw
import regex_spm


def main(file_input):
    five_of_a_kind = re.compile(r'([2-9TJQKA])\1{4}')  # 6
    four_of_a_kind = re.compile(r'([2-9TJQKA])\1{3}')  # 5
    full_house = re.compile(r'([2-9TJQKA])\1{2}([2-9TJQKA])\2|([2-9TJQKA])\3([2-9TJQKA])\4{2}')  # 4
    three_of_a_kind = re.compile(r'([2-9TJQKA])\1{2}')  # 3
    two_pairs = re.compile(r'([2-9TJQKA])\1([2-9TJQKA])\2|([2-9TJQKA])\3[2-9TJQKA]([2-9TJQKA])\4')  # 2
    one_pair = re.compile(r'([2-9TJQKA])\1')  # 1

    hands = []
    dict_card = {
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    for line in file_input:
        line = line.strip()

        cards, bet = line.split(' ')
        regex_cards = ''.join(sorted(cards))

        if five_of_a_kind.search(regex_cards):
            hands.append((7, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        elif four_of_a_kind.search(regex_cards):
            hands.append((6, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        elif full_house.search(regex_cards):
            hands.append((5, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        elif three_of_a_kind.search(regex_cards):
            hands.append((4, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        elif two_pairs.search(regex_cards):
            hands.append((3, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        elif one_pair.search(regex_cards):
            hands.append((2, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

        else:
            hands.append((1, tuple(int(_) if _.isdigit() else dict_card[_] for _ in cards), int(bet)))

    print(sorted(hands, reverse=True, key=lambda x: (x[0], x[1])))
    answer = sum([_[2] * (i + 1) for i, _ in enumerate(reversed(sorted(hands, reverse=True, key=lambda x: (x[0], x[1]))))])

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
