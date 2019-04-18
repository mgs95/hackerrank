"""
https://www.hackerrank.com/challenges/fair-rations/problem

Score: 25/25
Submitted: 2018
"""


def fair_rations(B):
    counter = 0
    for i in range(len(B) - 1):
        if B[i] % 2 != 0:
            B[i] += 1
            B[i + 1] += 1
            counter += 2

    if B[-1] % 2 != 0:
        return 'NO'
    return counter


if __name__ == "__main__":
    N = int(input())
    B = list(map(int, input().split()))
    result = fair_rations(B)
    print(result)
