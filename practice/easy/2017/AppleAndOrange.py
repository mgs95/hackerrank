"""
https://www.hackerrank.com/challenges/apple-and-orange/problem

Score: 10/10
Submitted: 2017
"""

(s, t), (a, b), (m, n) = [list(map(int, input().split())) for __ in range(3)]
apple = list(filter(lambda x: s-a <= x <= t-a, map(int, input().split())))
orange = list(filter(lambda x: s-b <= x <= t-b, map(int, input().split())))

[print(x) for x in map(len, [apple, orange])]
