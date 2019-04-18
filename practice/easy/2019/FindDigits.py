"""
https://www.hackerrank.com/challenges/find-digits/problem

Score: 25/25
Submitted: Mar, 2019
"""

for _ in range(int(input())):
    r = 0

    number = int(input())

    digits = list(map(int, list(str(number))))
    digits = filter(lambda el: el != 0, digits)

    for n in digits:
        r += not number % n

    print(r)
