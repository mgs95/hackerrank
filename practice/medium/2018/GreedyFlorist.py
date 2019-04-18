"""
https://www.hackerrank.com/challenges/greedy-florist/problem

Score: 35/35
Submitted: 2018
"""


def get_minimum_cost(n, k, c):
    c = sorted(c)

    solution = 0
    multiplier = 1

    while True:
        act_flowers = 0
        for __ in range(k):
            try:
                act_flowers += c.pop()
            except IndexError:
                return solution + multiplier * act_flowers

        solution += multiplier * act_flowers
        multiplier += 1


n, k = list(map(int, input().split()))
c = list(map(int, input().split()))
minimumCost = get_minimum_cost(n, k, c)
print(minimumCost)
