"""
https://www.hackerrank.com/challenges/pangrams/problem

Score: 20/20
Submitted: 2018
"""

from string import ascii_lowercase


def pangrams(s):
    letters = list(ascii_lowercase)
    for c in s:
        if c in letters:
            letters.pop(letters.index(c))

    return 'pangram' if not letters else 'not pangram'


if __name__ == '__main__':
    sentence = input()
    print(pangrams(sentence.lower()))
