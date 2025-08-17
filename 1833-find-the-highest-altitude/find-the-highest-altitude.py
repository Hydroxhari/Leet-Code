class Solution(object):
    def largestAltitude(self, g):
        m=0
        c=0
        for i in g:
            c+=i
            m=max(m,c)
        return m