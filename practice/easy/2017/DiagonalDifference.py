"""
https://www.hackerrank.com/challenges/diagonal-difference/problem

Score: 10/10
Submitted: 2017
"""

n = int(input().strip())
a = [list(map(int, input().split())) for i in range(n)]

print(abs(sum([a[i][i] - a[i][n-i-1] for i in range(n)])))
