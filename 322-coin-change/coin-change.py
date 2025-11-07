class Solution(object):
    def coinChange(self, c, a):
        n = [float('inf')] * (a + 1)
        n[0] = 0  # base: 0 coins needed for amount 0

        for i in range(1, a + 1):
            for j in c:
                if i - j >= 0:
                    n[i] = min(n[i], 1 + n[i - j])

        return n[a] if n[a] != float('inf') else -1
