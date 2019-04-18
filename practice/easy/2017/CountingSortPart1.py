"""
https://www.hackerrank.com/challenges/countingsort1/problem

Score: 30/30
Submitted: 2017
"""

__ = input()

sol = [0] * 100
for i in map(int, input().split()):
    sol[i] += 1

print(*sol)
