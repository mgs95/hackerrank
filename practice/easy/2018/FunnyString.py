"""
https://www.hackerrank.com/challenges/funny-string/problem

Score: 25/25
Submitted: 2018
"""

from string import ascii_lowercase

mapper = {z[0]: z[1] for z in zip(ascii_lowercase, range(1, len(ascii_lowercase) + 1))}
get_diff = lambda x, i: abs(mapper[x[i + 1]] - mapper[x[i]])


def funny_string(s):
    a, b = s[:], s[::-1]

    for idx in range(len(s) - 1):
        if get_diff(a, idx) != get_diff(b, idx):
            return 'Not Funny'
    return 'Funny'


q = int(input())
for __ in range(q):
    s = input()
    result = funny_string(s)
    print(result)
