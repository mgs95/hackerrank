"""
https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem

Score: 30/30
Submitted: 2018
"""


def organizing_containers(container):
    total = list(map(sum, zip(*container)))

    for c in container:
        desired = sum(c)
        if desired not in total:
            return 'Impossible'

    return 'Possible'


if __name__ == "__main__":
    q = int(input())
    for __ in range(q):
        n = int(input())
        container = []
        for container_i in range(n):
            container_t = [int(container_temp) for container_temp in input().split()]
            container.append(container_t)
        result = organizing_containers(container)
        print(result)
