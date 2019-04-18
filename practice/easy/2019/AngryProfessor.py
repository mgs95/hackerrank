"""
https://www.hackerrank.com/challenges/angry-professor/problem

Score: 20/20
Submitted: Feb, 2019
"""

for _ in range(int(input())):
    a, k = map(int, input().split())
    print(['YES', 'NO'][len(list(filter(lambda el: int(el) <=0, input().split()))) >= k])
