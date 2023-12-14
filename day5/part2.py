import re
import time

from icecream import ic

from answers import get_answer
from aoc_input import aoc_input_raw
import numpy


def main(file_input):
    file_input = file_input.replace('\n', ' ')
    regex_match = re.match(
        r'seeds: ([\d ]*) seed-to-soil map: (?P<seeds_soil>[\d ]*) soil-to-fertilizer map: (?P<soil_fertilizer>[\d ]*) fertilizer-to-water map: (?P<fertilizer_water>[\d ]*) water-to-light map: (?P<water_light>[\d ]*) light-to-temperature map: (?P<light_temperature>[\d ]*) temperature-to-humidity map: (?P<temperature_humidity>[\d ]*) humidity-to-location map: (?P<humidity_location>[\d ]*)',
        file_input)

    seeds = numpy.array([_ for _ in regex_match.group(1).split()]).reshape(-1, 2).astype(numpy.int64)
    seeds = numpy.reshape(seeds, (-1, 2))
    seeds[:, 1] += seeds[:, 0]

    maps = {key: numpy.array([_ for _ in value.split()]).astype(numpy.int64).reshape(-1, 3) for key, value in regex_match.groupdict().items()}
    for key in maps:
        maps[key][:, 2] += maps[key][:, 0]
        maps[key][:, 1] -= maps[key][:, 0]

    ic(maps)

    conversion2 = ["humidity_location", "temperature_humidity", "light_temperature", "water_light", "fertilizer_water", "soil_fertilizer", "seeds_soil"]

    i = numpy.arange(0, 10000000, dtype=numpy.int64)
    value = i.copy()

    result = numpy.array([])

    for conv in conversion2:
        ic(conv)
        temp_value = value.copy()
        for key in maps[conv]:
            mask = (key[0] <= temp_value) & (temp_value < key[2])
            value[mask] += key[1]

    for seed in seeds:
        mask = (seed[0] <= value) & (value < seed[1])
        result = numpy.concatenate((result, i[mask]))

    return int(numpy.min(result))


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
