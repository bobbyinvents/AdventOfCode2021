a = open("input.txt", "r").read().strip().split("\n")

opens = "([{<"
closes = ")]}>"

syntax_errors = []

for line in a:
    pairs = []
    for i in line:
        if i in opens:
            pairs.append(i)
        elif i in closes:
            open_symbol = opens[closes.index(i)]
            if open_symbol == pairs[-1]:
                pairs = pairs[:-1]
            else:
                syntax_errors.append(i)
                break


syntax_error_dict = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

total_syntax_error_score = sum(syntax_error_dict[i] for i in syntax_errors)

print(f"part 1: {total_syntax_error_score}")
