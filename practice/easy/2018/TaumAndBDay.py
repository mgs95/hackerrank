"""
https://www.hackerrank.com/challenges/taum-and-bday/problem

Score: 25/25
Submitted: 2018
"""


def taum_bday(b, w, x, y, z):
    b_and_w = x * b + y * w
    b_to_w = x * (b + w) + z * w
    w_to_b = y * (b + w) + z * b

    return min(b_and_w, b_to_w, w_to_b)


if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        b, w = list(map(int, input().split()))
        x, y, z = list(map(int, input().split()))
        result = taum_bday(b, w, x, y, z)
        print(result)
