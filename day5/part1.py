import re
import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input_raw, aoc_input
import numpy


def main(file_input):
    file_input = file_input.replace('\n', ' ')
    regex_match = re.match(
        r'seeds: ([\d ]*) seed-to-soil map: (?P<seeds_soil>[\d ]*) soil-to-fertilizer map: (?P<soil_fertilizer>[\d ]*) fertilizer-to-water map: (?P<fertilizer_water>[\d ]*) water-to-light map: (?P<water_light>[\d ]*) light-to-temperature map: (?P<light_temperature>[\d ]*) temperature-to-humidity map: (?P<temperature_humidity>[\d ]*) humidity-to-location map: (?P<humidity_location>[\d ]*)',
        file_input)

    seeds = numpy.array([_ for _ in regex_match.group(1).split(' ') if _ != '']).astype(numpy.int64)
    seeds = numpy.reshape(seeds, (-1, 2))
    print(seeds)
    maps = regex_match.groupdict()

    range_maps = {}
    for key in maps:
        range_maps[key] = numpy.array([], dtype=[('number', numpy.int64), ('value', numpy.int64)])
        maps[key] = numpy.array([_ for _ in maps[key].split(' ') if _ != '']).astype(numpy.int64)
        maps[key] = numpy.reshape(maps[key], (-1, 3))

        # for y in maps[key]:
        #
        #     range_maps[key][(y[1], y[1] + y[2])] = y[0] - y[1]

    conversion = ["seeds_soil", "soil_fertilizer", "fertilizer_water", "water_light", "light_temperature", "temperature_humidity", "humidity_location"]

    locations = []

    for seed in seeds:
        string = f'{seed:5} '
        for conv in conversion:
            for key in range_maps[conv]:
                if key[0] <= seed < key[1]:
                    seed = seed + range_maps[conv][key]
                    string += f'=> {seed:5} '
                    break
            else:
                string += f'=> {seed:5} '

        locations.append(seed)

    return min(locations)


startTime = time.time()
file = aoc_input_raw()
aoc_answer = ic(main(file))
endTime = time.time()

correct_answer = get_answer()
ic(correct_answer)

is_correct = correct_answer == aoc_answer if correct_answer else "Unknown"
ic(is_correct)

run_time = endTime - startTime
ic(run_time)
