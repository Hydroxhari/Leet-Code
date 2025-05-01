class Solution(object):
    def shortestToChar(self, s, c):
        
        l=[]
        p=float('-inf')

        for i in range(len(s)):
            if s[i]==c:
                l.append(0)
                p=i
            else:
                l.append(min(abs(i-p),abs((s.find(c,i))-i)))

        return l