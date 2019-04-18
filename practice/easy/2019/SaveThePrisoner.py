"""
https://www.hackerrank.com/challenges/save-the-prisoner/problem

Score: 15/15
Submitted: Mar, 2019
"""

for _ in range(int(input())):
    n, m, s = map(int, input().split())
    pos = m + s - 1

    if pos > n:
        r = pos % n
        print(n if r == 0 else r)
    else:
        print(pos)
