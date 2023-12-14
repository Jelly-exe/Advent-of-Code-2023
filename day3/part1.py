import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input


def main(file_input):
    characters = {'#', '$', '+', '=', '%', '/', '&', '-', '@', '*'}
    answer = 0

    input_grid = [[char for char in line] for line in file_input]

    number_length = -1
    number = ""

    for file_y, line in enumerate(input_grid):
        for file_x, char in enumerate(line):

            if number_length >= 0:
                if char.isdigit():
                    number_length += 1
                    number += char

                    if not file_x + 1 >= len(input_grid[file_y]):
                        continue

                for search_y in range(max(0, file_y - 1), min(len(input_grid), file_y + 2)):
                    for search_x in range(max(0, file_x - number_length - 2), min(len(input_grid[0]), file_x + 1)):
                        if input_grid[search_y][search_x] in characters:
                            print(int(number))
                            answer += int(number)
                            break
                    else:
                        continue
                    break

                number_length = -1
                number = ""


            elif char.isdigit():
                number_length = 0
                number += char
                continue

    # # ic(numbers)
    # for num in numbers:
    #     print(f'[{num["y_range"][0]}, {num["x_range"][0]}]')
    #     for i in range(num["y_range"][0], num["y_range"][1]):
    #         string = ""
    #         for j in range(num["x_range"][0], num["x_range"][1]):
    #             string += input_grid[i][j]
    #
    #         print(string)

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
