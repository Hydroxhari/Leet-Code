class Solution(object):
    def change(self, a, c):

        dp=[0]*(a+1)
        dp[0]=1
        for i in c:
            for j in range(i,a+1):
                dp[j]+=dp[j-i]
        return dp[-1]