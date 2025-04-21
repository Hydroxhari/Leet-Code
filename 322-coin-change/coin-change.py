class Solution(object):
    def coinChange(self, c, a):

        dp=[float('inf')]*(a+1)
        dp[0]=0

        for i in c:
            for x in range(i,a+1):
                dp[x]=min(dp[x],1+dp[x-i])
        
        return dp[a] if dp[a]!=float('inf') else -1
