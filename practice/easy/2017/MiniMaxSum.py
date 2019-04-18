"""
https://www.hackerrank.com/challenges/mini-max-sum/problem

Score: 10/10
Submitted: 2017
"""

arr = sorted(list(map(int, input().split())))
print(sum(arr[:4]), sum(arr[1:]))
