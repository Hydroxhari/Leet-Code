class Solution(object):
    def findKDistantIndices(self, n, t, k):

        l=0
        res=[]
        for i in range(len(n)):
            if n[i]==t:
                l=max(l,i-k)
                while l<len(n) and l<=k+i:
                    res.append(l)
                    l+=1
        return res