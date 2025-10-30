class Solution(object):
    def maxSubArray(self, n):

        m=n[0]
        s=0
        for i in n:
            s=max(s+i,i)
            m=max(m,s)
        return m