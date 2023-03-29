def solve_02(input):
    conv = {"X":0, "Y":1, "Z":2, "A":0, "B":1, "C":2}
    result=[
        #A  B  C
        [3, 0, 6],  # X
        [6, 3, 0],  # Y
        [0, 6, 3]   # Z

    ]
    with open(input, "r") as f:
        rounds = f.readlines()
    
    score = 0
    for round in rounds:
        score += 3*("Z" in round) + 2*("Y" in round) + ('X' in round) # scores for choices
        opponent, player = round.strip().split(" ")
        score += result[conv[player]][conv[opponent]]
    return score


if __name__ == "__main__":
    print(solve_02("02/input.txt"))
    #print(solve_02("02/input.txt", 3))