"""
https://www.hackerrank.com/challenges/drawing-book/problem

Score: 10/10
Submitted: 2018
"""

n = int(input())
p = int(input())

start = p // 2
end = ((n-p) // 2) + 1 * (n%2 == 0 and p%2 != 0)

print(min([start, end]))
