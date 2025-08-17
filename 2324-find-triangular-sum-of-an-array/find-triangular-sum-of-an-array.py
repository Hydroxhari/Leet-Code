class Solution(object):
    def triangularSum(self, n):

        while len(n)>1:
            l=[]
            for i in range(1,len(n)):
                l.append((n[i-1]+n[i])%10)
            n=l
        return n[0]
        