class Solution(object):
    def rearrangeCharacters(self, s, t):
        c=Counter(s)
        r=Counter(t)

        a=float('inf')
        for i in r:
            n=c[i]/r[i]
            a=min(a,n)
        
        return a
