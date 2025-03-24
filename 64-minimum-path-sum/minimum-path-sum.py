class Solution(object):
    def minPathSum(self, g):
        m,n=len(g),len(g[0])
        dp=g
        
        for i in range(1,m):
            dp[i][0]+=dp[i-1][0]
        for j in range(1,n):
            dp[0][j]+=dp[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]+=min(dp[i-1][j],dp[i][j-1])
        
        return dp[m-1][n-1]