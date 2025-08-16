class Solution(object):
    def hasPathSum(self, r, t):

        def dp(n,t):
            if not n:
                return False
            if not n.left and not n.right and t-n.val==0:
                return True
            
            return dp(n.left,t-n.val) or dp(n.right,t-n.val)
        
        return dp(r,t)