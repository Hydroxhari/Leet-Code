class Solution(object):
    def findLucky(self, a):
        m=-1

        c=Counter(a)
        for i,j in c.items():
            if i==j:
                m=max(m,i)
        return m