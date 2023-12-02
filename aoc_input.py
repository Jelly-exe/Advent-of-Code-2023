def aoc_input(file_name="input.txt"):
    with open(file_name, "r") as file:
        for line in file:
            yield line.strip()