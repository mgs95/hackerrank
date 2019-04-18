"""
https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem

Score: 15/15
Submitted: 2018
"""


def minimum_absolute_difference(arr):
    arr = sorted(arr)

    min_diff = max(arr)

    for idx in range(1, len(arr)):
        act_diff = abs(arr[idx - 1] - arr[idx])
        if act_diff < min_diff:
            min_diff = act_diff

    return min_diff


if __name__ == "__main__":
    __ = int(input())
    arr = list(map(int, input().split()))
    result = minimum_absolute_difference(arr)
    print(result)
