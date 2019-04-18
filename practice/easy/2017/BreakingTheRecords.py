"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

Score: 10/10
Submitted: 2017
"""


def get_record(s):
    lower = higher = s.pop(0)
    top = bot = 0

    for n in s:
        if n > higher:
            higher = n
            top += 1
        if n < lower:
            lower = n
            bot += 1

    return top, bot


__ = input()
s = list(map(int, input().split()))
result = get_record(s)
print(" ".join(map(str, result)))
