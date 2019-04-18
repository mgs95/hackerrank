"""
https://www.hackerrank.com/contests/w37/challenges/superior-characters/problem

Score: 27.56/30
Submitted: 2018
Difficulty: Medium
"""


def maximum_superior_characters(freq):
    numbers = list(filter(lambda x: x, freq))

    sum_numbers = sum(numbers)
    half = (sum_numbers - 1) / 2

    count = 0
    count_limit = sum_numbers - half
    upper = 0

    while count <= count_limit and upper < len(numbers):
        count += numbers[upper]
        upper += 1

    remain = half + count - sum_numbers
    count -= numbers[upper - 1]

    remain2 = min(remain, max(count - 1, 0))

    return int(half - remain + remain2)


if __name__ == '__main__':
    t = int(input())

    for __ in range(t):
        freq = list(map(int, input().split()))

        result = maximum_superior_characters(freq)
        print(result)
