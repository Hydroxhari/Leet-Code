class Solution(object):
    def makeGood(self, s):

        l=[]
        p=False
        for i in s:
            if l and l[-1]!=i and (upper(l[-1])==i or lower(l[-1])==i):
                l.pop()
                continue
            l.append(i)
        return ''.join(l)
