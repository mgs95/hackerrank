"""
https://www.hackerrank.com/challenges/missing-numbers/problem

Score: 45/45
Submitted: 2018
"""

# !/bin/python3

from collections import Counter


def missing_numbers(arr, brr):
    arr = Counter(arr)
    brr = Counter(brr)
    solution = []

    for key in brr:
        if key not in arr:
            solution.append(key)
        else:
            difference = brr[key] - arr[key]
            if difference:
                solution.append(key)

    return solution


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    m = int(input())
    brr = list(map(int, input().split()))
    result = missing_numbers(arr, brr)
    print(" ".join(map(str, result)))
