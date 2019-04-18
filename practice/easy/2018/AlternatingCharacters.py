"""
https://www.hackerrank.com/challenges/alternating-characters/problem

Score: 20/20
Submitted: 2018
"""


def alternating_characters(s):
    last = s[0]
    count = 0
    for c in s[1:]:
        if c == last:
            count += 1
        last = c

    return count


q = int(input())
for __ in range(q):
    s = input()
    result = alternating_characters(s)
    print(result)
