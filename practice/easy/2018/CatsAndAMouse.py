"""
https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

Score: 15/15
Submitted: 2018
"""

import os


def cat_and_mouse(a, b, c):
    ca = abs(c - a)
    cb = abs(c - b)

    if ca == cb:
        return 'Mouse C'
    elif ca < cb:
        return 'Cat A'
    else:
        return 'Cat B'


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        inp = list(map(int, input().split()))

        result = cat_and_mouse(*inp)

        f.write(result + '\n')

    f.close()
