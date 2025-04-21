class Solution(object):
    def longestPalindrome(self, s):

        def e(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
        
        a=''
        for i in range(len(s)):
            t=e(i,i)
            if len(t)>len(a):
                a=t
            t=e(i,i+1)
            if len(t)>len(a):
                a=t
        return a           
        