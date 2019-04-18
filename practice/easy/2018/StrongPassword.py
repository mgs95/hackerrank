"""
https://www.hackerrank.com/challenges/strong-password/problem

Score: 15/15
Submitted: 2018
"""

SPECIAL = "!@#$%^&*()-+"


def minimum_number(n, password):
    count = 0

    if not any([c.islower() for c in password]):
        count += 1
    if not any([c.isupper() for c in password]):
        count += 1
    if not any([c.isdigit() for c in password]):
        count += 1
    if not any([c in SPECIAL for c in password]):
        count += 1

    count += max(0, 6 - n - count)

    return count


if __name__ == "__main__":
    n = int(input())
    password = input()
    answer = minimum_number(n, password)
    print(answer)
