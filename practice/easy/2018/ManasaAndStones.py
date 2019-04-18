"""
https://www.hackerrank.com/challenges/manasa-and-stones/problem

Score: 30/30
Submitted: 2018
"""

from itertools import combinations_with_replacement


def stones(n, a, b):
    combinations = list(combinations_with_replacement([a, b], n-1))
    return sorted(set(map(sum, combinations)))


if __name__ == "__main__":
    T = int(input())
    for __ in range(T):
        n = int(input())
        a = int(input())
        b = int(input())
        result = stones(n, a, b)
        print(" ".join(map(str, result)))
