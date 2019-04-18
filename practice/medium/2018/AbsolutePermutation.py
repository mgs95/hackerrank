"""
https://www.hackerrank.com/challenges/absolute-permutation/problem

Score: 40/40
Submitted: 2018
"""


for _ in range(int(input())):
    n, k = map(int, input().split())

    numbers = set(range(1, n+1))
    r = []
    end = False

    for i in range(n, 0, -1):
        a, b = i + k, i - k

        if a in numbers:
            r.append(a)
            numbers.remove(a)
        elif b in numbers:
            r.append(b)
            numbers.remove(b)
        else:
            print(-1)
            break
    else:
        print(' '.join(list(map(str, r[::-1]))))
