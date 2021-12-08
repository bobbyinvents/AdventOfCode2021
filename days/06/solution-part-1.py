import numpy as np

a = [int(i) for i in open("input.txt", "r").read().split(",")]
print(a)
total_days = 80
curr_day = 0
fishes = len(a)
for day in range(total_days):
    curr_day = day
    diff = len(a) - fishes
    fishes = len(a)
    print(f"day {curr_day}: {fishes} fishes, +{diff}")
    for i in range(len(a)):
        if a[i] > 0:
            a[i] -= 1
        elif a[i] == 0:
            a[i] = 6
            a.append(8)

print(f"part 1: {len(a)}")
