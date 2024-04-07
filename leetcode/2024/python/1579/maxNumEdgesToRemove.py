class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n+1)]
        self.rank = [0 for _ in range(n+1)]
        
    def find(self, n):
        res = n
        while res != self.parent[res]:
            self.parent[res] = self.parent[self.parent[res]]
            res = self.parent[res]
        return res
    
    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.rank[p1] += self.rank[p2]
            self.parent[p2] = p1
        else:
            self.rank[p2] += self.rank[p1]
            self.parent[p1] = p2
        self.n -= 1
        return True
    
    def isConn(self):
        return self.n == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        alice = UnionFind(n)
        bob = UnionFind(n)
        for t, u, v in edges:
            if t == 3:
                cnt += (alice.union(u, v) | bob.union(u, v))
        for t, u, v in edges:
            if t == 1:
                cnt += (alice.union(u, v))
            elif t == 2:
                cnt += (bob.union(u, v))
        if alice.isConn() and bob.isConn():
            return len(edges) - cnt
        else:
            return -1
