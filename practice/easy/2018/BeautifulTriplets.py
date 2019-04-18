"""
https://www.hackerrank.com/challenges/beautiful-triplets/problem

Score: 20/20
Submitted: 2018
"""


def beautiful_triplets(d, arr):
    result = 0
    for i in arr[:-2]:
        j = i + d
        k = j + d

        if j in arr and k in arr:
            result += 1

    return result


if __name__ == "__main__":
    __, d = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    result = beautiful_triplets(d, arr)
    print(result)
