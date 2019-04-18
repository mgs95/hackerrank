"""
https://www.hackerrank.com/contests/world-codesprint-13/challenges/competitive-teams

Score: 21.36/60
Submitted: 2018
Difficulty: Hard
"""

from collections import defaultdict


def solve(n, arr):
    m = {i: [i, 1] for i in range(1, n + 1)}

    G = defaultdict(int)
    G[1] = n
    ni = n + 1

    for o, *ags in arr:
        if o == 1:
            ia, ib = ags
            a, b = 1, 1
            while ia in m and ia != m[ia][0]:
                ia, a = m[ia]
            while ib in m and ib != m[ib][0]:
                ib, b = m[ib]

            if ia == ib:
                continue

            G[a] -= 1
            G[b] -= 1

            if G[a] == 0:
                del G[a]
            if G[b] == 0:
                del G[b]

            nw = a + b
            G[nw] += 1

            ni += 1

            m[ia] = [ni, nw]
            m[ib] = [ni, nw]

        else:
            c = ags[0]

            ks = sorted(G.keys(), reverse=True)

            r = 0
            for i, el in enumerate(ks):
                for el2 in ks[i:]:
                    if el - el2 >= c:
                        if el == el2 and c == 0:
                            temp = G[el] - 1
                            while temp:
                                r += temp
                                temp -= 1
                        else:
                            r += G[el] * G[el2]

            print(r)


if __name__ == '__main__':
    n, q = list(map(int, input().split()))

    arr = [list(map(int, input().split())) for __ in range(q)]

    solve(n, arr)
