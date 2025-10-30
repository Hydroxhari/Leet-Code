class Solution(object):
    def maxProfit(self, p):

        c=float('inf')
        m=0
        for i in p:
            c=min(c,i)
            m=max(m,i-c)
        return m
        