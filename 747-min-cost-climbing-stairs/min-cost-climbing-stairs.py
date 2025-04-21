class Solution(object):
    def minCostClimbingStairs(self, c):
        n=len(c)
        a,b=c[0],c[1]

        for i in range(2,n):
            a,b=b,c[i]+min(a,b)
        
        return min(a,b)