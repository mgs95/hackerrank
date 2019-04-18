"""
https://www.hackerrank.com/challenges/time-conversion/problem

Score: 15/15
Submitted: 2017
"""

from time import strptime, strftime

time = input()
Time = strptime(time, '%I:%M:%S%p')

print(strftime('%H:%M:%S', Time))
