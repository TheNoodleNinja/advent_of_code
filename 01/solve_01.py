def solve_01(input, n=1):
    with open(input, "r") as f:
        data = f.read()

    elves = data.split("\n\n")
    totals = []
    for elf in elves:
        calories = elf.split("\n")
        totals.append(sum([int(x) for x in calories if x]))
    totals.sort()

    return sum(totals[-n:])

if __name__ == "__main__":
    print(solve_01("01/input.txt"))
    print(solve_01("01/input.txt", 3))