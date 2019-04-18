"""
https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

Score: 20/20
Submitted: 2018
"""


def climbing_leaderboard(scores, alice):
    results = []
    ranking = len(list(set(scores))) + 1
    pos = len(scores) - 1
    prev = 0
    results = []

    for a in alice:
        if pos != -1:
            while a >= scores[pos]:
                act = scores[pos]
                pos -= 1
                if prev != act:
                    ranking -= 1
                prev = act

                if pos == -1:
                    break

        results.append(ranking)

    return results


if __name__ == "__main__":
    __ = input()
    scores = list(map(int, input().split()))
    __ = input()
    alice = map(int, input().split())
    result = climbing_leaderboard(scores, alice)
    print("\n".join(map(str, result)))
