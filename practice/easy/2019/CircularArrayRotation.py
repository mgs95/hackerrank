"""
https://www.hackerrank.com/challenges/circular-array-rotation/problem

Score: 20/20
Submitted: Mar, 2019
"""

n, k, q = map(int, input().split())
arr = list(map(int, input().split()))

k %= n
cut = n - k

arr = arr[cut:] + arr[:cut]

for _ in range(q):
    print(arr[int(input())])
