import numpy as np

def is_visible(m: np.array, i: int, j: int) -> bool:
    x = m[i,j]
    left = m[i,:j]
    right = m[i,j+1:]
    top = m[:i,j]
    bottom = m[i+1:,j]
    visible_left = np.where(left>=x, 0, 1).all()
    visible_right = np.where(right>=x, 0, 1).all()
    visible_top = np.where(top>=x, 0, 1).all()
    visible_bottom = np.where(bottom>=x, 0, 1).all()
    return visible_left or visible_right or visible_top or visible_bottom

def get_visibility(m: np.array, i: int, j: int) -> int:
    x = m[i,j]
    left = m[i,:j]
    right = m[i,j+1:]
    top = m[:i,j]
    bottom = m[i+1:,j]

    blocked_left = np.where(left>=x)[0]
    visible_left = len(left) - blocked_left.max() if blocked_left.size else len(left)

    blocked_right = np.where(right>=x)[0]
    visible_right = blocked_right.min() +1 if blocked_right.size else len(right)

    blocked_top = np.where(top>=x)[0]
    visible_top = len(top) - blocked_top.max() if blocked_top.size else len(top)

    blocked_bottom = np.where(bottom>=x)[0]
    visible_bottom = blocked_bottom.min()+1 if blocked_bottom.size else len(bottom)

    return visible_left * visible_right * visible_top * visible_bottom

def solve_08(input, part='A', debug=False):
    with open(input, "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        lines[i] = [j for j in lines[i].strip()]
    
    tree_grid = np.array(lines, dtype=int)
    debug_grid = np.zeros_like(tree_grid)

    total = 0

    M, N = tree_grid.shape

    for i in range(1, M-1):
        for j in range(1, N-1):
            if part == 'A':
                score = is_visible(tree_grid, i, j)
                total += score
            if part == 'B':
                score = get_visibility(tree_grid, i, j)
                total = max(total, score)
            if debug:
                debug_grid[i,j] = score

    if debug:
        print(debug_grid)
    return total + (part == 'A')*(2*(M-1) + 2*(N-1)) # interior + border

if __name__ == "__main__":
    print(solve_08("08/input_test.txt", 'A', True))
    print(solve_08("08/input.txt"))
    print(solve_08("08/input_test.txt", 'B', True))
    print(solve_08("08/input.txt", 'B'))