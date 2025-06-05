class Solution(object):
    def maxSubstrings(self, s):
        res = 0
        pos = {}
        for i, c in enumerate(s):
            if c not in pos:
                pos[c] = i
            elif i - pos[c] + 1 >= 4:
                res += 1
                pos = {}
        return res