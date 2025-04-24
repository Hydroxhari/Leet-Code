class Solution:
    def maxProfit(self, p: List[int]) -> int:

        l=len(p)

        @lru_cache(None)
        def dfs(i,buy):
            if i>=l:
                return 0

            n=dfs(i+1,buy)
            if buy:
                b=dfs(i+1,not buy) - p[i]
                return max(b,n)
            else:
                s=dfs(i+2,not buy) + p[i]
                return max(s,n)

        return dfs(0,1)
        