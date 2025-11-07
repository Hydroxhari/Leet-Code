class Solution(object):
    def canPartition(self, n):

        s=sum(n)
        m=s//2
        if s%2!=0:
            return False
        
        d=defaultdict(bool)
        def dp(i,r):
            if (i,r) in d:
                return d[(i,r)]
            if r==0:
                return True
            if i>=len(n):
                return False
            
            d[(i,r)] = dp(i+1,r-n[i]) or dp(i+1,r)
            return d[(i,r)]
        
        return dp(0,m)

        