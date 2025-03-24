class Solution(object):
    def maxProfit(self, p):
        m=0
        for i in range(1,len(p)):
            if p[i]>p[i-1]:
                m+=p[i]-p[i-1]
        return m