import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input, aoc_input_raw


def main(file_input):
    answer = 0
    for line in file_input:
        sequences = {0: [int(_) for _ in line.split(' ')]}

        depth = 0
        while not all(_ == 0 for _ in sequences[depth]):
            sequences[depth + 1] = [sequences[depth][i + 1] - sequences[depth][i] for i in range(0, len(sequences[depth]) - 1)]
            depth += 1

        for i in range(len(sequences) - 1, 0, -1):
            sequences[i - 1].append(sequences[i - 1][-1] + sequences[i][-1])

        answer += sequences[0][-1]

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
