"""
https://www.hackerrank.com/challenges/compare-the-triplets/problem

Score: 10/10
Submitted: 2017
"""


def solve(A, B):
    sol = [1*(a>b) + 2*(b>a) for a, b in zip(A, B)]
    return sol.count(1), sol.count(2)


A = list(map(int, input().split()))
B = list(map(int, input().split()))
result = solve(A, B)

print(" ".join(map(str, result)))
