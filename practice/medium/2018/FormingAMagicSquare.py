"""
https://www.hackerrank.com/challenges/magic-square-forming/problem

Score: 20/20
Submitted: 2018
"""


def forming_magic_square(s):
    solved_magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    ]
    size = 3
    counters = []

    for magic_square in solved_magic_squares:
        counter = 0
        for i in range(size):
            for j in range(size):
                if s[i][j] != magic_square[i][j]:
                    counter += abs(s[i][j] - magic_square[i][j])
        counters.append(counter)

    return min(counters)


if __name__ == "__main__":
    s = []
    for s_i in range(3):
        s_t = [int(s_temp) for s_temp in input().split()]
        s.append(s_t)
    result = forming_magic_square(s)
    print(result)
