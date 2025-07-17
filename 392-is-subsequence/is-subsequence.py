class Solution(object):
    def isSubsequence(self, s, t):

        if len(s)>len(t):
            return False
        if not s and t:
            return True
        if s and not t:
            return False
        if not s and not t:
            return True

        i,j=0,0
        while j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
            if i==len(s):
                return True
        return False