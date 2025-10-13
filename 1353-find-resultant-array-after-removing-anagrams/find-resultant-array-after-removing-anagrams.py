class Solution(object):
    def removeAnagrams(self, w):
        p=''
        l=[]
        for i in w:
            s=''.join(sorted(i))
            if not p or p!=s:
                p=s
                l.append(i)
        return l