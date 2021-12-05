import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"


def process_input(file_location: str) -> list[list[list[int]]]:
    with file_location.open() as input_file:
        full_coords = [line.strip().split("->") for line in input_file if line.strip()]
        full_coords = [
            [[*map(int, j.strip().split(","))] for j in i] for i in full_coords
        ]
        return full_coords


def print_first_twenty(input_list: list[str]):
    """Print the first five elements in the list."""
    print("Printing the first 5 elements...")
    print("=" * 60)
    print(input_list[:5])
    print("=" * 60)


def part_1(x):
    width, height = 1000, 1000
    grid = [[0 for i in range(width)] for j in range(height)]
    for s in x:
        point1 = s[0]
        point2 = s[1]
        point1_width = point1[0]
        point1_height = point1[1]

        point2_width = point2[0]
        point2_height = point2[1]

        if point1_width == point2_width or point1_height == point2_height:
            grid[point1_height][point1_width] += 1
            grid[point2_height][point2_width] += 1

        if point1_height == point2_height:
            if point1_width < point2_width:
                for i in range(point1_width + 1, point2_width):
                    point_width = i
                    point_height = point1_height
                    grid[point_height][point_width] += 1
            elif point1_width > point2_width:
                for i in range(point2_width + 1, point1_width):
                    point_width = i
                    point_height = point1_height
                    grid[point_height][point_width] += 1

        if point1_width == point2_width:
            if point1_height < point2_height:
                for i in range(point1_height + 1, point2_height):
                    point_height = i
                    point_width = point1_width
                    grid[point_height][point_width] += 1
            elif point1_height > point2_height:
                for i in range(point2_height + 1, point1_height):
                    point_height = i
                    point_width = point1_width
                    grid[point_height][point_width] += 1

    count = 0
    for i in grid:
        for j in i:
            if j > 1:
                count += 1
    return count


def part_2(x):
    width, height = 1000, 1000
    grid = [[0 for i in range(width)] for j in range(height)]
    for s in x:
        point1 = s[0]
        point2 = s[1]
        point1_width = point1[0]
        point1_height = point1[1]

        point2_width = point2[0]
        point2_height = point2[1]

        grid[point1_height][point1_width] += 1
        grid[point2_height][point2_width] += 1

        if point1_height == point2_height:
            if point1_width < point2_width:
                for i in range(point1_width + 1, point2_width):
                    point_width = i
                    point_height = point1_height
                    grid[point_height][point_width] += 1
            elif point1_width > point2_width:
                for i in range(point2_width + 1, point1_width):
                    point_width = i
                    point_height = point1_height
                    grid[point_height][point_width] += 1
        elif point1_width == point2_width:
            if point1_height < point2_height:
                for i in range(point1_height + 1, point2_height):
                    point_height = i
                    point_width = point1_width
                    grid[point_height][point_width] += 1
            elif point1_height > point2_height:
                for i in range(point2_height + 1, point1_height):
                    point_height = i
                    point_width = point1_width
                    grid[point_height][point_width] += 1
        else:
            if point1_width < point2_width and point1_height < point2_height:
                a = point1_height + 1
                b = point1_width + 1
                c = point2_height
                while a < c:
                    grid[a][b] += 1
                    a += 1
                    b += 1
            elif point1_width > point2_width and point1_height > point2_height:
                a = point1_height - 1
                b = point1_width - 1
                c = point2_height
                while a > c:
                    grid[a][b] += 1
                    a -= 1
                    b -= 1
            elif point1_width < point2_width and point1_height > point2_height:
                a = point1_height - 1
                b = point1_width + 1
                c = point2_height
                while a > c:
                    grid[a][b] += 1
                    a -= 1
                    b += 1
            elif point1_width > point2_width and point1_height < point2_height:
                a = point1_height + 1
                b = point1_width - 1
                c = point2_height
                while a < c:
                    grid[a][b] += 1
                    a += 1
                    b -= 1
    count = 0
    for i in grid:
        for j in i:
            if j > 1:
                count += 1
    return count


if __name__ == "__main__":
    good_input = process_input(puzzle_input)
    print_first_twenty(good_input)

    print(f"part 1: {part_1(good_input)}")
    print(f"part 2: {part_2(good_input)}")
