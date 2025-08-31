class Solution(object):
    def maxSubArray(self, n):

        r=float('-inf')
        c=float('-inf')
        for i in n:
            c=max(i,c+i)
            r=max(r,c)
        return r
