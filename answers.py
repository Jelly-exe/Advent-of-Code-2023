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
}
