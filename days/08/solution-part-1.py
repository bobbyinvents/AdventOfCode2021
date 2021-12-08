import numpy as np

a = np.array(
    [
        line.split("|")[1].strip().split()
        for line in open("input.txt", "r").read().split("\n")
    ]
).flatten()

count = 0
for i in a:
    if len(i) in [2, 3, 4, 7]:
        count += 1

print(f"part one: {count}")
