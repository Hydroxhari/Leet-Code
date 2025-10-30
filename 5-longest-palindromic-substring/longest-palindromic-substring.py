class Solution(object):
    def longestPalindrome(self, s):
        
        def ep(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        a=''
        for i in range(len(s)):
            f = ep(i,i)
            d = ep(i,i+1)

            if len(f)>len(a):
                a=f
            if len(d)>len(a):
                a=d
        return a
        