"""
https://www.hackerrank.com/challenges/almost-sorted/problem

Score: 50/50
Submitted: 2018
"""


def almost_sorted(arr):
    last = arr[0]
    incoincidences = []

    for idx, act in enumerate(arr[1:]):
        if act < last:
            incoincidences.append(idx + 2)
        last = act

    if len(incoincidences) == 1:
        incoincidences.append(incoincidences[0])

    if len(incoincidences) == 2:
        idx_1, idx_2 = incoincidences
        new_arr = arr[:]
        new_arr[idx_1 - 2], new_arr[idx_2 - 1] = new_arr[idx_2 - 1], new_arr[idx_1 - 2]
        if sorted(arr) == new_arr:
            print('yes\nswap {} {}'.format(idx_1 - 1, idx_2))
            return
    else:
        first = incoincidences[0]
        last = incoincidences[-1]
        new_arr = arr[:first - 2] + list(reversed(arr[first - 2:last])) + arr[last:]
        if sorted(arr) == new_arr:
            print('yes\nreverse {} {}'.format(first - 1, last))
            return

    print('no')


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    almost_sorted(arr)
