"""
https://www.hackerrank.com/challenges/truck-tour/problem

Score: 50/50
Submitted: May 19th, 2019
Difficulty: Hard
"""


# !/bin/python3


def truck_tour(petrol_pumps):
    """
    Calculates the first point from where the truck will be able to complete
    the circle
    """
    # Stores difference between capacity and distance to next station
    diffs = list(map(lambda x: x[0] - x[1], petrol_pumps))

    initial_station = 0
    fuel = 0

    # Starting from station 0, adds the next station to the queue, if fuel is
    # negative sets initial_station to the next station and keep adding stations
    for idx in range(len(petrol_pumps)):
        fuel += diffs[idx]

        if fuel < 0:
            fuel = 0
            initial_station = idx + 1

    print(initial_station)


if __name__ == '__main__':
    n = int(input())

    petrol_pumps = []

    for _ in range(n):
        petrol_pumps.append(list(map(int, input().split())))

    truck_tour(petrol_pumps)
