class Solution(object):
    def rearrangeCharacters(self, s, t):

        a=Counter(s)
        b=Counter(t)

        m=float('inf')

        for i,j in b.items():
            r=a[i]//j
            m=min(m,r)
        return m

