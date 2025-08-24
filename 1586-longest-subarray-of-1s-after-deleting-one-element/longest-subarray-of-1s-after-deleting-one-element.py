class Solution(object):
    def longestSubarray(self, n):


        k=1
        i=0
        m=0

        for j in range(len(n)):
            if n[j]==0:
                k-=1
            while k<0:
                if n[i]==0:
                    k+=1
                i+=1
            m=max(m,j-i+1)
        return m-1
