"""
https://www.hackerrank.com/challenges/sock-merchant/problem

Score: 10/10
Submitted: 2018
"""

from collections import Counter

__ = input()
ar = Counter(list(map(int, input().strip().split(' '))))

count = 0

for el in ar:
    count += ar[el] // 2

print(count)
