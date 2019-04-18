"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited/problem

Score: 15/15
Submitted: Mar, 2019
"""

n, k = map(int, input().split())
arr = list(map(int, input().split()))

r = 100

for idx in range(0, n, k):
    idx = idx + k
    if idx >= n:
        idx = idx % n

    r -= 1 + 2 * arr[idx]

print(r)
