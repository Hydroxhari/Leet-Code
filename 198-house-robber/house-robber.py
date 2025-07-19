class Solution(object):
    def rob(self, n):

        memo={}
        def dp(i,c):
            if i>=len(n):
                return c
            if (i,c) in memo:
                return memo[(i,c)]
            
            memo[(i,c)]=max(dp(i+1,c),dp(i+2,c+n[i]))
            return memo[(i,c)]
        return dp(0,0)