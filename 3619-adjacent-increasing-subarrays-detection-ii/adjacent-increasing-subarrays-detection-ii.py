class Solution(object):
    def maxIncreasingSubarrays(self, n):
        el=len(n)
        l=[1]*el

        for i in range(1,el):
            if n[i]>n[i-1]:
                l[i]=l[i-1]+1
        
        p=0
        c=0
        m=0
        for i in range(el):
            if l[i]==1:
                p=c
                c=1
            else:
                c=l[i]
            m=max(m,c//2,min(c,p))
        return m
            
            
