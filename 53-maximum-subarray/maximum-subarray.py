class Solution(object):
    def maxSubArray(self, n):
        dp=[0]*len(n)
        dp[0]=n[0]

        for i in range(1,len(n)):
            dp[i]=max(n[i],dp[i-1]+n[i])
        
        print(dp)
        return max(dp)