"""
https://www.hackerrank.com/challenges/camelcase/problem

Score: 15/15
Submitted: 2018
"""

from string import ascii_uppercase


def camelcase(s):
    count = 0
    for c in s:
        if c in ascii_uppercase:
            count += 1

    return count + 1


if __name__ == "__main__":
    s = input().strip()
    result = camelcase(s)
    print(result)
