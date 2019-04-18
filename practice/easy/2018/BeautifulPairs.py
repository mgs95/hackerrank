"""
https://www.hackerrank.com/challenges/beautiful-pairs/problem

Score: 30/30
Submitted: 2018
"""

from collections import Counter


def beautiful_pairs(A, B):
    A_nums, B_nums = set(A), set(B)
    A_count, B_count = Counter(A), Counter(B)

    same_nums = A_nums & B_nums
    diff_nums = A_nums - B_nums

    result = 0
    for num in same_nums:
        result += min(A_count[num], B_count[num])

    if diff_nums == set():
        return result - 1

    if result == len(A):
        return result

    return result + 1


if __name__ == "__main__":
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = beautiful_pairs(A, B)
    print(result)
