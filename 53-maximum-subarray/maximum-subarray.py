class Solution(object):
    def maxSubArray(self, n):

        s=n[0]
        m=n[0]

        for i in range(1,len(n)):
            s=max(n[i],s+n[i])
            m=max(m,s)
        return m