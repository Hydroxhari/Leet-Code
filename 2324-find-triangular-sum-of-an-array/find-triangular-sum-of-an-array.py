class Solution(object):
    def triangularSum(self, n):

        while len(n)!=1:
            na=[]
            for i in range(1,len(n)):
                na.append((n[i]+n[i-1])%10)
            n=na
        return n[-1]