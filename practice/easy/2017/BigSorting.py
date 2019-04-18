"""
https://www.hackerrank.com/challenges/big-sorting/problem

Score: 20/20
Submitted: 2017
"""

print(*sorted((input() for _ in range(int(input()))), key=int), sep="\n")