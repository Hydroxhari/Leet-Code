class Solution(object):
    def maxProfit(self, p, f):

        l=len(p)
        b = [0]*l
        s = [0]*l

        b[0] = -p[0]

        for i in range(1,l):
            b[i] = max(b[i-1],s[i-1]- p[i])
            s[i] = max(s[i-1],b[i-1]+p[i]-f)
        
        return s[-1]
        