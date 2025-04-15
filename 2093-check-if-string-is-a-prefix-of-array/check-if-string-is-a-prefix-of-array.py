class Solution(object):
    def isPrefixString(self, s, w):
        l1=len(s)
        for i in w:
            l1-=len(i)
            if l1<1:
                break
        if l1<0:
            return False
    
        w = ''.join(w)
        return w.startswith(s)
        