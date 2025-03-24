class Solution(object):
    def isSubsequence(self, s, t):
        if not s and not t:
            return True
        if not t:
            return False
        if not s:
            return True 
        
        p1=0
        p2=0
        while p1<len(s) and p2<len(t):
            if s[p1]==t[p2]:
                p1+=1
                p2+=1
            else:
                p2+=1
        
        if p1==len(s):
            return True
        return False