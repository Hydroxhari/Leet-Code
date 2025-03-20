class Solution(object):
    def maxOperations(self, n, t):

        n.sort()
        l,r=0,len(n)-1
        o=0
        while l<r:
            s=n[r]+n[l]
            if s==t:
                o+=1
                l+=1
                r-=1
            elif s>t:
                r-=1
            else:
                l+=1            
        return o
        