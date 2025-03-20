class Solution(object):
    def maxOperations(self, n, k):

        c=Counter(n)

        s=set(n)
        o=0

        for i in s:
            t=k-i
            if t in c:
                if i==t:
                    m=c[t]//2
                else:
                    m=min(c[t],c[i])
                c[t]-=m
                c[i]-=m
                o+=m

        return o
            
            
        