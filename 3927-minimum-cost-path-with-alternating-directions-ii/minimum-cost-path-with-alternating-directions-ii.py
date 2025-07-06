from functools import lru_cache
from typing import List

class Solution: 
    def minCost(self, m: int, n: int, w: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(i, j, parity):
            if i == m - 1 and j == n - 1:
                return 0

            if parity == 1:
                # Even second → must wait
                return w[i][j] + dfs(i, j, 0)
            else:
                # Odd second → can move
                res = float('inf')
                if i + 1 < m:
                    res = min(res, dfs(i + 1, j, 1) + (i + 2) * (j + 1))
                if j + 1 < n:
                    res = min(res, dfs(i, j + 1, 1) + (i + 1) * (j + 2))
                return res

        # Start at second 1 → odd parity (0)
        return (0 + 1) * (0 + 1) + dfs(0, 0, 0)
