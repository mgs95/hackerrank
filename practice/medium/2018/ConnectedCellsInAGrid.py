"""
https://www.hackerrank.com/challenges/connected-cell-in-a-grid/problem

Score: 50/50
Submitted: 2018
"""


from itertools import product


def connected_cell(test):
    NEIGHBOURS = list(product([-1, 0, 1], repeat=2))
    NEIGHBOURS.pop(NEIGHBOURS.index((0, 0)))
    result = 0
    seen = []
    to_study = []

    for x in range(1, len(test) - 1):
        for y in range(1, len(test[0]) - 1):
            if test[x][y] == 1 and (x, y) not in seen:
                seen.append((x, y))
                to_study.append((x, y))
                count = 1

                while to_study:
                    x, y = to_study.pop(0)
                    for dx, dy in NEIGHBOURS:
                        nx, ny = x + dx, y + dy
                        if nx < 0 or ny < 0:
                            continue
                        try:
                            if test[nx][ny] == 1 and (nx, ny) not in seen:
                                count += 1
                                seen.append((nx, ny))
                                to_study.append((nx, ny))
                        except IndexError:
                            continue

                result = max(result, count)
            else:
                seen.append((x, y))

    return result


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    matrix = []
    for __ in range(n):
       matrix_t = [int(matrix_temp) for matrix_temp in input().split()]
       matrix.append(matrix_t)
    result = connected_cell(matrix)
    print(result)
