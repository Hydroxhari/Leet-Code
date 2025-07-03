class Solution(object):
    def canPartition(self, n):

        s=sum(n)
        if s%2!=0:
            return False
        t=s//2

        memo={}

        def dp(r,i):
            if (r,i) in memo:
                return memo[(r,i)]
            if r==0:
                memo[(r,i)]=True
                return True
            if r<0 or i==len(n):
                memo[(r,i)]=False
                return False
            


            memo[(r,i)]=dp(r-n[i],i+1) or dp(r,i+1)
            return memo[(r,i)]
        
        return dp(t,0)