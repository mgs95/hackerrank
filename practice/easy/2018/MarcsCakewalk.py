"""
https://www.hackerrank.com/challenges/marcs-cakewalk/problem

Score: 15/15
Submitted: 2018
"""


def marcs_cakewalk(calorie):
    calorie = sorted(calorie, reverse=True)

    result = 0
    for idx in range(len(calorie)):
        result += (2 ** idx) * calorie[idx]

    return result


if __name__ == "__main__":
    n = int(input())
    calorie = list(map(int, input().split()))
    result = marcs_cakewalk(calorie)
    print(result)
