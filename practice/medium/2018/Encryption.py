"""
https://www.hackerrank.com/challenges/encryption/problem

Score: 30/30
Submitted: 2018
"""

from math import sqrt, floor, ceil


def encryption(s):
    s_short = s.replace(' ', '')
    s_root = sqrt(len(s_short))
    a, b = floor(s_root), ceil(s_root)
    if a * b < len(s_short):
        a += 1

    result = []
    for start in range(b):
        word = ''
        for i in range(a):
            try:
                word += s_short[start + i * b]
            except IndexError:
                break
        result.append(word)

    return result


if __name__ == "__main__":
    s = input()
    result = encryption(s)
    print(' '.join(result))
