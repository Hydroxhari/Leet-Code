class Solution(object):
    def twoSum(self, n, t):

        d={}
        for i,j in enumerate(n):
            if t-j in d:
                return [d[t-j],i]
            d[j]=i
            
