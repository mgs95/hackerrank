"""
https://www.hackerrank.com/challenges/reduced-string/problem

Score: 10/10
Submitted: 2018
"""


def super_reduced_string(s):
    sol = []

    for l in s:
        if sol:
            if l == sol[-1]:
                sol.pop()
                continue
        sol.append(l)

    return ''.join(sol) if sol else 'Empty String'


s = input().strip()
result = super_reduced_string(s)
print(result)
