"""
https://www.hackerrank.com/challenges/quicksort1/problem

Score: 20/20
Submitted: 2017
"""

__ = input()
pivot, *arr = [int(n) for n in input().split()]
left, equals, right = [], [pivot], []

for n in arr:
    l = left if n < pivot else right if n > pivot else equals
    l.append(n)

print(' '.join(map(str, left + equals + right)))
