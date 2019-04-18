"""
https://www.hackerrank.com/challenges/acm-icpc-team/problem

Score: 25/25
Submitted: 2018
"""

from itertools import combinations


def acm_team(topic):
    max_topics = 0

    counter = 0
    for t1, t2 in combinations(range(n), 2):
        final_topics = bin(topic[t1] | topic[t2]).count('1')

        if final_topics == max_topics:
            counter += 1
        elif final_topics > max_topics:
            max_topics = final_topics
            counter = 1

    print(max_topics)
    print(counter)


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    topic = []
    for __ in range(n):
        topic_t = int(input(), 2)
        topic.append(topic_t)
    acm_team(topic)
