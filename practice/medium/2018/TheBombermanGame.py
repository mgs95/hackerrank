"""
https://www.hackerrank.com/challenges/bomber-man/problem

Score: 40/40
Submitted: 2018
"""


def bomber_man(n, grid):
    if n == 1:
        return grid

    if not n % 2:
        return [['O'] * len(grid[0]) for __ in range(len(grid))]

    n = int(n - 4 * (n // 4))

    DIRS = [(0, 0), (-1, 0), (0, -1), (0, 1), (1, 0)]
    grid_2 = [['O'] * len(grid[0]) for __ in range(len(grid))]
    indexes = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] == 'O':
                indexes.append((x, y))

    for x, y in indexes:
        for dx, dy in DIRS:
            new_x, new_y = x + dx, y + dy
            new_x, new_y = max(0, new_x), max(0, new_y)

            try:
                grid_2[new_x][new_y] = '.'
            except IndexError:
                pass

    grid_3 = [['O'] * len(grid[0]) for __ in range(len(grid))]
    indexes = []
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid_2[x][y] == 'O':
                indexes.append((x, y))

    for x, y in indexes:
        for dx, dy in DIRS:
            new_x, new_y = x + dx, y + dy
            new_x, new_y = max(0, new_x), max(0, new_y)

            try:
                grid_3[new_x][new_y] = '.'
            except IndexError:
                pass

    return grid_2 if n == 3 else grid_3


if __name__ == "__main__":
    r, c, n = list(map(int, input().split()))
    grid = []
    for __ in range(r):
        grid_t = str(input())
        grid.append(grid_t)
    result = bomber_man(n, grid)
    print("\n".join(map(lambda x: ''.join(x), result)))
