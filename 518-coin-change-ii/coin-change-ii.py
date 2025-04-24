class Solution:
    def change(self, a: int, c: List[int]) -> int:
        from functools import lru_cache

        n = len(c)

        @lru_cache(None)
        def dfs(i,a):
            if a==0:
                return 1
            if a<0 or i==n:
                return 0

            return dfs(i,a-c[i]) + dfs(i+1,a)

        return dfs(0,a)