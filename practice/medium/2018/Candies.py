"""
https://www.hackerrank.com/challenges/candies/problem

Score: 50/50
Submitted: 2018
"""


def candies(n, arr):
    sol = [1] * n

    # Part 1: solves the problem from left to right
    last = arr[0]
    for idx in range(1, len(arr)):
        act = arr[idx]
        if act > last:
            sol[idx] = sol[idx - 1] + 1

        last = act

    # Part 2: solves the problem from right to left
    last = arr[-1]
    for idx in range(len(arr) - 2, -1, -1):
        act = arr[idx]
        if act > last:
            sol[idx] = max(sol[idx + 1] + 1, sol[idx])

        last = act

    return sum(sol)


if __name__ == "__main__":
    n = int(input())
    arr = []
    for __ in range(n):
        arr_t = int(input())
        arr.append(arr_t)
    result = candies(n, arr)
    print(result)
