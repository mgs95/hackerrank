"""
https://www.hackerrank.com/challenges/countingsort2/problem

Score: 30/30
Submitted: 2017
"""

__, ar = input(), list(map(int, input().split()))

sol = [0] * 100
for i in ar:
    sol[i] += 1

print(*[i for i in range(100) for __ in range(sol[i]) if sol[i]])
