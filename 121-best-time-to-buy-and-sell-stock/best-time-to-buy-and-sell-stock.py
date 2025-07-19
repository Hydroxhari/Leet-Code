class Solution(object):
    def maxProfit(self, p):

        m=float('inf')
        r=0

        for i in p:
            m=min(m,i)
            r=max(r,i-m)
        return r
        