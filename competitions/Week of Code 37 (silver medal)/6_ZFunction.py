"""
https://www.hackerrank.com/contests/w37/challenges/z-function/problem

Score: 43.18/100
Submitted: 2018
Difficulty: Expert
"""


from itertools import product

ALPHABET = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-_=+'


def z_algo(s):
    S = len(s)
    Z = [0] * S

    ptr_right = 0
    ptr_left = 0
    for k in range(1, S):
        if k > ptr_right:
            n = 0
            while n + k < len(s) and s[n] == s[n + k]:
                n += 1
            Z[k] = n
            if n > 0:
                ptr_left = k
                ptr_right = k + n - 1
        else:
            p = k - ptr_left
            R = ptr_right - k + 1

            if Z[p] < R:
                Z[k] = Z[p]
            else:
                i = ptr_right + 1
                while i < len(s) and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k

                ptr_left = k
                ptr_right = i - 1
    return Z


def z_function(n, k):
    strings = product(ALPHABET[:k], repeat=n)
    count = 0
    first_letter = None

    for s in strings:
        if s[0] != first_letter:
            if first_letter == None:
                first_letter = s[0]
                count += max(z_algo(s))
            else:
                return count * k
        else:
            count += max(z_algo(s))

    return count


if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    result = z_function(n, k)
    print(result)
