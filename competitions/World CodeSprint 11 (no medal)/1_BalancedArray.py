"""
https://www.hackerrank.com/contests/world-codesprint-11/challenges/balanced-array

Score: 10/10
Submitted: 2017
Difficulty: Easy
"""


def solve(n, a):
    return abs(sum(a[:n//2])-sum(a[n//2:]))


n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = solve(n, a)
print(result)
