"""
https://www.hackerrank.com/challenges/icecream-parlor/problem

Score: 30/30
Submitted: 2018
"""


def icecream_parlor(n, arr):
    arr2 = [n - el for el in arr]

    for idx, el in enumerate(arr2):
        if el in arr[idx+1:]:
            return '{} {}'.format(idx+1, arr.index(el, idx+1) + 1)


if __name__ == "__main__":
    t = int(input())
    for a0 in range(t):
        m = int(input())
        n = int(input())
        arr = list(map(int, input().split()))
        print(icecream_parlor(m, arr))
