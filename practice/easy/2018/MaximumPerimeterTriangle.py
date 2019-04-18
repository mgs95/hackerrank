"""
https://www.hackerrank.com/challenges/maximum-perimeter-triangle/problem

Score: 20/20
Submitted: 2018
"""


def maximum_perimeter_triangle(sticks):
    sticks = sorted(sticks, reverse=True)

    for first_ptr in range(len(sticks) - 2):
        first_stick = sticks[first_ptr]
        for second_ptr in range(first_ptr + 1, len(sticks) - 1):
            second_stick = sticks[second_ptr]
            third_stick = sticks[second_ptr + 1]

            if second_stick + third_stick > first_stick:
                return [third_stick, second_stick, first_stick]

    return [-1]


if __name__ == '__main__':
    n = int(input())

    sticks = list(map(int, input().split()))

    result = maximum_perimeter_triangle(sticks)
    print(' '.join(map(str, result)))
