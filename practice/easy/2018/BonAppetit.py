"""
https://www.hackerrank.com/challenges/bon-appetit/problem

Score: 10/10
Submitted: 2018
"""

__, k = list(map(int, input().split()))
cs = list(map(int, input().split()))
charge = int(input())

total = sum(cs)
not_consummed = cs[k]

anna = (total - not_consummed) / 2
refund = charge - anna

print(int(refund) if refund else 'Bon Appetit')
