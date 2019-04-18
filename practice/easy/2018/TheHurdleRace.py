"""
https://www.hackerrank.com/challenges/the-hurdle-race/problem

Score: 15/15
Submitted: 2018
"""

if __name__ == "__main__":
    __, k = list(map(int, input().split()))
    height = list(map(int, input().split()))
    print(max(0, max(height)-k))
