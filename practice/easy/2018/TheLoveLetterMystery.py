"""
https://www.hackerrank.com/challenges/the-love-letter-mystery/problem

Score: 20/20
Submitted: 2018
"""

from string import ascii_lowercase

mapper = {z[0]: z[1] for z in zip(ascii_lowercase, range(1, len(ascii_lowercase) + 1))}


def the_love_letter_mystery(s):
    # Transforms characters into integers
    s = list(map(lambda x: mapper[x], list(s)))

    # Gets left and right sides of the future palindrome
    mid, mod = divmod(len(s), 2)
    left = s[:mid]
    right = s[mid + 1 if mod else mid:]
    right = right[::-1]

    # Return difference between characters of both sides (right side reversed)
    return sum([abs(left[idx] - right[idx]) for idx in range(len(left))])


q = int(input())
for __ in range(q):
    s = input()
    result = the_love_letter_mystery(s)
    print(result)
