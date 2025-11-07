class Solution(object):
    def rob(self, n):

        d=defaultdict(int)
        def dp(i):
            if i in d:
                return d[i]
            if i>=len(n):
                return 0
            
            t=n[i]+dp(i+2)
            dt=dp(i+1)
            
            d[i]=max(t,dt)
            return d[i]
        
        return dp(0)