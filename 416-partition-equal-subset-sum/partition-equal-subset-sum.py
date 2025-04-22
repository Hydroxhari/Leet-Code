class Solution:
    def canPartition(self, n):

        t=sum(n)
        if t%2!=0:
            return False
        
        r = t//2
        dp=[False]*(r+1)
        dp[0]=True

        for i in n:
            for j in range(r,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        
        return dp[r]

