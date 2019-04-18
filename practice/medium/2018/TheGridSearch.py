"""
https://www.hackerrank.com/challenges/the-grid-search/problem

Score: 30/30
Submitted: 2018
"""


def grid_search(G, P):
    first_row = P[0]
    row_len = len(first_row)
    for i in range(len(G) - len(P) + 1):
        row = G[i]
        # 1. For each row try to find an occurence of first row of P
        found = row.find(first_row)
        while found != -1:
            # 2. If found, check if the matrix starting at found of size P is the same as P
            matrix_found = [G[idx][found:found + row_len] for idx in range(i, i + len(P))]
            if P == matrix_found:
                return 'YES'

            # 3. If not, keep finding in actual row
            found = row.find(first_row, found + 1)

    return 'NO'


if __name__ == "__main__":
    t = int(input())
    for __ in range(t):
        R, C = list(map(int, input().split()))
        G = []
        for __ in range(R):
            G_t = str(input())
            G.append(G_t)
        r, c = list(map(int, input().split()))
        P = []
        for __ in range(r):
            P_t = str(input())
            P.append(P_t)
        result = grid_search(G, P)
        print(result)
