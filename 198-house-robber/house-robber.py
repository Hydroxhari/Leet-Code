class Solution:
    def rob(self, n: List[int]) -> int:

        @lru_cache(None)
        def dp(i,s):
            if i>=len(n):
                return s
            
            return max(dp(i+2,s+n[i]),dp(i+1,s))

        return dp(0,0)
        