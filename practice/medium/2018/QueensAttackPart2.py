"""
https://www.hackerrank.com/challenges/queens-attack-2/problem

Score: 30/30
Submitted: 2018
"""


def queens_attack(n, k, r_q, c_q, obstacles):
    get_coord = lambda func, x, val: func(x, key=lambda el: el[val])

    # Get obstacles by directions
    r_obstacles = list(filter(lambda el: el[0] == r_q and el[1] != c_q, obstacles))
    left = list(filter(lambda el: el[1] < c_q, r_obstacles))
    right = list(filter(lambda el: el[1] > c_q, r_obstacles))
    c_obstacles = list(filter(lambda el: el[0] != r_q and el[1] == c_q, obstacles))
    up = list(filter(lambda el: el[0] < r_q, c_obstacles))
    down = list(filter(lambda el: el[0] > r_q, c_obstacles))
    x_obstacles = list(
        filter(lambda el: el[0] != r_q and el[1] != c_q and (abs(r_q - el[0]) == abs(c_q - el[1])),
               obstacles))
    up_right = list(filter(lambda el: el[0] < r_q and el[1] > c_q, x_obstacles))
    down_right = list(filter(lambda el: el[0] > r_q and el[1] > c_q, x_obstacles))
    up_left = list(filter(lambda el: el[0] < r_q and el[1] < c_q, x_obstacles))
    down_left = list(filter(lambda el: el[0] > r_q and el[1] < c_q, x_obstacles))

    # Get closest to queen obstacle (or last cell if no obstacles) for every direction
    up_right = [0, n + 1] if not up_right else get_coord(min, up_right, 1)
    right = [r_q, n + 1] if not right else get_coord(min, right, 1)
    down_right = [n + 1, n + 1] if not down_right else get_coord(min, down_right, 1)
    left = [r_q, 0] if not left else get_coord(max, left, 1)
    down_left = [n + 1, 0] if not down_left else get_coord(max, down_left, 1)
    down = [n + 1, c_q] if not down else get_coord(min, down, 0)
    up_left = [0, 0] if not up_left else get_coord(max, up_left, 1)
    up = [0, c_q] if not up else get_coord(max, up, 0)

    # Calculate distance between each obstacle and the queen
    result = sum([
        min(up_right[1] - c_q, r_q - up_right[0]),
        right[1] - c_q,
        min(down_right[1] - c_q, down_right[0] - r_q),
        down[0] - r_q,
        min(c_q - down_left[1], down_left[0] - r_q),
        c_q - left[1],
        min(c_q - up_left[1], r_q - up_left[0]),
        r_q - up[0]
    ])

    return result - 8


if __name__ == "__main__":
    # Board is n x n
    n, k = list(map(int, input().split()))
    # Queen located ar [r, c]
    r_q, c_q = list(map(int, input().split()))
    obstacles = []
    for __ in range(k):
        obstacles_t = list(map(int, input().split()))
        obstacles.append(obstacles_t)
    result = queens_attack(n, k, r_q, c_q, obstacles)
    print(result)
