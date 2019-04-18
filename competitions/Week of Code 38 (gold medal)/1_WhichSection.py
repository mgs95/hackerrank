"""
https://www.hackerrank.com/contests/w38/challenges/which-section

Score: 10/10
Submitted: Jun, 2018
Difficulty: Easy
"""


def which_section(n, k, a):
    # Return the section number you will be assigned to assuming you are student number k.
    students = 0

    for section, el in enumerate(a):
        students += el
        if students >= k:
            return section + 1


if __name__ == '__main__':
    t = int(input())

    for __ in range(t):
        n, k, m = list(map(int, input().split()))
        a = list(map(int, input().split()))

        result = which_section(n, k, a)

        print(result)
