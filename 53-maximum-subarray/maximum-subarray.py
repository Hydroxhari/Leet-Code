class Solution(object):
    def maxSubArray(self, n):

        s=0
        m=float('-inf')

        for i in n:
            s=max(i,i+s)
            m=max(m,s)
        return m