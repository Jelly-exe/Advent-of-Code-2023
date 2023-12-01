from icecream import ic
from aoc_input import aoc_input


def main(file_input):
    total = 0

    for line in file_input:
        first_digit = next(char for char in line if char.isdigit())
        last_digit = next(char for char in reversed(line) if char.isdigit())
        total += int(first_digit + last_digit)

    return total


file = aoc_input()
ic(main(file))
