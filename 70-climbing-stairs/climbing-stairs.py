class Solution(object):
    def climbStairs(self, n):

        if n==1:
            return 1
        f=1
        s=2
        for i in range(2,n):
            ns=f+s
            f=s
            s=ns
        return s
