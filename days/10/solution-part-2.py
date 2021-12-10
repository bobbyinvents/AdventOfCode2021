a = open("input.txt", "r").read().strip().split("\n")

opens = "([{<"
closes = ")]}>"

incompleted_lines = []

for line in a:
    pairs = []
    has_error = False
    for i in line:
        if i in opens:
            pairs.append(i)
        elif i in closes:
            open_symbol = opens[closes.index(i)]
            if open_symbol == pairs[-1]:
                pairs = pairs[:-1]
            else:
                has_error = True
                break
    if not has_error and len(pairs) > 0:
        incompleted_lines.append("".join(closes[opens.index(i)] for i in pairs)[::-1])

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

total_scores = []
for line in incompleted_lines:
    score = 0
    for i in line:
        score *= 5
        score += points[i]
    total_scores.append(score)

solution = sorted(total_scores)[(len(total_scores) - 1) // 2]
print(f"part 2: {solution}")
