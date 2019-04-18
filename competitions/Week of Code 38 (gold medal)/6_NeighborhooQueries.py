"""
https://www.hackerrank.com/contests/w38/challenges/neighborhood-queries/problem

Score: 0.17/100
Submitted: 2018
Difficulty: Expert
"""

from collections import defaultdict
from bisect import insort


def neighborhood_queries(a_arr):
    N = len(a_arr)
    G = defaultdict(list)
    a_map = dict()
    solutions = {}

    for i, n in enumerate(a_arr):
        a_map[i] = n

    for a, b in (list(map(int, input().split())) for _ in range(N - 1)):
        a, b = a - 1, b - 1
        G[a].append(b)
        G[b].append(a)

    queries = defaultdict(list)
    original_queries = []

    for u, d, k in (list(map(int, input().split())) for _ in range(int(input()))):
        queries[u - 1].append((d, k))
        original_queries.append((u - 1, d, k))

    for n, data in queries.items():
        data = sorted(data, key=lambda x: x[0])
        visited, stack = set(), [(n, 0)]
        act_layer = 0
        nodes = []
        target_dist, kth = data.pop(0)
        next_layer = 1

        while stack:
            vertex, layer = stack.pop(0)
            insort(nodes, a_map[vertex])

            if vertex not in visited:
                visited.add(vertex)
                for v2 in G[vertex]:
                    if v2 not in visited:
                        stack.append((v2, layer + 1))

                if not stack or stack[0][1] == next_layer:
                    next_layer += 1
                    if act_layer == target_dist:
                        while act_layer == target_dist:
                            new = -1
                            if kth - 1 < len(nodes):
                                new = nodes[kth - 1]
                            solutions[(n, target_dist, kth)] = new
                            if not data:
                                stack = []
                                break
                            target_dist, kth = data.pop(0)
                    act_layer += 1

    for query in original_queries:
        print(solutions[query])


if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().split()))

    neighborhood_queries(a)
