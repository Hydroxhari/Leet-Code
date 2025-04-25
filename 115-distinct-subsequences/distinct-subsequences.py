class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        from functools import lru_cache

        l = len(s)
        r = len(t)
        
        @lru_cache(None)
        def dfs(i,k):
            if k==r:
                return 1

            if i==l:
                return 0

            c,d=0,0
            
            if s[i]==t[k]:
                c= dfs(i+1,k+1) 
            d = dfs(i+1,k)
            
            return c+d
            
        return dfs(0,0)
