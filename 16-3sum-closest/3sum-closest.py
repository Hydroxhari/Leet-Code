class Solution(object):
    def threeSumClosest(self, n, t):

        n.sort()
        m,rn=float('inf'),-1

        for i in range(len(n)-2):
            if i>0 and n[i]==n[i-1]:
                continue
            j=i+1
            k=len(n)-1

            while j<k:
                s=n[i]+n[j]+n[k]
                if s==t:
                    return t
                elif s>t:
                    k-=1
                else:
                    j+=1
                
                if abs(s-t)<m:
                    m=abs(s-t)
                    rn=s
        return rn