"""
https://www.hackerrank.com/contests/w38/challenges/cargo-delivery

Score: 62.31/85
Submitted: Jun, 2018
Difficulty: Expert
"""


from collections import defaultdict
from heapq import heappop, heappush, heapify


def shortest_path(graph, source, sink):
    queue = [(0, source, [])]
    visited = set()
    heapify(queue)
    while queue:
        (cost, node, path) = heappop(queue)
        if node not in visited:
            visited.add(node)
            if node == sink:
                return (cost, path)
            for neighbour, cs in graph[node].items():
                c, mc = cs
                if neighbour not in visited:
                    heappush(queue, (cost + c, neighbour, path + [(node, neighbour)]))


def minimum_brokenness(n, m, k, t):
    G = defaultdict(dict)

    for a, b in [list(map(int, input().split())) for _ in range(m)]:
        G[a][b] = [0, 0]
        G[b][a] = [0, 0]

    act_k = k
    while k:
        taken = max(1, act_k // 200)
        act_k -= taken
        path = shortest_path(G, 0, n - 1)[1]
        for a, b in path:
            G[a][b][1] = G[a][b][0]
            G[a][b][0] += taken
        k -= taken

    paths = []
    for a, _ in G.items():
        for _, w in G[a].items():
            paths.append(w[1])

    while t:
        paths = sorted(paths)
        paths[-1] -= 1
        if paths[-1] == -1:
            return 0
        t -= 1

    return max(paths)


if __name__ == '__main__':
    n, m, k, t = list(map(int, input().split()))
    result = minimum_brokenness(n, m, k, t)

    print(result)
