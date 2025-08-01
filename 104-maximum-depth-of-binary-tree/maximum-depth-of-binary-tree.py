# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, r):

        def dp(r):
            if not r:
                return 0
            return 1 + max(dp(r.right),dp(r.left))
        return dp(r)

        