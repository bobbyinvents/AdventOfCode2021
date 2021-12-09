a = [int(i) for i in open("input.txt", "r").read().strip().split(",")]

b = [0 for _ in range(9)]
for i,v in enumerate(a):
    b[v] += 1

days = 256
print(f"Initial state:\t {b} => {sum(b)} fishes")

for i in range(days):
    c = b[0]
    b = b[1:] + [b[0]]
    b[6] += c
    print(f"After {i+1} day:\t {b} => {sum(b)} fishes")

print(f"part 2: {sum(b)}")
