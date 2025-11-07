class Solution(object):
    def isValidBST(self, r):

        def dfs(n, lv, rv):
            if not n:
                return True  # empty node is valid

            if n.val <= lv or n.val >= rv:
                return False

            return dfs(n.left, lv, n.val) and dfs(n.right, n.val, rv)

        return dfs(r, float('-inf'), float('inf'))
