"""
https://www.hackerrank.com/challenges/strange-code/problem

Score: 30/30
Submitted: 2018
"""


def strange_code(t):
    next_boundary = 3
    while t > next_boundary:
        t -= next_boundary
        next_boundary *= 2

    return next_boundary + 1 - t


if __name__ == "__main__":
    t = int(input())
    result = strange_code(t)
    print(result)
