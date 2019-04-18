"""
https://www.hackerrank.com/challenges/closest-numbers/problem

Score: 35/35
Submitted: 2017
"""

len_ = int(input())
A = sorted(map(int, input().split()))
sol = [abs(A[0] - A[1]), [(A.pop(0), A[0])]]

for i, n in enumerate(A):
    try:
        nxt = A[i + 1]
    except IndexError:
        break

    diff = abs(n - nxt)
    if diff < sol[0]:
        sol = [diff, [(n, nxt)]]
    elif diff == sol[0]:
        sol[1].append((n, nxt))

print(*[x for y in sol[1] for x in y])
