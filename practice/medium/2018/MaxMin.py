"""
https://www.hackerrank.com/challenges/angry-children/problem

Score: 35/35
Submitted: 2018
"""


def angry_children(k, arr):
    arr = sorted(arr)
    solutions = []

    for idx in range(0, len(arr) - k + 1):
        solutions.append(arr[idx + k - 1] - arr[idx])

    return min(solutions)


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    arr = []
    for __ in range(n):
        arr_t = int(input())
        arr.append(arr_t)
    result = angry_children(k, arr)
    print(result)
