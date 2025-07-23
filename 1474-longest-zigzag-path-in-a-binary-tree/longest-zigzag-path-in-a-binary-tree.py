# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, r: Optional[TreeNode]) -> int:

        @lru_cache(None)
        def dp(n,d):
            if not n:
                return 0
            if d==0:
                return 1+dp(n.left,1)
            if d==1:
                return 1+dp(n.right,0)
        
        m=0
        d= deque([r])
        while d:
            e=d.popleft()
            c=max(dp(e.right,0),dp(e.left,1))
            if e.right:
                d.append(e.right)
            if e.left:
                d.append(e.left)
            m=max(m,c)
        return m
        
