"""
https://www.hackerrank.com/contests/world-codesprint-11/challenges/simple-file-commands

Score: 20/40
Submitted: 2017
Difficulty: Medium
"""

from collections import defaultdict


def find_next_aval(l):
    for n in range(len(l) + 1):
        if n not in l:
            return n


def create(filenames, fn, rn=False):
    filenames.setdefault(fn, [])
    n = find_next_aval(filenames[fn])
    filenames[fn].append(n)

    if rn:
        return n

    print('+', fn + (n > 0) * ('(' + str(n) + ')'))


def remove(filenames, fn, rn=False):
    if not rn:
        print('-', fn)

    if fn[-1] == ')':
        fn, n = fn.split('(')
        n = int(n.split(')')[0])
    else:
        n = 0

    filenames[fn].pop(filenames[fn].index(n))


q = int(input())
filenames = defaultdict(list)
for c in range(q):
    command, *arg = input().split()

    if command == 'crt':
        fn = arg[0]
        create(filenames, fn)

    elif command == 'del':
        fn = arg[0]
        remove(filenames, fn)

    else:
        fn1, fn2 = arg
        remove(filenames, fn1, True)
        n = create(filenames, fn2, True)
        number = '(' + str(n) + ')' if n else ''

        print('r', fn1, '->', fn2 + number)
