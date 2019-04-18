"""
https://www.hackerrank.com/challenges/staircase/problem

Score: 10/10
Submitted: 2017
"""

n = int(input())

for i in range(n):
    print(' ' * (n-i-1) + '#' * (i+1))
