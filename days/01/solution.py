import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"


def part_1(x):
    n = 0
    for i in range(len(x) - 1):
        if x[i] < x[i + 1]:
            n += 1
    return n


def part_2(x):
    n = 0
    for i in range(len(x) - 3):
        a = sum([x[i], x[i + 1], x[i + 2]])
        b = sum([x[i + 1], x[i + 2], x[i + 3]])
        if a < b:
            n += 1
    return n


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = [int(line.strip()) for line in input_file if line.strip()]
        print(f"part 1: {part_1(processed_input)}")
        print(f"part 2: {part_2(processed_input)}")
