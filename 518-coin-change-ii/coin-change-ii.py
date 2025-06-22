class Solution:
    def change(self, a: int, c: List[int]) -> int:

        c.sort()
        @lru_cache(None)
        def dp(a,s):
            if a==0:
                return 1 
            if a<0 or s==len(c):
                return 0
            
            return dp(a-c[s],s)+dp(a,s+1)

        return dp(a,0)