class Solution(object):
    def maxAdjacentDistance(self, n):
        m=0
        for i in range(0,len(n)):
            a=abs(n[i]-n[i-1])
            m=max(m,a)
        return m
        