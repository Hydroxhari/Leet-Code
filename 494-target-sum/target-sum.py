class Solution(object):
    def findTargetSumWays(self, n, t):

        d=defaultdict(int)
        def dp(i,s):
            if (i,s) in d:
                return d[(i,s)]

            if i==len(n):
                return s==t
            
            d[(i,s)] = dp(i+1,s+n[i]) + dp(i+1,s-n[i])
            return d[(i,s)]
        
        return dp(0,0)