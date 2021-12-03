import pathlib

puzzle_input = pathlib.Path(__file__).parent / "input.txt"


def func_1(x):
    h = 0
    d = 0
    for i in x:
        if i[0]=="f":
            h+=int(i[-1])
        elif i[0]=="d":
            d+=int(i[-1])
        elif i[0]=="u":
            d-=int(i[-1])
    return h*d



def func_2(x):
    h = 0
    d = 0
    a = 0
    for i in x:
        if i[0]=="f":
            h+=int(i[-1])
            d+=(a*int(i[-1]))
        elif i[0]=="d":
            a+=int(i[-1])
        elif i[0]=="u":
            a-=int(i[-1])
    return h*d


if __name__ == "__main__":
    with puzzle_input.open() as input_file:
        processed_input = [line.strip() for line in input_file if line.strip()]
        print(processed_input)
        print(f"part 1: {func_1(processed_input)}")
        print(f"part 2: {func_2(processed_input)}")
