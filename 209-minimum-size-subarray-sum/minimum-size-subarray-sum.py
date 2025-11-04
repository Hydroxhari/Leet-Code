class Solution(object):
    def minSubArrayLen(self, t, n):

        l=float('inf')
        j=0
        s=0
        for i in range(len(n)):
            s+=n[i]
            while s>=t:
                l=min(l,i-j+1)
                s-=n[j]
                j+=1
        return l if l!=float('inf') else 0