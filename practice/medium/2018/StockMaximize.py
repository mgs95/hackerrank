"""
https://www.hackerrank.com/challenges/stockmax/problem

Score: 50/50
Submitted: 2018
"""


def stockmax(prices):
    prices.append(0)
    last = prices[0]
    maximums = []
    for act in prices[1:]:
        if act < last:
            try:
                while last > maximums[-1]:
                    maximums.pop()
            except IndexError:
                pass
            maximums.append(last)
        last = act

    # print(maximums)

    result = 0
    to_sell = 0

    for price in prices:
        if not maximums:
            break

        if price == maximums[0]:
            maximums.pop(0)
            result += price * to_sell
            to_sell = 0
        else:
            to_sell += 1
            result -= price

    return result


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        _ = int(input())

        prices = list(map(int, input().split()))

        print(stockmax(prices))
