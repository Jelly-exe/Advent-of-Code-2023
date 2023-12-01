import re
from icecream import ic

from aoc_input import aoc_input


def main(file_input):
    total = 0
    number_dict = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    pattern = re.compile(r'^.*?(\d|one|two|three|four|five|six|seven|eight|nine)')
    reverse_pattern = re.compile(r'^.*?(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)')

    for line in file_input:
        first_digit = value if (value := pattern.search(line).group(1)).isdigit() else number_dict[value]
        last_digit = value if (value := reverse_pattern.search(line[::-1]).group(1)).isdigit() else number_dict[value[::-1]]

        total += int(first_digit + last_digit)

    return total


file = aoc_input()
ic(main(file))

