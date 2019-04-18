"""
https://www.hackerrank.com/challenges/cavity-map/problem

Score: 30/30
Submitted: 2018
"""


def cavity_map(grid):
    SIDES = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    for x in range(1, n - 1):
        for y in range(1, n - 1):
            if all([grid[x][y] > grid[x + dx][y + dy] for dx, dy in SIDES]):
                grid[x] = grid[x][:y] + 'X' + grid[x][y + 1:]

    return grid


if __name__ == "__main__":
    n = int(input())
    grid = []
    for __ in range(n):
        grid_t = str(input())
        grid.append(grid_t)
    result = cavity_map(grid)
    print("\n".join(map(str, result)))
