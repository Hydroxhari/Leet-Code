class Solution(object):
    def findKDistantIndices(self, n, t, k):

        res=set()
        l=0
        for r in range(len(n)):
            if n[r]==t:
                while l<=r:
                    if abs(r-l)<=k:
                        res.add(l)
                    l+=1
        l=len(n)-1
        for r in range(len(n)-1,-1,-1):
            if n[r]==t:
                while l>r:
                    if abs(r-l)<=k:
                        res.add(l)
                    l-=1
        return sorted(res)


        