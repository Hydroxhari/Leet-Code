# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, r):

        def dp(n,v):
            c=0
            if n.val>=v:
                c+=1
            if n.left:
                c+=dp(n.left,max(n.val,v))
            if n.right:
                c+=dp(n.right,max(n.val,v))
            
            return c

        return dp(r,r.val)