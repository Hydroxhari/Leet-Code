# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self,root, p, q):
        self.ans = None

        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            mid = node == p or node == q

            if mid + left + right >= 2:
                self.ans = node

            return mid or left or right

        dfs(root)
        return self.ans
