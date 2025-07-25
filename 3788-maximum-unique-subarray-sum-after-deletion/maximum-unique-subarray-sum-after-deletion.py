class Solution(object):
    def maxSum(self, n):

        s=set(n)
        mp = sum(i for i in s if i>0)
        return max(mp if mp>0 else -101, max(s))
