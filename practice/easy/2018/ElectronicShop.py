"""
https://www.hackerrank.com/challenges/electronics-shop/problem

Score: 15/15
Submitted: 2018
"""

s, __, __ = list(map(int, input().split()))
keyboards = sorted(list(map(int, input().split())))
drives = sorted(list(map(int, input().split())))


# The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
if keyboards[0] + drives[0] > s:
    print(-1)
else:
    money = 0
    for k in keyboards:
        for d in drives:
            m = k + d
            if m <= s and m > money:
                money = m

    print(money)
