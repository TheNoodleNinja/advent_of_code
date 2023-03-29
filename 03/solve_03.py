from functools import lru_cache

@lru_cache
def priority(char):
    char = ord(char)
    # upper case
    if char < 96:
        return char - 38
    # lower case
    else:
        return char - 96

def find_common(*args):
    set0 = set([char for char in args[0]])
    for str in args[1:]:
        set1 = set([char for char in str])
        set0 = set0.intersection(set1)
    return set0.pop()

def solve_03A(input):
    with open(input, "r") as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        line = line.strip()
        N = len(line)
        comp0, comp1 = line[:int(N/2)], line[int(N/2):]
        total += priority(find_common(comp0, comp1))

    return total

def solve_03B(input):
    with open(input, "r") as f:
        lines = f.readlines()

    total = 0
    for i in range(0, len(lines), 3):
        group = [line.strip() for line in lines[i:i+3]]
        total += priority(find_common(*group))

    return total

if __name__ == "__main__":
    print(priority("a"))
    print(priority("A"))
    print(find_common("vJrwpWtwJgWr", "hcsFMMfFFhFp"))
    print(solve_03A("03/input.txt"))
    print(solve_03B("03/input.txt"))