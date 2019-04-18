"""
https://www.hackerrank.com/challenges/repeated-string/problem

Score: 20/20
Submitted: 2018
"""


def repeated_string(s, n):
    n_a_in_s = s.count('a')
    ns_div, ns_remainder = divmod(n, len(s))
    n_a_in_ns_remainder = s[:ns_remainder].count('a')

    return n_a_in_s * ns_div + n_a_in_ns_remainder


if __name__ == "__main__":
    s = input()
    n = int(input())
    result = repeated_string(s, n)
    print(result)
