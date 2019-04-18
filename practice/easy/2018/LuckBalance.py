"""
https://www.hackerrank.com/challenges/luck-balance/problem

Score: 20/20
Submitted: 2018
"""


def luck_balance(n, k, contests):
    total_luck = 0
    important_contests = []

    for luck, importance in contests:
        if importance == 1:
            important_contests.append(luck)
            total_luck -= luck
        else:
            total_luck += luck

    important_contests = sorted(important_contests, reverse=True)

    for idx in range(k):
        try:
            total_luck += 2 * important_contests[idx]
        except IndexError:
            return total_luck

    return total_luck


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    contests = []
    for __ in range(n):
        contests_t = [int(contests_temp) for contests_temp in input().split()]
        contests.append(contests_t)
    result = luck_balance(n, k, contests)
    print(result)
