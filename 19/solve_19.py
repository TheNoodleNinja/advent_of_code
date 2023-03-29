import numpy as np
import re
from tqdm import tqdm

RESOURCES = ["ore", "clay", "obs", "geo"]
def distance(x0,y0,x1,y1):
    return abs(x0-x1), abs(y0-y1)

def read_input(input):
    blueprints = []
    with open(input, "r") as f:
        
        lines = f.readlines()
    for line in lines:
        bp = re.findall("\d+", line)
        blueprints.append(np.array([
            [bp[1], 0, 0, 0],
            [bp[2], 0, 0, 0],
            [bp[3], bp[4], 0, 0],
            [bp[5], 0, bp[6], 0],
        ], dtype=np.int32))
    return blueprints
    

def solve_15_A(input, T, debug=False):
    blueprints = read_input(input)
    #axis 0: possbible build plans, 1: (resources, robots), 2: ore varieties
    nodes = np.array([[[0,0,0,0],[1,0,0,0]]], dtype=np.int32)

    for i, bp in enumerate(blueprints):
        for t in range(T):
            # build_robots
            building=np.zeros([4], dtype=np.int32)
            for j, r_bp in enumerate(bp):
                if (resources-r_bp).min() >= 0:
                    building[j] = 1
                    resources -= r_bp
            # collect_resources
            nodes[:, 0, :] += nodes[:, 1, :] # add robots to resources
            # robots finsih building
            robots += building
            if debug:
                print(f"---[t:{t+1}|bp:{i+1}]---")
                print(f"[res]: {resources}")
                print(f"[rob]: {robots}")
        x=10
            

        



def solve_15_B(input, debug=False):
    blueprints = read_input(input)


if __name__ == "__main__":
    # A
    print(solve_15_A("19/input_test.txt", 24, True))
    # print(solve_15_A("19/input.txt", 2000000))
    # print(solve_15_B("19/input_test.txt", 0, 20, True))
    # print(solve_15_B("19/input.txt", 0, 4000000, True))