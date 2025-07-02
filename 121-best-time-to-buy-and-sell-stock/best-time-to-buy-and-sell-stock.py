class Solution(object):
    def maxProfit(self, p):

        b=float('inf')
        s=float('-inf')

        for i in p:
            b=min(b,i)
            s=max(s,i-b)
        return s