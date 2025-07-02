class Solution(object):
    def threeSumClosest(self, n, t):

        n.sort()
        r=0
        m=float('inf')
        for i in range(len(n)-2):
            j=i+1
            k=len(n)-1
            while j<k:
                s=n[i]+n[j]+n[k]
                if abs(s-t)<m:
                    m=abs(s-t)
                    r=s
                
                if s==t:
                    return t
                elif s<t:
                    j+=1
                else:
                    k-=1
        return r

