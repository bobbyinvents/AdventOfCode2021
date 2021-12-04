import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"


def process_input(file_location: str) -> list[int]:
    with file_location.open() as input_file:
        l = [line.strip() for line in input_file if line.strip()][0].replace(",", " ")
        l = [i for i in l.split()]
        return [*map(int, l)]


def process_input2(file_location: str) -> list[list[list[int]]]:
    with file_location.open() as input_file:
        all_boards = []
        board = []
        for line in input_file:
            if "," in line:
                continue
            if line == "\n":
                all_boards.append(board)
                board = []
            if line.strip():
                board.append([int(i) for i in line.strip().split()])
        all_boards.append(board)

        return all_boards[1:]


def print_first_twenty(input_list: list[str]):
    """Print the first five elements in the list."""
    print("Printing the first 5 elements...")
    print("=" * 60)
    print(input_list[:5])
    print("=" * 60)


def check_bingo(x):
    winning_boards = []
    for board in x:
        for line in board:
            if all(number == -1 for number in line):
                winning_boards.append(board)
        for i in range(len(board[0])):
            if all(line[i] == -1 for line in board):
                winning_boards.append(board)
    return winning_boards


def part_1(x, y, index=0) -> int:
    new_y = []
    new_board = []
    new_line = []
    for board in y:
        for line in board:
            for number in line:
                if number == x[index]:
                    new_line.append(-1)
                else:
                    new_line.append(number)
            new_board.append(new_line)
            new_line = []
        new_y.append(new_board)
        new_board = []

    if check_bingo(y) != []:
        board = check_bingo(y)[0]
        return sum(n for line in board for n in line if n != -1) * x[index - 1]

    return part_1(x, new_y, index + 1)


def part_2(x: list[str], y, index=0, winning_boards=[]) -> int:
    new_y = []
    new_board = []
    new_line = []
    for board in y:
        for line in board:
            for number in line:
                if number == x[index]:
                    new_line.append(-1)
                else:
                    new_line.append(number)
            new_board.append(new_line)
            new_line = []
        new_y.append(new_board)
        new_board = []

    if check_bingo(y) != []:
        bingo_boards = check_bingo(y)
        winning_boards.append([x[index - 1], bingo_boards[0]])
        for board in bingo_boards:
            new_y = [b for b in new_y if b != board]

    if index == len(x) - 1:
        return (
            sum(n for line in winning_boards[-1][1] for n in line if n != -1)
            * winning_boards[-1][0]
        )

    return part_2(x, new_y, index + 1, winning_boards)


if __name__ == "__main__":
    good_input = process_input(puzzle_input)
    good_input2 = process_input2(puzzle_input)
    print_first_twenty(good_input)
    print_first_twenty(good_input2)

    print(f"part 1: {part_1(good_input, good_input2)}")
    print(f"part 2: {part_2(good_input, good_input2)}")
