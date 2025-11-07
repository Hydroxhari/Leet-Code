class Solution(object):
    def minCostClimbingStairs(self, c):

        c=c+[0]
        f=c[0]
        s=c[1]

        for i in range(2,len(c)):
            ns=c[i]+min(f,s)
            f=s
            s=ns
        return s

