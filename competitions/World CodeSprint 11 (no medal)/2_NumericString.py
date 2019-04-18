"""
https://www.hackerrank.com/contests/world-codesprint-11/challenges/numeric-string/problem

Score: 18/30
Submitted: 2017
Difficulty: Medium
"""

s = input()
k, b, m = list(map(int, input().split()))

if len(s) <= k:
    print(int(s, base=b) % m)
else:
    ss = s[:k]
    sol = int(ss, base=b) % m
    for n in s[k:]:
        ss = ss[1:]+n
        sol += int(ss, base=b) % m

    print(sol)
