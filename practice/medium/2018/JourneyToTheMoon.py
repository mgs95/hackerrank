"""
https://www.hackerrank.com/challenges/journey-to-the-moon/problem

Score: 50/50
Submitted: Jun, 2018
"""

from collections import defaultdict


def journey_to_moon(n, astronaut):
    connections = defaultdict(list)

    for a1, a2 in astronaut:
        connections[a1].append(a2)
        connections[a2].append(a1)

    countries = []

    nodes_to_process = n
    visited = [False for _ in range(n)]

    while nodes_to_process:
        # If no more connections, rest of astronauts are alone in their connections
        if not connections:
            for _ in range(nodes_to_process):
                countries.append(1)
            break

        # DFS search
        to_study = [next(iter(connections))]
        size = 0

        while to_study:
            size += 1
            act = to_study.pop()
            visited[act] = True
            nodes_to_process -= 1

            for a in connections[act]:
                if not visited[a]:
                    to_study.append(a)
                    visited[a] = True

            del connections[act]

        countries.append(size)

    result = 0
    for c in countries:
        n -= c
        result += c * n

    return result


if __name__ == '__main__':
    n, p = list(map(int, input().split()))

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().split())))

    result = journey_to_moon(n, astronaut)

    print(result)
