"""
https://www.hackerrank.com/challenges/insertionsort1/problem

Score: 30/30
Submitted: 2017
"""

__, arr = input(), [n for n in input().split()]

for step in range(-1, -len(arr), -1):
    to_sort = arr[step]
    i = step
    change = False

    try:
        while int(to_sort) < int(arr[i - 1]):
            change = True
            arr[i] = arr[i - 1]
            print(' '.join(arr))

            i -= 1

    except IndexError:
        pass

    arr[i] = to_sort
    if change:
        print(' '.join(arr))
