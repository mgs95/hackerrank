"""
https://www.hackerrank.com/challenges/grading/problem

Score: 10/10
Submitted: 2017
"""

solve = lambda grades: [g+5 - g%5 if g%5 > 2 and g>37 else g for g in grades]

n = int(input())
grades = [int(input()) for __ in range(n)]
result = solve(grades)

print("\n".join(map(str, result)))
