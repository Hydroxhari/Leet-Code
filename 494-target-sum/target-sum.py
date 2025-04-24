class Solution:
    def findTargetSumWays(self, c: List[int], t: int) -> int:
        from functools import lru_cache

        n = len(c)

        @lru_cache(None)
        def dfs(i,a):
            if i==n and a==t:
                return 1
            
            if i==n:
                return 0
            
            return dfs(i+1,a-c[i]) + dfs(i+1,a+c[i])
        
        return dfs(0,0)

