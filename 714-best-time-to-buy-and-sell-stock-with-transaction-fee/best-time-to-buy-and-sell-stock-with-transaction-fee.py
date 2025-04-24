class Solution(object):
    def maxProfit(self, p, f):

        b = -p[0]
        s=0

        for i in range(1,len(p)):
            b= max(b,s- p[i])
            s= max(s,b+p[i]-f)
        
        return s
        