class Solution:
    def coinChange(self, c: List[int], a: int) -> int:

        if not a:
            return 0
        c.sort(reverse=True)
        
        @lru_cache(None)
        def dp(a):
            n=float('inf')

            if a==0:
                return 0

            for i in c:
                if a>=i:
                    n=min(1+dp(a-i),n)
            
            return n 
            
        
        return(dp(a) if dp(a)!=float('inf') else -1)
        