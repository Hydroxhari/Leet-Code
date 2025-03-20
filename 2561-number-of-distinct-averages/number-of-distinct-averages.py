class Solution(object):
    def distinctAverages(self, n):
        n.sort()
        s=set()
        l,r=0,len(n)-1
        while l<r:
            s.add(float(n[l]+n[r])/2)
            l+=1
            r-=1
        return len(s)
