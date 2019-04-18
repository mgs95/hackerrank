"""
https://www.hackerrank.com/challenges/migratory-birds/problem

Score: 10/10
Submitted: 2018
"""

from collections import Counter

_ = input()
ar = Counter(list(map(int, input().split())))

print(ar.most_common()[0][0])
