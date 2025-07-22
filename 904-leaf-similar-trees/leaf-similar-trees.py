# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, r1, r2):
        
        l=[]
        def dp(n):
            if not n.left and not n.right:
                l.append(n.val)
                return
            
            if n.left:
                dp(n.left)
            if n.right:
                dp(n.right)
            return 
        
        dp(r1)
        ll=len(l)
        dp(r2)
        return l[:ll]==l[ll:]
