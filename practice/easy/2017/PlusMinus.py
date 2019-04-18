"""
https://www.hackerrank.com/challenges/plus-minus/problem

Score: 10/10
Submitted: 2017
"""

n = int(input())
values = {0: 0, 1: 0, 2: 0}

for i in map(int, input().split()):
    values[2*(not i) + 1*(i < 0)] += 1

print('\n'.join(map(lambda x: str(round(x/n, 6)), values.values())))
