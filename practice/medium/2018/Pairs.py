"""
https://www.hackerrank.com/challenges/pairs/problem

Score: 50/50
Submitted: 2018
"""


def pairs(k, arr):
    solution = 0
    arr_2 = set([el + k for el in arr])

    for el in arr:
        if el in arr_2:
            solution += 1

    return solution


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = pairs(k, arr)
    print(result)
