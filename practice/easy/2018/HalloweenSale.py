"""
https://www.hackerrank.com/challenges/halloween-sale/problem

Score: 20/20
Submitted: 2018
"""


def how_many_games(p, d, m, s):
    counter = 0
    prev = p
    while s >= prev:
        s -= prev
        prev = max(prev - d, m)
        counter += 1

    return counter


if __name__ == "__main__":
    p, d, m, s = list(map(int, input().split()))
    answer = how_many_games(p, d, m, s)
    print(answer)
