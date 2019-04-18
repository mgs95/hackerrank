"""
https://www.hackerrank.com/challenges/mark-and-toys/problem

Score: 35/35
Submitted: 2018
"""


def maximum_toys(prices, k):
    prices = sorted(prices)
    solution = 0
    spent = 0

    for el in prices:
        spent += el
        if spent > k:
            return solution
        solution += 1

    return solution


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    prices = list(map(int, input().split()))
    result = maximum_toys(prices, k)
    print(result)
