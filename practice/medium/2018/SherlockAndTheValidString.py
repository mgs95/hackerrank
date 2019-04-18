"""
https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem

Score: 35/35
Submitted: 2018
"""

from collections import defaultdict


def is_valid(s):
    if len(s) <= 1:
        return 'YES'

    d = defaultdict(int)

    for l in s:
        d[l] += 1

    v = sorted(d.values(), reverse=True)
    if v[0] > v[1]:
        v[0] -= 1
    if v[-1] < v[0] and v[-1] == 1:
        v.pop()

    if not ''.join([str(l) for l in v]).replace(str(v[0]), ''):
        return 'YES'
    return 'NO'


s = input().strip()
result = is_valid(s)
print(result)
