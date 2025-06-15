class Solution(object):
    def findPermutationDifference(self, s, t):

        d={}
        for i,j in enumerate(t):
            d[j]=i
        
        c=0
        for i,j in enumerate(s):
            c+=abs(i-d[j])
        
        return c


        