from icecream import ic
# import regex as re
import re
from answers import get_answer
from aoc_input import aoc_input


def main(file_input):
    answer = 0

    copies = {}

    for line in file_input:
        answer += 1
        regex_match = re.match(r'Card *(\d*): ([\d ]*) \| ([\d ]*)', line)
        card_id = int(regex_match.group(1))

        winning_numbers = set([_ for _ in regex_match.group(2).split(' ') if _ != ''])
        card_numbers = set([_ for _ in regex_match.group(3).split(' ') if _ != ''])

        in_both = winning_numbers & card_numbers

        if len(in_both) > 0:
            copies.update({i: copies.get(i, 0) + 1 + (1 * copies.get(card_id, 0)) for i in range(card_id + 1, card_id + 1 + len(in_both))})

    answer += sum(copies.values())

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
