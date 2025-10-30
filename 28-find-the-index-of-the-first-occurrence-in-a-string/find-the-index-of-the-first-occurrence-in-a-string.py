class Solution(object):
    def strStr(self, h, n):
        if n in h:
            return h.index(n)
        return -1

