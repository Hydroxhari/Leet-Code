class Solution(object):
    def isBalanced(self, r):
        
        def dfs(n):
            if not n:
                return 0
            l = dfs(n.left)
            ri = dfs(n.right)
            if l == -1 or ri == -1 or abs(l - ri) > 1:
                return -1
            return 1 + max(l, ri)
        
        return dfs(r) != -1
