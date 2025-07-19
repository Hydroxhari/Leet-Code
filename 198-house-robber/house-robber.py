class Solution(object):
    def rob(self, n):

        memo={}
        def dp(i):
            if i>=len(n):
                return 0
            if i in memo:
                return memo[i]
            
            memo[i]=max(dp(i+1),n[i]+dp(i+2))
            return memo[i]
        return dp(0)