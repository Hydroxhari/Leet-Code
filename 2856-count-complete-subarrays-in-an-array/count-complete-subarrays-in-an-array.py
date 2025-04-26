from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, n: List[int]) -> int:
        d = defaultdict(int)
        l = len(set(n))
        j = 0
        c = 0

        for i in range(len(n)):
            d[n[i]] += 1  # fix: count value n[i]

            while len(d) == l:
                c += len(n) - i
                d[n[j]] -= 1  # fix: decrease value n[j]
                if d[n[j]] == 0:
                    del d[n[j]]
                j += 1
        
        return c
