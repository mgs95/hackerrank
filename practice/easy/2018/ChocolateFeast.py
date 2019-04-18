"""
https://www.hackerrank.com/challenges/chocolate-feast/problem

Score: 25/25
Submitted: 2018
"""


def chocolate_feast(n, c, m):
    chocolate = n // c
    wrappers = chocolate

    while wrappers >= m:
        promo = wrappers // m
        chocolate += promo
        wrappers = wrappers - m * promo + promo

    return chocolate


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n, c, m = list(map(int, input().split()))
        result = chocolate_feast(n, c, m)
        print(result)
