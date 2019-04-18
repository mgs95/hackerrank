"""
https://www.hackerrank.com/challenges/sherlock-and-squares/problem

Score: 20/20
Submitted: 2018
"""

from math import sqrt

if __name__ == "__main__":
    q = int(input())

    for __ in range(q):
        a, b = list(map(int, input().split()))
        a_s, b_s = list(map(lambda x: int(sqrt(x)), [a, b]))

        result = b_s - a_s
        if a_s * a_s == a:
            result += 1

        print(result)
