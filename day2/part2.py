from icecream import ic
from aoc_input import aoc_input


class Game:
    def __init__(self, data):
        split_data = data.split(':')
        self.game_number = split_data.split(' ')[1]

        self.round_data = split_data[1].split(';')


def main(file_input):

    answer = 0
    for game in file_input:
        cubes = {'red': 0, 'green': 0, 'blue': 0}
        game_split = game.split(':')
        game_data = game_split[1].split(';')

        for round_data in game_data:
            split_round = round_data.split(',')
            for cube in split_round:
                cube_data = cube.strip().split(' ')

                match cube_data[1]:
                    case 'red' if cubes['red'] < int(cube_data[0]):
                        cubes['red'] = int(cube_data[0])

                    case 'green' if cubes['green'] < int(cube_data[0]):
                        cubes['green'] = int(cube_data[0])

                    case 'blue' if cubes['blue'] < int(cube_data[0]):
                        cubes['blue'] = int(cube_data[0])

        ic(game, cubes, cubes['red'] * cubes['green'] * cubes['blue'])
        answer += cubes['red'] * cubes['green'] * cubes['blue']

    return answer


file = aoc_input()
ic(main(file))
