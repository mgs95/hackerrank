"""
https://www.hackerrank.com/contests/w37/challenges/the-average-rating-of-top-employees/problem

Score: 10/10
Submitted: 2018
Difficulty: Easy
"""


def average_of_top_employees(rating):
    rating = list(filter(lambda x: x >= 90, rating))

    result = sum(rating) / len(rating)
    result_str = str(result)

    if len(result_str.split('.')[1]) <= 2:
        print("%.2f" % result)
        return

    first, last = result_str.split('.')
    r_dec = last[1] if int(last[2]) < 5 else str(int(last[1]) + 1)
    final_result = first + '.' + last[0] + r_dec

    print(final_result)
    return


if __name__ == '__main__':
    n = int(input())

    rating = []

    for _ in range(n):
        rating_item = int(input())
        rating.append(rating_item)

    average_of_top_employees(rating)
