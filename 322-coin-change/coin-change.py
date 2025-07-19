class Solution(object):
    def coinChange(self, c, a):


        memo={}
        def dp(a):
            if a==0:
                return 0
            if a in memo:
                return memo[a]
            m=float('inf')
            for i in c:
                if a-i>=0:
                    m=min(m,1+dp(a-i))

            memo[a]=m
            return m

        return dp(a) if dp(a)!=float('inf') else -1