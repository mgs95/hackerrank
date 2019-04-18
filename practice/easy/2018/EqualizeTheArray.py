"""
https://www.hackerrank.com/challenges/equality-in-a-array/problem

Score: 20/20
Submitted: 2018
"""

from collections import Counter


def equalize_array(arr):
    return len(arr) - Counter(arr).most_common(1)[0][1]


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = equalize_array(arr)
    print(result)
