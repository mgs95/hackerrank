"""
https://www.hackerrank.com/challenges/torque-and-development/problem

Score: 30/30
Submitted: 2018
"""

from collections import defaultdict


def roads_and_libraries(n, c_lib, c_road, roads):
    if c_road > c_lib:
        return c_lib * n

    connections = defaultdict(list)
    n_groups, n_roads = 0, 0

    # Builds graph
    for c1, c2 in roads:
        connections[c1].append(c2)
        connections[c2].append(c1)

    visited = [False for _ in range(n)]
    nodes_to_process = n
    while nodes_to_process > 0:
        # If no more connections, rest of nodes are unique
        if not connections:
            n_groups += nodes_to_process
            break

        # DFS search
        to_study = [next(iter(connections))]

        while to_study:
            act = to_study.pop()
            visited[act - 1] = True
            nodes_to_process -= 1

            for c in connections[act]:
                if not visited[c - 1]:
                    to_study.append(c)
                    visited[c - 1] = True
                    n_roads += 1

            del connections[act]

        n_groups += 1

    return c_road * n_roads + c_lib * n_groups


if __name__ == '__main__':
    q = int(input())

    for _ in range(q):
        n, m, c_lib, c_road = list(map(int, input().split()))

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().split())))

        result = roads_and_libraries(n, c_lib, c_road, cities)

        print(result)
