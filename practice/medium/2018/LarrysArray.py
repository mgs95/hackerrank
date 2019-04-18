"""
https://www.hackerrank.com/challenges/larrys-array/problem

Score: 40/40
Submitted: 2018
"""

"""
Every move consists on two swaps:
    [A, B, C] |---(swap A and B)--> [B, A, C] |---(swap A and C)--> [B, C, A]

The number of swaps in insertion sort is minimum amount of swaps to sort the array.
Other options consists on swapping two times the same numbers so the number of swaps
can be described as N + 2*x where N is the minimum amount of swaps and x is any positive
integer.

Moves consist on two swaps, so in order to have a sorteable array, N must be even.
"""


def larrys_array(A):
    count = 0
    for i in range(1, len(A)):
        a = A[i]
        for j in range(i - 1, -1, -1):
            b = A[j]
            if b > a:
                count += 1
                A[i], A[j] = A[j], A[i]
            i = j

    return 'YES' if not count % 2 else 'NO'


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        n = int(input())
        A = list(map(int, input().split()))
        result = larrys_array(A)
        print(result)
