"""
https://www.hackerrank.com/challenges/non-divisible-subset/problem

Score: 20/20
Submitted: 2018
"""


def non_divisible_subset(k, arr):
    remainders = [0] * k
    for n in arr:
        remainders[n % k] += 1

    c = min(remainders[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            c += max(remainders[i], remainders[k - i])

    if k % 2 == 0:
        c += 1

    return c


if __name__ == "__main__":
    __, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = non_divisible_subset(k, arr)
    print(result)
