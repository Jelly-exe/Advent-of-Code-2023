def aoc_input():
    with open("input.txt", "r") as file:
        for line in file:
            yield line.strip()