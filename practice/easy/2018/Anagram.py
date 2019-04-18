"""
https://www.hackerrank.com/challenges/anagram/problem

Score: 25/25
Submitted: 2018
"""

from collections import Counter


def anagram(s):
    mid, mod = divmod(len(s), 2)
    if mod:
        return -1

    a, b = s[:mid], s[mid:]
    a, b = Counter(a), Counter(b)

    return sum((a - b).values())


q = int(input())
for __ in range(q):
    s = input()
    result = anagram(s)
    print(result)
