import numpy as np


def read_grid():
    grid = []
    with open('./input', 'r') as f:
        lines = f.readlines()
        for line in lines:
            c_line = [int(i) for i in list(line.rstrip('\n'))]
            grid.append(c_line)
    return np.array(grid)


if __name__ == "__main__":
    grid = read_grid()

    # Part 1
    M = len(grid)
    N = len(grid[0])
    visible = 2*M + 2*(N - 2)
    for row in range(1, M - 1):
        for col in range(1, N - 1):
            if grid[row, col] > max(grid[row, col + 1:]) or \
                    grid[row, col] > max(grid[row, :col]) or \
                    grid[row, col] > max(grid[row + 1:, col]) or \
                    grid[row, col] > max(grid[:row, col]):
                visible += 1
    print(f"Part 1: {visible}")

    # Part 2
    scenic_score = 0
    for row in range(1, M - 1):
        for col in range(1, N - 1):
            l_height = grid[row, col]
            l_score = 0
            r_score = 0
            u_score = 0
            d_score = 0
            for i in range(row - 1, -1, -1):  # Look Up
                u_score += 1
                if l_height <= grid[i, col]:
                    break
            for i in range(row + 1, M):  # Look Down
                d_score += 1
                if l_height <= grid[i, col]:
                    break
            for i in range(col - 1, -1, -1):  # Look Left
                l_score += 1
                if l_height <= grid[row, i]:
                    break
            for i in range(col + 1, N):  # Look Right
                r_score += 1
                if l_height <= grid[row, i]:
                    break
            l_total_score = l_score * r_score * u_score * d_score
            if l_total_score > scenic_score:
                scenic_score = l_total_score
    print(f"Part 2: {scenic_score}")
