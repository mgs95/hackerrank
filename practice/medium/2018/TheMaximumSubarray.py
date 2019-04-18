"""
https://www.hackerrank.com/challenges/maxsubarray/problem

Score: 50/50
Submitted: 2018
"""


def max_subarray(arr):
    max_subarr = arr[0]
    max_subseq = max(0, arr[0])

    for idx, el in enumerate(arr[1:]):
        arr[idx + 1] = max(el, arr[idx] + el)
        max_subarr = max(max_subarr, arr[idx + 1])
        max_subseq += max(0, el)

    if max_subseq == 0:
        max_subseq = max_subarr

    return [str(max_subarr), str(max_subseq)]


if __name__ == '__main__':
    t = int(input())

    for __ in range(t):
        __ = input()
        arr = list(map(int, input().split()))

        result = max_subarray(arr)

        print(' '.join(result))
