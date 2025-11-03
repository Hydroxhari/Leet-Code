class Solution(object):
    def minCost(self, c, n):

        a=0
        j=0
        for i in range(1,len(c)):
            if c[i]==c[j]:
                if n[i]>n[j]:
                    a+=n[j]
                    j=i
                else:
                    a+=n[i]
            else:
                j=i
        
        return a