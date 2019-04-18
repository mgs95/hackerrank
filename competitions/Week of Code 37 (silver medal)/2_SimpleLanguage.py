"""
https://www.hackerrank.com/contests/w37/challenges/simple-language

Score: 20/20
Submitted: 2018
Difficulty: Easy
"""


def maximum_program_value(instructions):
    max_val = 0

    for inst, val in instructions:
        if inst == 'add':
            max_val = max(max_val, max_val + int(val))
        else:
            max_val = max(max_val, int(val))

    return max_val


if __name__ == '__main__':
    n = int(input())
    instructions = []
    for __ in range(n):
        instructions.append((input().split()))
    result = maximum_program_value(instructions)
    print(result)
