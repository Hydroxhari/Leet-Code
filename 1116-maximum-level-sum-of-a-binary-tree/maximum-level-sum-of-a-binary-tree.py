# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, r):

        m=float('-inf')
        el=1
        cl=1
        q=deque([r])
        while q:
            l=len(q)
            c=0
            for i in range(l):
                e=q.popleft()
                c+=e.val
                if e.left:
                    q.append(e.left)
                if e.right:
                    q.append(e.right)
            if c>m:
                m=c
                el=cl
            cl+=1
        return el