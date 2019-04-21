"""
https://www.hackerrank.com/challenges/solve-me-first/problem

Score: 50/50
Submitted: Apr 21st, 2019
Difficulty: Hard
"""


class DisjointSet:
    def __init__(self, N):
        self.nodes = list(range(N))
        self.sizes = [1] * N

    def root(self, node):
        """ Gets the root of a node """
        while self.nodes[node] != node:
            self.nodes[node] = self.nodes[self.nodes[node]]  # Path compression
            node = self.nodes[node]

        return node

    def connected(self, node_a, node_b):
        """ Check if node a and b are connected (same set) """
        root_a, root_b = self.root(node_a), self.root(node_b)

        return root_a == root_b

    def union(self, node_a, node_b):
        """ Merges the sets of nodes a and b """
        # There is no need to merge already connected nodes
        if self.connected(node_a, node_b):
            return

        root_a, root_b = self.root(node_a), self.root(node_b)
        size_a, size_b = self.sizes[root_a], self.sizes[root_b]

        if size_a < size_b:
            self.nodes[root_a] = root_b
            self.sizes[root_b] += size_a
        else:
            self.nodes[root_b] = root_a
            self.sizes[root_a] += size_b

    def size(self, node):
        """ Obtains the set of a node and returns its size """
        root = self.root(node)
        return self.sizes[root]


N, Q = map(int, input().split())

disjoint_set = DisjointSet(N)

for q in range(Q):
    letter, *numbers = input().split()

    if letter == 'Q':
        I = int(numbers[0]) - 1

        print(disjoint_set.size(I))
    else:
        I, J = map(lambda x: int(x) - 1, numbers)

        disjoint_set.union(I, J)
