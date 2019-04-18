"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

Score: 15/15
Submitted: Feb, 2019
"""

a, b, k = map(int, input().split())
print(sum(not (n - int(str(n)[::-1])) % k for n in range(a, b+1)))
