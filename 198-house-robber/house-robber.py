class Solution(object):
    def rob(self, n):
        l=len(n)
        if l==0:
            return 0
        if l==1:
            return n[0]
            
        dp=[0]*l
        dp[0]=n[0]
        dp[1]=max(n[0],n[1])

        for i in range(2,l):
            dp[i]=max(dp[i-1],n[i]+dp[i-2])

        return dp[l-1]
        