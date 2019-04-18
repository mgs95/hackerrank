"""
https://www.hackerrank.com/challenges/strange-advertising/problem

Score: 15/15
Submitted: Feb, 2019
"""

from math import floor

result = 0
people = 5

for d in range(int(input())):
    new_people = floor(people / 2)
    result += new_people

    people = new_people * 3

print(result)
