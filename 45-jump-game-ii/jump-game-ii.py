class Solution(object):
    def jump(self, n):

        dp=[float('inf')]*len(n)
        dp[0]=0

        for i in range(len(n)):
            for j in range(i+1,i+n[i]+1):
                if j<len(dp):
                    dp[j]=min(dp[i]+1,dp[j])
        return dp[-1] if dp[-1]!=float('inf') else -1
