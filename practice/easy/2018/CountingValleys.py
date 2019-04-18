"""
https://www.hackerrank.com/challenges/counting-valleys/problem

Score: 10/10
Submitted: 2018
"""

__ = input()
s = input()

n_valleys = 0
level = 0

for p in s:
    if p == 'U':
        level +=1
        if level == 0:
            n_valleys += 1
    else:
        level -= 1

print(n_valleys)
