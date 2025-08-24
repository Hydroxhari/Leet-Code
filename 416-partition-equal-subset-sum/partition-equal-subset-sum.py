class Solution(object):
    def canPartition(self, n):

        s=sum(n)
        if s%2!=0:
            return False
            
        r=s//2

        dp=[1]+[0]*(r)

        for i in n:
            for j in range(r,i-1,-1):
                dp[j]=dp[j] or dp[j-i]
                
        return dp[-1]==1