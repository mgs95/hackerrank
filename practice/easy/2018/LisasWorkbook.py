"""
https://www.hackerrank.com/challenges/lisa-workbook/problem

Score: 25/25
Submitted: 2018
"""


def workbook(n, k, arr):
    act_page = 1
    counter = 0

    for chapter in arr:
        for ex in range(1, chapter + 1):
            # Exercise and actual page are the same?
            if ex == act_page:
                counter += 1
            # Is actual exercise the last can fit in the actual page?
            if ex % k == 0:
                act_page += 1
        # No need to increment the actual page if is was increased with the last
        # iterated exercise
        if ex % k != 0:
            act_page += 1

    return counter


if __name__ == "__main__":
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = workbook(n, k, arr)
    print(result)
