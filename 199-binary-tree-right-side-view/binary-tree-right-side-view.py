# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, r):

        if not r:
            return []
        
        q=deque([r])
        a=[]
        while q:
            l=len(q)
            for i in range(l):
                e=q.popleft()
                if i==l-1:
                    a.append(e.val)
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
        return a


