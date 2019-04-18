"""
https://www.hackerrank.com/challenges/grid-challenge/problem

Score: 20/20
Submitted: 2018
"""


def grid_challenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    sorted_reversed_grid = [''.join(row) for row in zip(*sorted_grid)]
    sorted_reversed_grid_sorted = [''.join(sorted(row)) for row in sorted_reversed_grid]
    return 'YES' if sorted_reversed_grid == sorted_reversed_grid_sorted else 'NO'


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        n = int(input())
        grid = []
        for __ in range(n):
           grid_t = str(input())
           grid.append(grid_t)
        result = grid_challenge(grid)
        print(result)
