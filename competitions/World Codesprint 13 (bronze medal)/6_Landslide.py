"""
https://www.hackerrank.com/contests/world-codesprint-13/challenges/landslide/problem

Score: 2/75
Submitted: 2018
Difficulty: Hard
"""

from collections import defaultdict

PATHS = 0
CITY = 1
DIST = 2


def landslide(n):
    cities = {}
    for i in range(n):
        cities[i] = {j: [[], 0] for j in range(i + 1, n)}

    g = defaultdict(list)
    possibilities = []
    opts = set()

    for a, b in [input().split() for __ in range(n - 1)]:
        g[int(a) - 1].append(int(b) - 1)
        g[int(b) - 1].append(int(a) - 1)
        possibilities.append(sorted([int(a) - 1, int(b) - 1]))
        opts.add(int(a))
        opts.add(int(b))

    for city in range(n):
        visited = []
        to_visit = [[[], city, 1]]

        while to_visit:
            act = to_visit.pop(0)
            node = g[act[CITY]]
            for leaf in node:
                if leaf not in visited:
                    new_road = list(sorted([act[CITY], leaf]))
                    roads = act[PATHS][:]
                    roads.append(new_road)
                    to_visit.append([roads, leaf, act[DIST] + 1])

                    if leaf >= city:
                        cities[city][leaf] = [roads, act[DIST]]

            visited.append(act[CITY])

    m = int(input())
    destroyed = []

    for row in [input().split() for __ in range(m)]:
        o, a, b = row[0], int(row[1]), int(row[2])
        a, b = list(sorted([a, b]))
        act_path = list(sorted([a - 1, b - 1]))

        if o == 'q':
            result = cities[a - 1][b - 1]

            found = True
            for path in result[0]:
                if path in destroyed:
                    print('Impossible')
                    found = False
                    break
            if found:
                print(result[1])
        elif o == 'd':
            if act_path not in possibilities:
                continue
            if act_path not in destroyed:
                destroyed.append(act_path)
        elif o == 'c':
            if act_path not in possibilities:
                continue
            if act_path in destroyed:
                destroyed.pop(destroyed.index(act_path))


if __name__ == '__main__':
    n = int(input())

    landslide(n)
