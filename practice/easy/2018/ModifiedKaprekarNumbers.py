"""
https://www.hackerrank.com/challenges/kaprekar-numbers/problem

Score: 30/30
Submitted: 2018
"""


def kaprekar_numbers(p, q):
    result = []
    for i in range(p, q+1):
        i_2 = str(i * i)
        half = len(i_2) // 2

        try:
            left = int(i_2[:half])
        except ValueError:
            left = 0

        right = int(i_2[half:])

        if left + right == i:
            result.append(i)

    return " ".join(map(str, result)) if result else 'INVALID RANGE'


if __name__ == "__main__":
    p = int(input())
    q = int(input())
    result = kaprekar_numbers(p, q)
    print(result)
