class Solution(object):
    def maxSubArray(self, n):
        s=float('-inf')
        m=float('-inf')
        for i in n:
            s=max(i,s+i)
            m=max(m,s)
        return m
