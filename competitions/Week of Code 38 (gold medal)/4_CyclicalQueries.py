"""
https://www.hackerrank.com/contests/w38/challenges/cyclical-queries

Score: 49.85/60
Submitted: Jun, 2018
Difficulty: Hard
"""


from math import log
from bisect import insort


def next_power_of_2():
    return 1 << (n - 1).bit_length()


class SegmentTree:
    def __init__(self, array):
        self.n = (1 << int(log(len(array) - 1, 2) + 1))
        self.tree = array + [[-1, -1, -10 ** 9]] * (2 * self.n - len(array))

        for i in range(self.n, 2 * self.n):
            self.tree[i] = self.tree[i - self.n]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[2 * i], self.tree[2 * i + 1], key=lambda x: x[2])

    def query(self, left, right):
        ans = [-1, -1, -10 ** 9]
        left += (self.n - 1)
        right += (self.n - 1)
        while left <= right:
            if left & 1:
                ans = max(ans, self.tree[left], key=lambda x: x[2])
            if not (right & 1):
                ans = max(ans, self.tree[right], key=lambda x: x[2])
            left = (left + 1) // 2
            right = (right - 1) // 2
        return ans

    def update(self, i, x):
        i += self.n - 1
        self.tree[i][2] = x
        i //= 2
        while i:
            a, b = self.tree[2 * i], self.tree[2 * i + 1]
            if a[2] >= b[2]:
                self.tree[i] = a
            else:
                self.tree[i] = b

            i //= 2

    def __str__(self):
        return '{}, {}'.format(self.n, [x[2] for x in self.tree])


class CyclicalTree:
    def __init__(self, n, links):
        self.N, self.roots, self.get_root = n, [], {}
        self.next_power = next_power_of_2(n)
        self.max_node, self.next_id = n, 0
        self.next_node, self.parents, self.maximums = [], {}, {}

        aw = 0
        self.roots = [[1, 0, 0]]
        self.parents[1] = {1: 0}
        self.get_root[1] = 1
        self.maximums[1] = [1, 0]
        for id, w in enumerate(links[:-1]):
            id += 2
            aw += w
            self.roots.append([id, aw, aw])
            self.get_root[id] = id
            self.parents[id] = {id: 0}
            self.maximums[id] = [id, 0]
        aw += links[-1]
        self.roots[0] = [1, 0, aw]
        self.max_dist = aw

        for _ in range(self.next_power % n):
            self.roots.append([-1, 0, 0])

        self.segment_tree = SegmentTree(self.roots)

    def get_oposite(self, x, get_distance=False):
        X = self.get_root[x]
        a1, a2 = X + 1, self.next_power
        A = self.segment_tree.query(a1, a2)

        local = [X, 0, self.maximums[X][1]]
        local[2] -= self.parents[X][x]

        b1, b2 = 2, X - 1
        B = []
        if b1 > b2:
            pass
        elif b1 == b2:
            B.append(self.roots[X - 2])
        else:
            B.append(self.segment_tree.query(b1, b2))
        if X != 1:
            B.append([1, 0, self.maximums[1][1]])
        if not B:
            B.append([-1, -1, -99999999999999])
        B = max(B, key=lambda x: x[2])

        dA, dB, dLocal = A[:], B[:], local[:]

        dA[2] = A[2] - self.roots[X - 1][1]
        dB[2] = B[2] + self.max_dist - self.roots[X - 1][1]

        Y, _, dist = max([dA, dB, dLocal], key=lambda x: x[2])

        if get_distance:
            return dist, None

        return Y, self.maximums[Y][0]

    def get_new_node(self):
        if not self.next_node:
            self.max_node += 1
            new_node = self.max_node
        else:
            new_node = self.next_node.pop(0)

        return new_node

    def add_node(self, root, x, w):
        new_node = self.get_new_node()
        self.next_id += 1
        new_w = self.parents[root][x] + w
        new_tot_w = new_w + self.roots[root - 1][1]
        self.parents[root][new_node] = new_w

        if new_tot_w >= self.roots[root - 1][2]:
            self.segment_tree.update(root, new_tot_w)

        if new_w > self.maximums[root][1]:
            self.maximums[root] = [new_node, new_w]

        self.get_root[new_node] = root

    def del_node(self, root, x):
        if x <= self.N:
            return None
        mx = [-1, -1]
        del self.parents[root][x]
        del self.get_root[x]

        insort(self.next_node, x)

        for key, value in self.parents[root].items():
            if value >= mx[1]:
                mx = [key, value]

        self.maximums[root] = mx

        new_w = mx[1] + self.roots[root - 1][1]
        if new_w < self.roots[root - 1][2]:
            self.segment_tree.update(root, new_w)

    def __str__(self):
        return str(self.roots)


def cyclical_queries(n, w, m):
    structure = CyclicalTree(n, w)

    for operation, *args in [list(map(int, input().split())) for _ in range(m)]:
        if operation in [1, 2]:
            x, w = args
            if operation == 1:
                Y, y = structure.get_oposite(x)
            else:
                Y, y = structure.get_root[x], x

            structure.add_node(Y, y, w)
        else:
            x = args[0]
            if operation == 3:
                Y, y = structure.get_oposite(x)
                structure.del_node(Y, y)
            else:
                dist, _ = structure.get_oposite(x, get_distance=True)
                print(dist)


if __name__ == '__main__':
    n = int(input())
    w = list(map(int, input().split()))
    m = int(input())

    cyclical_queries(n, w, m)
