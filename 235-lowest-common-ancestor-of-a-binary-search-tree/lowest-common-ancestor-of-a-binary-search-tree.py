class Solution(object):
    def lowestCommonAncestor(self, r, p, q):

        self.ans = None

        def dfs(n):
            if not n:
                return 0

            # Count matches in left and right
            left = dfs(n.left)
            right = dfs(n.right)
            
            mid = (n == p) or (n == q)
            
            # If any two of left, right, mid are True → LCA
            if left + right + mid >= 2 and not self.ans:
                self.ans = n

            # Return True if this node is p/q or any child has p/q
            return left or right or mid

        dfs(r)
        return self.ans
