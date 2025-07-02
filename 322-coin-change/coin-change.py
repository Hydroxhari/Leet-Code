class Solution(object):
    def coinChange(self, c, a):

        dp=[float('inf')]*(a+1)
        dp[0]=0
        for i in range(1,a+1):
            for j in c:
                if i-j>=0:
                    dp[i]=min(dp[i],1+dp[i-j])
        return dp[-1] if dp[-1]!=float('inf') else -1

