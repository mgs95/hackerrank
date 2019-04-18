"""
https://www.hackerrank.com/challenges/coin-change/problem

Score: 60/60
Submitted: 2018
"""


def get_ways(n, c):
    """
    Starting at the highest coin, solve exercise with
    n = n - [0|1|2|3|...|N] for N going up until n - N < 0
    and c = c[1:].
    This way it is possible to check how many solutions we can obtain
    with 0|1|2|3|...|N highest coins recursivelly for the following
    subproblems.
    """

    def iterate_coins(n, c, precomputed):
        # If end of recursion, return 1 if final coins can sum n
        if len(c) == 1:
            return n % c[0] == 0

        count = 0
        act_coin_value = 0
        while act_coin_value < n:
            key = (n - act_coin_value, tuple(c[1:]))
            # Use precomputed value if possible
            if key in precomputed:
                count += precomputed[key]
            else:
                adition = iterate_coins(key[0], key[1], precomputed)
                count += adition
                precomputed[key] = adition
            act_coin_value += c[0]

        # Add 1 to count if is possible to sum n without using lower value coins
        if act_coin_value == n:
            count += 1

        return count

    return iterate_coins(n, c, {})


n, m = list(map(int, input().split()))
c = list(map(int, input().split()))
c = sorted(c, reverse=True)

# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
print(get_ways(n, c))
