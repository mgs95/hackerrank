"""
https://www.hackerrank.com/challenges/the-time-in-words/problem

Score: 25/25
Submitted: 2018
"""

NUMBERS = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
           'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fiveteen',
           'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']


def time_in_words(h, m):
    if m <= 30:
        link = 'past'
    else:
        link = 'to'
        m = 60 - m
        h += 1

    hour = NUMBERS[h - 1]

    if m == 0:
        return "{} o' clock".format(hour)
    if m == 15:
        return 'quarter {} {}'.format(link, hour)
    if m == 30:
        return 'half past {}'.format(hour)

    minute_ind = 'minutes' if m % 10 != 1 else 'minute'
    minute = NUMBERS[m - 1] if m <= 20 else NUMBERS[-1] + ' ' + NUMBERS[m % 10 - 1]

    return '{} {} {} {}'.format(minute, minute_ind, link, hour)


if __name__ == "__main__":
    h = int(input())
    m = int(input())
    result = time_in_words(h, m)
    print(result)
