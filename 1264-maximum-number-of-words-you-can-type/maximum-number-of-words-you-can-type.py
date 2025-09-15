class Solution(object):
    def canBeTypedWords(self, t, b):
        l = t.split(' ')
        sb=set(b)
        c=0
        for i in l:
            si = set(i)
            if len(si&sb)==0:
                c+=1
        return c        