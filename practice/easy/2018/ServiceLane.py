"""
https://www.hackerrank.com/challenges/service-lane/problem

Score: 20/20
Submitted: 2018
"""


def service_lane():
    result = []
    for a, b in cases:
        result.append(min(width[a:b + 1]))

    return result


if __name__ == "__main__":
    __, t = list(map(int, input().split()))
    width = list(map(int, input().split()))
    cases = []
    for __ in range(t):
        cases_t = list(map(int, input().split()))
        cases.append(cases_t)
    result = service_lane()
    print("\n".join(map(str, result)))
