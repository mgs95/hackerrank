"""
https://www.hackerrank.com/contests/w38/challenges/a-time-saving-affair

Score: 40/40
Submitted: Jun, 2018
Difficulty: Medium
"""

from collections import defaultdict
from heapq import heappop, heappush


def least_time_to_interview(n, k, m):
    T = 2 * k
    G = defaultdict(list)

    for a, b, w in [list(map(int, input().split())) for _ in range(m)]:
        if a != b:
            G[a].append((w, b))
            G[b].append((w, a))

    queue = [(0, 1)]
    seen = [False for _ in range(n)]
    results = {1: 0}
    while queue:
        cost, v1 = heappop(queue)
        if not seen[v1 - 1]:
            seen[v1 - 1] = True
            if v1 == n:
                return cost

            for c, v2 in G.get(v1, ()):
                if seen[v2 - 1]:
                    continue

                prev = results.get(v2, None)

                next_cost = cost + c
                if v2 != n:
                    if next_cost % T >= k:
                        next_cost = next_cost + T - (next_cost % T)

                if prev is None or next_cost < prev:
                    results[v2] = next_cost
                    heappush(queue, (next_cost, v2))

    return 0


if __name__ == '__main__':
    n = int(input())
    k = int(input())
    m = int(input())

    result = least_time_to_interview(n, k, m)

    print(result)
