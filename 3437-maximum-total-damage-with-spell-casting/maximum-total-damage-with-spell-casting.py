from functools import lru_cache
from collections import Counter

class Solution:
    def maximumTotalDamage(self, l):
        c = Counter(l)
        vals = sorted(c)
        n = len(vals)

        @lru_cache(None)
        def dp(i):
            if i >= n:
                return 0
            
            # Option 1: Skip current
            skip = dp(i + 1)

            # Option 2: Take current
            j = i + 1
            while j < n and vals[j] - vals[i] <= 2:
                j += 1
            take = vals[i] * c[vals[i]] + dp(j)

            return max(take, skip)

        return dp(0)
