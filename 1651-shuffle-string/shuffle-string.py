class Solution(object):
    def restoreString(self, s, l):

        d={}
        for i in range(len(s)):
            d[l[i]]=s[i]
        
        a=''
        for i in range(len(s)):
            a+=d[i]
        
        return a

        