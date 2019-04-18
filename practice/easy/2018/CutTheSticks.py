"""
https://www.hackerrank.com/challenges/cut-the-sticks/problem

Score: 25/25
Submitted: 2018
"""


def cut_the_sticks(arr, solution=[]):
    if not arr:
        return solution

    solution.append(len(arr))

    arr = list(map(lambda x: x - min(arr), arr))
    arr = list(filter(lambda x: x > 0, arr))

    return cut_the_sticks(arr, solution)


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = cut_the_sticks(arr)
    print("\n".join(map(str, result)))
