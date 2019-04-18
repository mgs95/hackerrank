"""
https://www.hackerrank.com/contests/w38/challenges/minute-to-win-it

Score: 20/20
Submitted: Jun, 2018
Difficulty: Easy
"""

from collections import Counter


def minute_to_win_it(a, k):
    # Return the minimum amount of time in minutes.
    N = len(a)

    factor = -k
    for idx in range(N):
        a[idx] += factor
        factor -= k

    results = Counter(a)
    longest_subset = results.most_common(1)[0][1]

    return N - longest_subset


if __name__ == '__main__':
    n, k = list(map(int, input().split()))

    a = list(map(int, input().split()))

    result = minute_to_win_it(a, k)

    print(result)
