"""
https://www.hackerrank.com/challenges/sherlock-and-array/problem

Score: 40/40
Submitted: 2018
"""


def solve(test):
    if len(test) == 1:
        return 'YES'
    left_sum = 0
    right_sum = sum(test[1:])
    last = test[0]

    for n in test[1:]:
        if left_sum == right_sum:
            return 'YES'

        left_sum += last
        right_sum -= n

        last = n

    return 'NO'


T = int(input())
for __ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    result = solve(a)
    print(result)
