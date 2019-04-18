"""
https://www.hackerrank.com/challenges/string-construction/problem

Score: 25/25
Submitted: 2018
"""


def string_construction(s):
    return len(set(list(s)))


if __name__ == "__main__":
    q = int(input())
    for __ in range(q):
        s = input()
        result = string_construction(s)
        print(result)
