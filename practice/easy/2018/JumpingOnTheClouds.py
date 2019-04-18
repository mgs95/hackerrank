"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

Score: 20/20
Submitted: 2018
"""


def jumping_on_clouds(c):
    target = len(c) - 1
    i = 0
    count = 0

    while True:
        if i == target:
            return count
        elif i + 1 == target:
            return count + 1

        i += 1 if c[i + 2] else 2
        count += 1


if __name__ == "__main__":
    n = int(input())
    c = list(map(int, input().split()))
    result = jumping_on_clouds(c)
    print(result)
