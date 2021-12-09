import numpy as np

a = np.array(
    [[int(j) for j in i] for i in open("input.txt", "r").read().strip().split("\n")]
)
print(a)


def is_lowest_among_neighbors(row, col):
    neighbors = []
    # top neighbor
    if row > 0:
        top = a[row - 1][col]
        neighbors.append(top)
    # left neighbor
    if col > 0:
        left = a[row][col - 1]
        neighbors.append(left)
    # right neighbor
    if col < cols - 1:
        right = a[row][col + 1]
        neighbors.append(right)
    # bottom neighbor
    if row < rows - 1:
        bottom = a[row + 1][col]
        neighbors.append(bottom)

    return all(a[row][col] < i for i in neighbors)


rows, cols = len(a), len(a[0])
lowest_points = []
for i in range(rows):
    for j in range(cols):
        if is_lowest_among_neighbors(i, j):
            lowest_points.append(a[i][j])


solution = sum(i + 1 for i in lowest_points)
print(f"part 1: {solution}")
