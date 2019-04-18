"""
https://www.hackerrank.com/challenges/runningtime/problem

Score: 30/30
Submitted: 2017
"""

n, arr = int(input()), [number for number in input().split()]
counter = 0

for i in range(1, n):
    while (int(arr[i]) < int(arr[i - 1])) * i:
        arr[i], arr[i - 1] = arr[i - 1], arr[i]
        i -= 1
        counter += 1

print(counter)
