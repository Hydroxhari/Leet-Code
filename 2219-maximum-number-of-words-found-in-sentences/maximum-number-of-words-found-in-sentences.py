class Solution(object):
    def mostWordsFound(self, s):

        m=0

        for i in s:
            w=i.split()
            m=max(m,len(w))
        return m