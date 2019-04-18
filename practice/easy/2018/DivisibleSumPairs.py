"""
https://www.hackerrank.com/challenges/divisible-sum-pairs/problem

Score: 10/10
Submitted: 2018
"""

__, k = list(map(int, input().split(' ')))
ar = list(map(int, input().split(' ')))

counter = 0

for i, x in enumerate(ar[:-1]):
    for y in ar[i + 1:]:
        if not (x + y) % k:
            counter += 1

print(counter)
