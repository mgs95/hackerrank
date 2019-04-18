"""
https://www.hackerrank.com/challenges/tower-breakers-1/problem

Score: 15/15
Submitted: 2018
"""


def tower_breakers(n, m):
    if m == 1:
        return 2
    return 1 if n % 2 else 2


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        n, m = list(map(int, input().split()))
        result = tower_breakers(n, m)
        print(result)
