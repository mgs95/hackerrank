"""
https://www.hackerrank.com/challenges/flatland-space-stations/problem

Score: 25/25
Submitted: 2018
"""


def flatland_space_stations(n, c):
    # Add stations tot he beggining and end
    c = sorted([0] + c + [n - 1])
    last = c[0]
    max_dist = 0
    # For each station calculate max distance
    for i, conn in enumerate(c):
        # Second and last stations can only have astrounant from one side
        # so the maximum distance is the distance between side stations
        if i == 1 or i == (len(c) - 1):
            dist = conn - last
        # Other stations can have astronaunts in both sides, so maximum
        # distance is halved
        else:
            dist = (conn - last) // 2

        last = conn
        if dist > max_dist:
            max_dist = dist

    return max_dist


if __name__ == "__main__":
    n, m = list(map(int, input().split()))
    c = list(map(int, input().split()))
    result = flatland_space_stations(n, c)
    print(result)
