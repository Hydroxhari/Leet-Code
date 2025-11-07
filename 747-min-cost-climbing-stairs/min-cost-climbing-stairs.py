class Solution(object):
    def minCostClimbingStairs(self, c):
        
        c=c+[0]
        n=[0]*(len(c))
        n[0]=c[0]
        n[1]=c[1]

        for i in range(2,len(c)):
            n[i]=c[i]+min(n[i-1],n[i-2])
        return n[-1]

