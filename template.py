from icecream import ic

from answers import get_answer
from aoc_input import aoc_input


def main(file_input):
    answer = None

    return answer


file = aoc_input()
aoc_answer = ic(main(file))
correct_answer = get_answer()
is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)
