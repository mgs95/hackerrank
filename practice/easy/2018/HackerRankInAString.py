"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

Score: 20/20
Submitted: 2018
"""


def hackerrank_in_string(s):
    word = 'hackerrank'
    idx = 0
    for c in s:
        letter = word[idx]
        if c == letter:
            idx += 1

        if idx == len(word):
            return 'YES'

    return 'NO'


if __name__ == "__main__":
    q = int(input())
    for __ in range(q):
        s = input()
        result = hackerrank_in_string(s)
        print(result)
