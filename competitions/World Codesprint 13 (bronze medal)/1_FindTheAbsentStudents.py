"""
https://www.hackerrank.com/contests/world-codesprint-13/challenges/find-the-absent-students

Score: 10/10
Submitted: 2018
Difficulty: Easy
"""


def find_the_absent_students(n, a):
    total = set(range(1, n + 1))
    present = set(a)

    result = list(total - present)

    return list(map(str, sorted(result)))


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))

    r = find_the_absent_students(n, a)

    print(' '.join(r))
