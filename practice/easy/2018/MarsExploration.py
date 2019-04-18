"""
https://www.hackerrank.com/challenges/mars-exploration/problem

Score: 15/15
Submitted: 2018
"""


def mars_exploration(s):
    count = 0
    for n, c in enumerate('SOS'):
        for idx in range(n, len(s), 3):
            if s[idx] != c:
                count += 1

    return count


if __name__ == "__main__":
    s = input()
    result = mars_exploration(s)
    print(result)
