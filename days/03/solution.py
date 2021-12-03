from operator import mul
from typing import TextIO
import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"


def process_input(file_location: str) -> list[str]:
    """Remove whitespaces from input file and add to list."""
    with file_location.open() as input_file:
        return [line.strip() for line in input_file if line.strip()]


def print_first_twenty(input_list: list[str]):
    """Print the first five elements in the list."""
    print("Printing the first 5 elements...")
    print("=" * 60)
    print(input_list[:5])
    print("=" * 60)


def part_1(report: list[str]) -> int:
    """Get the gamma rate and epsilon rate from the diagnostic report and multiply them after converting from binary to decimal."""

    gamma = ""
    for i in range(len(report[0])):
        ones = sum(number[i] == "1" for number in report)
        zeros = len(report) - ones
        gamma += str(int(ones > zeros))
    epsilon = "".join({"1": "0", "0": "1"}[i] for i in gamma)
    return mul(*map(lambda y: int(y, 2), (gamma, epsilon)))


def part_2(x: list[str]) -> int:
    """Get the oxygen generator rating and the CO2 scrubber rating from the diagnostic report and multiply them after converting from binary to decimal."""

    def oxygen_generator(numbers, index=0):
        """To find oxygen generator rating, determine the most common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 1 in the position being considered."""

        return rating_system(numbers, 1, index)

    def co2_scrubber(numbers, index=0):
        """To find CO2 scrubber rating, determine the least common value (0 or 1) in the current bit position, and keep only numbers with that bit in that position. If 0 and 1 are equally common, keep values with a 0 in the position being considered."""

        return rating_system(numbers, 0, index)

    def rating_system(numbers, common_bit, index=0):
        if len(numbers) == 1:
            return numbers[0]

        zeros = sum(i[index] == "0" for i in numbers)
        ones = len(numbers) - zeros
        least_common_bit, most_common_bit = ones < zeros, ones >= zeros
        new_numbers = [
            *filter(
                lambda x: int(x[index])
                == (least_common_bit, most_common_bit)[common_bit],
                numbers,
            )
        ]
        return rating_system(new_numbers, common_bit, index + 1)

    return mul(*map(lambda y: int(y, 2), (oxygen_generator(x), co2_scrubber(x))))


if __name__ == "__main__":
    good_input = process_input(puzzle_input)
    print_first_twenty(good_input)
    print(f"part 1: {part_1(good_input)}")
    print(f"part 2: {part_2(good_input)}")
