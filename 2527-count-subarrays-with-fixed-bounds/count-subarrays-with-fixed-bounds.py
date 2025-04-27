class Solution(object):
    def countSubarrays(self, n, l, m):

        a=-1
        b=-1
        d=-1
        c=0
        j=0

        for i in range(len(n)):
            if l>n[i] or n[i]>m:
                d=i
            
            if n[i]==l:
                a=i
            
            if n[i]==m:
                b=i
            
            c+= max(0,min(a,b)-d)
        
        return c


