class Solution(object):
    def twoSum(self, n, t):

        d={}

        for i,j in enumerate(n):
            a=t-j
            if a in d:
                return(i,d[a])
            d[j]=i