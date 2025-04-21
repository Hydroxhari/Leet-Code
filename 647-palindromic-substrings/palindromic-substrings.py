class Solution(object):
    def countSubstrings(self, s):

        def e(l,r):
            c=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                c+=1
                l-=1
                r+=1
            return c
        
        t=0
        for i in range(len(s)):
            t+=e(i,i)
            t+=e(i,i+1)
        
        return t