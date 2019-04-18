"""
https://www.hackerrank.com/challenges/game-of-thrones/problem

Score: 30/30
Submitted: 2018
"""

from collections import Counter


def game_of_thrones(s):
    odd = len(s) % 2
    s = Counter(list(s))
    values = s.values()

    odds = sum(map(lambda v: v % 2, values))

    if (odd and odds == 1) or (not odd and not odds):
        return 'YES'
    return 'NO'


s = input()
result = game_of_thrones(s)
print(result)
