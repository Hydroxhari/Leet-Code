class Solution:
    def minPathSum(self, dp: List[List[int]]) -> int:
        
        m,n=len(dp),len(dp[0])

        for i in range(1,m):
            dp[i][0]+=dp[i-1][0]
        for j in range(1,n):
            dp[0][j]+=dp[0][j-1]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=min(dp[i][j]+dp[i-1][j],dp[i][j]+dp[i][j-1])
        return dp[-1][-1]



