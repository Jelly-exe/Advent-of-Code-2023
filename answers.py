import os
import pathlib
import sys


def get_answer():
    return answers[pathlib.Path(sys.argv[0]).parts[-2]][pathlib.Path(sys.argv[0]).parts[-1]]


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
    }
}
