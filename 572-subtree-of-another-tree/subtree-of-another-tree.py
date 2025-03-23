# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):

        def enc(n):
            if not n:
                return "N"
            return "#{}{}{}".format(n.val, enc(n.left), enc(n.right))

        e1 = enc(root)    
        e2 = enc(subRoot)   
        return e2 in e1     
        