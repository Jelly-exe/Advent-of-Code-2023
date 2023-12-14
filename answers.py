import os
import pathlib
import sys


def get_answer():
    try:
        return answers[pathlib.Path(sys.argv[0]).parts[-2]][pathlib.Path(sys.argv[0]).parts[-1]]
    except:
        return None


answers = {
    'day1': {
        'part1.py': 54573,
        'part2.py': 54591
    },
    'day2': {
        'part1.py': 2207,
        'part2.py': 62241
    },
    'day3': {
        'part1.py': 514969,
        'part2.py': None
    },
    'day4': {
        'part1.py': 22897,
        'part2.py': 5095824
    },
    'day5': {
        'part1.py': 199602917,
        'part2.py': 2254686
    },
    'day6': {
        'part1.py': 1083852,
        'part2.py': 23501589
    },
    'day7': {
        'part1.py': 253205868,
        'part2.py': 253907829
    },
    'day8': {
        'part1.py': 21797,
        'part2.py': 23977527174353
    },
    'day9': {
        'part1.py': 1637452029,
        'part2.py': 908
    },
    'day10': {
        'part1.py': 6828,
        'part2.py': None
    },
    'day11': {
        'part1.py': 9312968,
        'part2.py': 597714117556
    },
    'day12': {
        'part1.py': 7195,
        'part2.py': None
    },
    'day13': {
        'part1.py': None,
        'part2.py': None
    },
    'day14': {
        'part1.py': None,
        'part2.py': None
    }
}
