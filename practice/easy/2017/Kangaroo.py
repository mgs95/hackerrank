"""
https://www.hackerrank.com/challenges/kangaroo/problem

Score: 10/10
Submitted: 2017
"""

x1, v1, x2, v2 = list(map(int, input().split()))
x, y = sorted([[x1, v1], [x2, v2]], key=lambda el: el[0])

if not x[1] > y[1] or (x[0]-y[0]) % (x[1]-y[1]):
    print('NO')
else:
    print('YES')
