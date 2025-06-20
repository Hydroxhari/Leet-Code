class Solution:
    def findParent(self, parent, x):
        if parent[x] != x:
            parent[x] = self.findParent(parent, parent[x])
        return parent[x]

    def union(self, parent, x, y):
        px = self.findParent(parent, x)
        py = self.findParent(parent, y)
        if px == py:
            return False  # cycle found
        parent[py] = px
        return True

    def findRedundantConnection(self, edges):
        n = len(edges)
        parent = [i for i in range(n + 1)]
        
        for u, v in edges:
            if not self.union(parent, u, v):
                return [u, v]
