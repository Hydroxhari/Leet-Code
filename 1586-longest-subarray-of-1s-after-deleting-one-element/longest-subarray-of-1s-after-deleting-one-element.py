class Solution(object):
    def longestSubarray(self, n):

        j=0
        m=0
        k=1
        for i in range(len(n)):
            if n[i]==0:
                k-=1
            while k<0:
                if n[j]==0:
                    k+=1
                j+=1
            m=max(m,i-j)
        return m
