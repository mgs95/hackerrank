"""
https://www.hackerrank.com/challenges/happy-ladybugs/problem

Score: 30/30
Submitted: 2018
"""

from collections import Counter


def solve(b):
    counter = Counter(b.replace('_', ''))

    # Any lonely ladybug? :(
    if 1 in counter.values():
        return 'NO'

    if '_' not in b:
        # Check if b is composed by already happy ladybugs
        count = 1
        last = b[0]
        for act in b[1:]:
            if act == last:
                count += 1
            else:
                if count != counter[last]:
                    return 'NO'
                count = 1
            last = act

    # If there is no lonely ladybug and at least one '_' to swap
    # positions
    return 'YES'


Q = int(input())
for __ in range(Q):
    __ = int(input())
    b = input()

    print(solve(b))
