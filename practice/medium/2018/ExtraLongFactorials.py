"""
https://www.hackerrank.com/challenges/extra-long-factorials/problem

Score: 20/20
Submitted: 2018
"""

from functools import reduce

if __name__ == "__main__":
    n = int(input())
    print(reduce(lambda x, y: x*y, range(n, 0, -1)))
