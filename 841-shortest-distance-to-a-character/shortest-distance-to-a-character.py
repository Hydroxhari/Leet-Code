class Solution(object):
    def shortestToChar(self, s, c):
        n = len(s)
        res = [0] * n
        prev = float('-inf')

        # First pass: left to right
        for i in range(n):
            if s[i] == c:
                prev = i
            res[i] = i - prev if prev != float('-inf') else float('inf')

        # Second pass: right to left
        prev = float('inf')
        for i in range(n - 1, -1, -1):
            if s[i] == c:
                prev = i
            res[i] = min(res[i], prev - i if prev != float('inf') else float('inf'))

        return res
