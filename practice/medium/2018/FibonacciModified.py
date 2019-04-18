"""
https://www.hackerrank.com/challenges/fibonacci-modified/problem

Score: 45/45
Submitted: 2018
"""


def fibonacci_modified(t1, t2, n):
    while n:
        t1, t2 = t2, t1 + t2 ** 2
        n -= 1

    return t2


if __name__ == "__main__":
    t1, t2, n = list(map(int, input().split()))
    result = fibonacci_modified(t1, t2, n - 2)
    print(result)
