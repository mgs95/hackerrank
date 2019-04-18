"""
https://www.hackerrank.com/challenges/3d-surface-area/problem

Score: 30/30
Submitted: 2018
"""


def surface_area(A):
    area = 0
    neighs = [[-1, 0], [0, 1], [1, 0], [0, -1]]

    for x in range(H):
        for y in range(W):
            el = A[x][y]
            # add base and top area
            area += 2
            for dx, dy in neighs:
                try:
                    # Raise index exception if trying to access index -1
                    if -1 in [x + dx, y + dy]:
                        raise IndexError

                    # Add area of actual element from neighbours as base
                    new = el - A[x + dx][y + dy]
                    if new > 0:
                        area += new
                # Add area corresponding to the sides of the figure
                except IndexError:
                    area += el

    return area


if __name__ == "__main__":
    H, W = list(map(int, input().split()))
    A = []
    for __ in range(H):
        A_t = list(map(int, input().split()))
        A.append(A_t)
    result = surface_area(A)
    print(result)
