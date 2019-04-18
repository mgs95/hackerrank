"""
https://www.hackerrank.com/challenges/birthday-cake-candles/problem

Score: 10/10
Submitted: 2017
"""

n = int(input())
height = list(map(int, input().split()))

print(height.count(max(height)))
