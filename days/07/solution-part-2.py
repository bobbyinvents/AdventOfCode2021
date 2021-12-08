import numpy as np

a = np.array([int(i) for i in open("input.txt", "r").read().split(",")])

b = []
for i in range(max(a)):
    total_fuel_used = 0
    print(f"{i/(max(a)-1):.1%}: Checking position {i} of {max(a)-1}...")
    for j in a:
        fuel_used = sum(i for i in range(abs(j - i) + 1))
        total_fuel_used += fuel_used
    b.append(total_fuel_used)

print(f"part 2: {min(b)}")
