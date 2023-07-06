class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    def find(self, x):
        if x == self.root[x]: return x
        return self.find(self.root[x])
    def union(self, x, y):
        X, Y = self.find(x), self.find(y)
        if X != Y: self.root[X] = Y

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        res = [0, 0]
        for u, v in edges:
            U, V = uf.find(u - 1), uf.find(v - 1)
            if U == V: res = [u, v]
            else: uf.union(u - 1, v - 1)
        return res