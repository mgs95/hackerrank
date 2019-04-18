"""
https://www.hackerrank.com/challenges/beautiful-binary-string/problem

Score: 20/20
Submitted: 2018
"""


def beautiful_binary_string(b):
    return b.count('010')


if __name__ == "__main__":
    n = int(input())
    b = input()
    result = beautiful_binary_string(b)
    print(result)
