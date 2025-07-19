class Solution(object):
    def largestAltitude(self, g):

        m=0
        s=0
        for i in g:
            s+=i
            m=max(m,s)
        return m