"""
https://www.hackerrank.com/challenges/the-birthday-bar/problem

Score: 10/10
Submitted: 2017
"""


def solve(n, bar, val, size):
    count = 0
    for i in range(n):
        if i + size <= n:
            count += 1 * (sum(bar[i:i + size]) == val)

    return count


n = int(input())
bar = list(map(int, input().split()))
val, size = list(map(int, input().split()))
result = solve(n, bar, val, size)

print(result)
