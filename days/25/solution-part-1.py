import numpy as np

a = np.array([[j for j in i] for i in open("input.txt", "r").read().split("\n")])

steps = 0
height, width = len(a), len(a[0])
b = c = np.array([["." for j in i] for i in a])
is_there_movement = any(c[i][j] != a[i][j] for i in range(height) for j in range(width))


while is_there_movement:
    b = np.array([i for i in a])
    c = np.array([i for i in a])
    for row in range(height):
        for col in range(width):
            if a[row][col] == ">":
                if col < width - 1:
                    if a[row][col + 1] == ".":
                        b[row][col + 1] = ">"
                        b[row][col] = "."
                elif a[row][0] == ".":
                    b[row][0] = ">"
                    b[row][col] = "."
            else:
                pass

    a = np.array([i for i in b])

    for row in range(height):
        for col in range(width):
            if a[row][col] == "v":
                if row < height - 1:
                    if a[row + 1][col] == ".":
                        b[row + 1][col] = "v"
                        b[row][col] = "."
                elif a[0][col] == ".":
                    b[0][col] = "v"
                    b[row][col] = "."
            else:
                pass

    a = np.array([i for i in b])
    is_there_movement = any(
        c[i][j] != a[i][j] for i in range(height) for j in range(width)
    )
    steps += 1
    print(f"{steps}...")

print(f"part 1: {steps}")
