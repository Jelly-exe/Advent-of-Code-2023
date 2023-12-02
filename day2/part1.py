from icecream import ic
from aoc_input import aoc_input


class Game:
    def __init__(self, data):
        split_data = data.split(':')
        self.game_number = split_data.split(' ')[1]

        self.round_data = split_data[1].split(';')


def main(file_input):
    cubes = {'red': 12, 'green': 13, 'blue': 14}
    answer = 0
    for game in file_input:
        flag = True
        game_split = game.split(':')
        game_data = game_split[1].split(';')

        for round_data in game_data:
            split_round = round_data.split(',')
            for cube in split_round:
                cube_data = cube.strip().split(' ')
                # ic(game, flag, cube_data)
                match cube_data[1]:
                    case 'red' if cubes['red'] < int(cube_data[0]):
                        flag = False
                        break

                    case 'green' if cubes['green'] < int(cube_data[0]):
                        flag = False
                        break

                    case 'blue' if cubes['blue'] < int(cube_data[0]):
                        flag = False
                        break
            else:
                continue
            break

        if flag:
            answer += int(game_split[0].split(' ')[1])

    return answer


file = aoc_input()
ic(main(file))
