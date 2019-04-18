"""
https://www.hackerrank.com/challenges/picking-numbers/problem

Score: 20/20
Submitted: 2018
"""


def picking_numbers(a):
    sets = []
    for n in a:
        n_count = a.count(n)
        upper = n_count + a.count(n + 1)
        lower = n_count + a.count(n - 1)
        sets.append(max([upper, lower]))

    return max(sets)


if __name__ == "__main__":
    __ = input()
    a = list(map(int, input().split()))
    result = picking_numbers(a)
    print(result)
