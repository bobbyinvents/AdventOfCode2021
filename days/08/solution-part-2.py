import numpy as np

a = np.array(
    [
        [i.strip().split() for i in line.split("|")]
        for line in open("input.txt", "r").read().strip().split("\n")
    ],
    dtype=object,
)

total = 0
for display in a:
    n = np.empty(10, dtype=object)
    five_segments = []
    six_segments = []
    segment_a_to_g = np.empty(7, dtype="U64")
    for signal in display[0]:
        segments = len(signal)
        if segments == 2:
            n[1] = signal
        elif segments == 3:
            n[7] = signal
        elif segments == 4:
            n[4] = signal
        elif segments == 7:
            n[8] = signal
        elif segments == 5:
            five_segments.append(signal)
        elif segments == 6:
            six_segments.append(signal)

    # segment a
    segment_a_to_g[0] = next(i for i in (set(n[7]) - set(n[1])))

    # segment b
    segment_a_to_g[1] = next(i for i in n[4] if "".join(five_segments).count(i) == 1)
    n[5] = next(i for i in five_segments if segment_a_to_g[1] in i)

    # segment d
    segment_a_to_g[3] = next(i for i in n[4] if "".join(five_segments).count(i) == 3)

    # segment e
    segment_a_to_g[4] = next(
        i
        for i in set("".join(five_segments))
        if "".join(five_segments).count(i) == 1 and i not in n[4]
    )

    # segment c
    segment_a_to_g[6] = next(
        i
        for i in set("".join(five_segments))
        if "".join(five_segments).count(i) == 3
        and i not in [segment_a_to_g[0], segment_a_to_g[3]]
    )

    # segment f
    segment_a_to_g[5] = "".join(
        i
        for i in set("".join(six_segments))
        if i
        not in [
            segment_a_to_g[0],
            segment_a_to_g[1],
            segment_a_to_g[3],
            segment_a_to_g[4],
            segment_a_to_g[6],
        ]
        and "".join(six_segments).count(i) == 3
    )

    # segment g
    segment_a_to_g[2] = "".join(
        i
        for i in set("".join(six_segments))
        if i
        not in [
            segment_a_to_g[0],
            segment_a_to_g[1],
            segment_a_to_g[3],
            segment_a_to_g[4],
            segment_a_to_g[6],
        ]
        and "".join(six_segments).count(i) == 2
    )

    a, b, c, d, e, f, g = [*segment_a_to_g]
    for signal in display[0]:
        if sorted(signal) == sorted(a + b + c + e + f + g):
            n[0] = signal
        elif sorted(signal) == sorted(a + c + d + e + g):
            n[2] = signal
        elif sorted(signal) == sorted(a + c + d + f + g):
            n[3] = signal
        elif sorted(signal) == sorted(a + b + d + e + f + g):
            n[6] = signal
        elif sorted(signal) == sorted(a + b + c + d + f + g):
            n[9] = signal

    output_value = ""
    for digit_output in display[1]:
        for i, v in enumerate(n):
            if sorted(v) == sorted(digit_output):
                output_value += str(i)
    print(f"{display[1]}: {int(output_value)}")
    total += int(output_value)

print(f"part 2: {total}")
