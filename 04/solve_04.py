def solve_04(input):
    with open(input, "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        ranges = line.strip().split(",")
        for i, r in enumerate(ranges):
            ranges[i] = [int(n) for n in r.split("-")]

        envelop = [min(ranges[0][0], ranges[1][0]), max(ranges[0][1], ranges[1][1])]
        print(line, envelop)
        for r in ranges:
            if (envelop == r):
                total += 1

    return total

if __name__ == "__main__":
    print(solve_04("04/input.txt"))