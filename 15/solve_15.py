import numpy as np
import cv2
import re
from tqdm import tqdm

def distance(x0,y0,x1,y1):
    return abs(x0-x1), abs(y0-y1)

def read_input(input):
    sensors, beacons = [], []
    with open(input, "r") as f:
        lines = f.readlines()
        for line in lines:
            sx, bx = [int(i) for i in re.findall("x=(-?\d+)", line)]
            sy, by = [int(i) for i in re.findall("y=(-?\d+)", line)]

            sensors.append([sx,sy, *distance(sx, sy, bx, by)])
            beacons.append((bx, by))
    return sensors, beacons
    
def get_ranges(sensors, beacons, y, min_x=-float("inf"), max_x=float("inf"), debug=False):
    ranges = []
    for i, (sx, sy, dx, dy) in enumerate(sensors):
        bx, by = beacons[i]
        dx, dy = distance(sx, sy, bx, by)
        if abs(sy-y) <= dx+dy:
            dx_ = dx+dy-abs(sy-y)
            if sx+dx_ >= min_x and sx-dx_ <= max_x:
                ranges.append([max(sx-dx_, min_x), min(sx+dx_, max_x)])
    # merge ranges
    ranges.sort(key=lambda x:x[0])

    i = 0
    while i < len(ranges)-1:
        if ranges[i][1]+1 >= ranges[i+1][0]:
            if ranges[i][1] <= ranges[i+1][1]:
                ranges[i][1] = ranges[i+1][1]
            ranges.pop(i+1)
        else:
            i+=1

    return ranges


def solve_15_A(input, y, debug=False):
    sensors, beacons = read_input(input)
    ranges = get_ranges(sensors, beacons, y)
    beacons = set(beacons)
    total = 0
    for r in ranges:
        total += r[1]-r[0]+1
        for beacon in beacons:
            if beacon[1] == y and beacon[0] >= r[0] and beacon[0] <= r[1]:
                total -= 1
    
    return total

def solve_15_B(input, min_, max_, debug=False):
    sensors, beacons = read_input(input)
    for y in tqdm(range(min_, max_)):
        ranges = get_ranges(sensors, beacons, y, min_, max_)
        if len(ranges) > 1:
            x = ranges[0][1]+1
            return x*4000000+y

if __name__ == "__main__":
    # A
    sensors, bacons = read_input("15/input_test.txt")
    print(solve_15_A("15/input_test.txt", 10, True))
    print(solve_15_A("15/input.txt", 2000000))
    print(solve_15_B("15/input_test.txt", 0, 20, True))
    print(solve_15_B("15/input.txt", 0, 4000000, True))