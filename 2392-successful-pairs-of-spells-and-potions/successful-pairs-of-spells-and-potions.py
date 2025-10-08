class Solution(object):
    def successfulPairs(self, s, p, k):

        p.sort(reverse=True)
        fl=[]
        def bt(n):
            l,h=0,len(p)-1
            ans=0
            while l<=h:
                m=(l+h)//2
                if p[m]*n>=k:
                    ans=m+1
                    l=m+1
                else:
                    h=m-1
            return ans
        
        for i in s:
            fl.append(bt(i))
        return fl

        