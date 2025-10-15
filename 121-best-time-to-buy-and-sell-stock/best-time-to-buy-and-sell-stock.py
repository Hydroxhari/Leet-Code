class Solution(object):
    def maxProfit(self, p):

        s=float('inf')
        m=0
        for i in p:
            s=min(s,i)
            m=max(m,i-s)
        return m
        