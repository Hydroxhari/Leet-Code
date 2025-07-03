class Solution(object):
    def canPartition(self, n):

        if sum(n)%2!=0:
            return  False
        t=sum(n)//2

        dp=[0]*(t+1)
        dp[0]=1

        for i in n:
            for j in range(t,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
        return dp[-1]==1
