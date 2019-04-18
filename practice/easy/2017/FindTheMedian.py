"""
https://www.hackerrank.com/challenges/find-the-median/problem

Score: 35/35
Submitted: 2017
"""

n = int(input())
ar = sorted(map(int, input().split()))

print(ar[n//2])
