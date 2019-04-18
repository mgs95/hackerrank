"""
https://www.hackerrank.com/challenges/countingsort4/problem

Score: 40/40
Submitted: 2017
"""

n = int(input())
tx_pairs = lambda x, s: [int(x[0]), x[1] if s else '-']
ar = [tx_pairs(input().split(), i >= n / 2) for i in range(n)]

counts = [[0, []] for __ in range(100)]
for j, (i, __) in enumerate(ar):
    counts[i][0] += 1
    counts[i][1].append(j)

sol = []
for i in range(100):
    if counts[i][0]:
        for j in counts[i][1]:
            sol.append(ar[j][1])

print(' '.join(sol))
