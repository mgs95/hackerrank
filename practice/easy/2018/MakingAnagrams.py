"""
https://www.hackerrank.com/challenges/making-anagrams/problem

Score: 30/30
Submitted: 2018
"""

from collections import Counter


def making_anagrams(s1, s2):
    s1 = Counter(list(s1))
    s2 = Counter(list(s2))

    counter = 0
    for c in set(list(s1.keys()) + list(s2.keys())):
        if c not in s1:
            counter += s2[c]
        elif c not in s2:
            counter += s1[c]
        else:
            counter += abs(s1[c] - s2[c])

    return counter


s1 = input()
s2 = input()
result = making_anagrams(s1, s2)
print(result)
