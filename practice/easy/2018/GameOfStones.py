"""
https://www.hackerrank.com/challenges/game-of-stones-1/problem

Score: 15/15
Submitted: 2018
"""


def game_of_stones(n):
    return 'First' if n % 7 not in [0, 1] else 'Second'


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        n = int(input())
        result = game_of_stones(n)
        print(result)
