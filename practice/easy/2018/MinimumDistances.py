"""
https://www.hackerrank.com/challenges/minimum-distances/problem

Score: 20/20
Submitted: 2018
"""


def minimum_distances(a):
    counter_dict = {}
    max_distance = len(a)

    for i, el in enumerate(a):
        if el in counter_dict:
            el_last_i, el_last_distance = counter_dict[el]
            distance = i - el_last_i
            new_distance = el_last_distance if el_last_distance < distance else distance
            counter_dict[el] = [i, new_distance]
        else:
            counter_dict[el] = [i, max_distance]

    min_distance = min(counter_dict.values(), key=lambda x: x[1])[1]

    return -1 if min_distance == max_distance else min_distance


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    result = minimum_distances(a)
    print(result)
