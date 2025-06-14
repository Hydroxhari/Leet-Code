"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, n):

        h={}

        def dfs(n):
            if n in h:
                return h[n]
            
            c=Node(n.val)
            h[n]=c

            for i in n.neighbors:
                c.neighbors.append(dfs(i))
            
            return c
        
        return dfs(n) if n else None