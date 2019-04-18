"""
https://www.hackerrank.com/challenges/gem-stones/problem

Score: 20/20
Submitted: 2018
"""

from functools import reduce


def gemstones(arr):
    arr = map(set, arr)
    gemstones = reduce(lambda a, b: b & a, arr)

    return len(gemstones)


n = int(input())
arr = []
for __ in range(n):
    arr_t = str(input())
    arr.append(arr_t)
result = gemstones(arr)
print(result)
