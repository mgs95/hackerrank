"""
https://www.hackerrank.com/challenges/permutation-equation/problem

Score: 20/20
Submitted: Mar, 2019
"""

n = int(input())
arr = list(map(int, input().split()))

for x in range(1, n+1):
    i = arr.index(x) + 1
    j = arr.index(i) + 1
    print(j)
