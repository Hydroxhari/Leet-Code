class Solution(object):
    def canPlaceFlowers(self, f, n):

        if n==0:
            return True
        dp=[0]+f+[0]
        k=n

        for i in range(1,len(f)+1):
            print(dp[i])
            if dp[i]==0 and dp[i-1]==0 and dp[i+1]==0:
                dp[i]=1
                n-=1
            if n==0:
                return True
        
        dp=[0]+f[::-1]+[0]
        n=k

        for i in range(1,len(f)+1):
            if dp[i]==0 and dp[i-1]==0 and dp[i+1]==0:
                dp[i]=1
                n-=1
            if n==0:
                return True
        return False