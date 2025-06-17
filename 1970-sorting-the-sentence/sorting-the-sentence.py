class Solution(object):
    def sortSentence(self, s):
        r=s.split()
        l=['']*len(r)
        for i in r:
            l[int(i[-1])-1]=i[:-1]
        return ' '.join(l)