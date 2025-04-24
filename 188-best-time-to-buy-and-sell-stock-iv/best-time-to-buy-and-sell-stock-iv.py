class Solution(object):
    def maxProfit(self, k, p):
        from functools import cache
        l=len(p)

        @cache
        def dfs(i,t,buy):
            if i==l or t==0:
                return 0
            
            n=dfs(i+1,t,buy)
            if buy:
                b=dfs(i+1,t,not buy) - p[i]
                return max(b,n)
            else:
                s=dfs(i+1,t-1,not buy) + p[i]
                return max(s,n)
            
        return dfs(0,k,1)