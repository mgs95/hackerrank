"""
https://www.hackerrank.com/challenges/caesar-cipher-1/problem

Score: 15/15
Submitted: 2018
"""

from string import ascii_lowercase, ascii_uppercase


def caesar_cipher(s, k):
    sol = ''

    for c in s:
        if c in ascii_lowercase + ascii_uppercase:
            letters = ascii_lowercase if c in ascii_lowercase else ascii_uppercase
            idx = letters.index(c)
            final_idx = (idx + k) % len(ascii_lowercase)
            sol += letters[final_idx]
        else:
            sol += c

    return sol


if __name__ == "__main__":
    n = int(input())
    s = input()
    k = int(input())
    result = caesar_cipher(s, k)
    print(result)
